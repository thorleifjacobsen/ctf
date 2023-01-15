package commands;

import java.io.PrintStream;

import utils.Config;

public class SetConfig extends Command {

    public Boolean execute(PrintStream out, Config cfg) {
        cfg.updateSettings(this.value, out);
        return true;
    }
}
