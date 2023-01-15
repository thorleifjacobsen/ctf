package commands;

import java.io.PrintStream;

import utils.Config;

public class GetConfig extends Command {

    public Boolean execute(PrintStream out, Config cfg) {
        out.print(cfg.asString());
        return true;
    }
}
