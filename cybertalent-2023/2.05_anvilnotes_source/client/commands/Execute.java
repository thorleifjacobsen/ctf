package commands;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;

import utils.Config;

public class Execute extends Command {

    public Boolean execute(PrintStream out, Config cfg) {
        try {
            String[] args = { "bash", "-c", this.value };
            Process p = Runtime.getRuntime().exec(args);
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            out.printf("Executing command '%s':\n", this.value);
            String line;

            // Read stdout
            while ((line = reader.readLine()) != null) {
                out.println(line);
            }

            // Read stderr
            reader = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            while ((line = reader.readLine()) != null) {
                out.println(line);
            }

            int exit = p.waitFor();
            out.printf("\nExit %d\n", exit);
            return true;

        } catch (IOException | InterruptedException e) {
            out.printf("Error while executing command '%s':\n", this.value);
            e.printStackTrace(out);
            return false;
        }
    }

}
