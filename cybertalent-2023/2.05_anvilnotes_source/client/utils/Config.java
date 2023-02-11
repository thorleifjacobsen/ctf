package utils;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintStream;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Random;

import commands.Command;

public class Config implements java.io.Serializable {
    private static int DEFAULT_SLEEP_DURATION = 60;
    private static String DEFAULT_SERVER_URL = "http://localhost/";

    public String id;
    public int sleepDuration;
    public String serverURL;
    public ArrayList<Command> pendingCommands;

    public Config() {
        id = "";
        Random rng = new Random();
        for (int i = 0; i < 8; i++)
            id += String.format("%02X", rng.nextInt(256));

        sleepDuration = DEFAULT_SLEEP_DURATION;
        serverURL = DEFAULT_SERVER_URL;

        pendingCommands = new ArrayList<Command>();
    }

    public static Config restore() {
        try {
            FileInputStream fd = new FileInputStream(".config");
            ObjectInputStream in;
            in = new ObjectInputStream(fd);
            Config cfg = (Config) in.readObject();

            in.close();
            fd.close();

            return cfg;
        } catch (FileNotFoundException e) {
            return new Config();
        } catch (IOException | ClassNotFoundException e) {
            new File(".config").delete();
            return new Config();
        }
    }

    private void readObject(ObjectInputStream ois) throws IOException, ClassNotFoundException {
        id = ois.readUTF();
        sleepDuration = ois.readInt();
        serverURL = ois.readUTF();
        pendingCommands = new ArrayList<Command>();
        Instant now = Instant.now();
        int pendingCommandsSize = ois.readInt();
        for (int i = 0; i < pendingCommandsSize; i++) {
            Command c = (Command) ois.readObject();
            if (c.runAfter.isBefore(now))
                c.execute(System.out, this);
            else
                pendingCommands.add(c);
        }
    }

    private void writeObject(ObjectOutputStream oos) throws IOException {
        oos.writeUTF(id);
        oos.writeInt(sleepDuration);
        oos.writeUTF(serverURL);
        oos.writeInt(pendingCommands.size());
        for (Command c : pendingCommands)
            oos.writeObject(c);
    }

    public void persist() {
        try {
            FileOutputStream fileOut = new FileOutputStream(".config");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(this);
            out.close();
            fileOut.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Do sanity check of settings
    public Boolean verify() {
        if (id == null || id.length() != 16)
            return false;
        if (sleepDuration > 60 * 60 * 24)
            return false;
        if (!serverURL.startsWith("http://"))
            return false;
        return true;
    }

    public void updateSettings(String value, PrintStream out) {
        for (String pair : value.split(",")) {
            String[] kv = pair.split("=", 2);
            String k = kv[0];
            String v = kv.length == 2 ? kv[1] : "";

            switch (k) {
                case "sleepDuration":
                    setSleepDuration(Integer.parseInt(v));
                    break;

                case "serverURL":
                    setServerURL(v);
                    break;

                case "id":
                    setID(v);
                    break;

                default:
                    out.printf("Don't know how to handle setting: %s=%s\n", k, v);
                    break;
            }
        }
    }

    private void setServerURL(String url) {
        serverURL = url;
    }

    private void setSleepDuration(int duration) {
        sleepDuration = duration;
    }

    private void setID(String newID) {
        id = newID;
    }

    // Run all pending commands whose time has come
    public void execute(PrintStream out) {
        Instant now = Instant.now();
        for (int i = pendingCommands.size() - 1; i >= 0; i--) {
            Command c = pendingCommands.get(i);
            if (c.runAfter.isBefore(now)) {
                c = pendingCommands.remove(i);
                out.printf("# Executing:\n%s", c.asString());
                c.execute(out, this);
            }
        }
        persist();
    }

    public void display(PrintStream out) {
        out.print(asString());
        out.println("* Pending commands:");
        for (Command c : pendingCommands) {
            out.println("---");
            c.display(out);
        }
    }

    public String asString() {
        return String.format(
                "* ID: %s\n* sleepDuration: %d\n* serverURL: %s\n",
                id, sleepDuration, serverURL);
    }
}
