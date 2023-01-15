package commands;

import java.io.PrintStream;

import utils.Config;

public class Nop extends Command {

    public Boolean execute(PrintStream out, Config cfg) {
        out.printf("Doing nothing with this value: %s\n", this.value);
        return true;
    }
}
