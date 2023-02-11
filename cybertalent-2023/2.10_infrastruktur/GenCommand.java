import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.security.InvalidKeyException;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.Signature;
import java.security.SignatureException;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.time.Instant;
import java.util.Base64;

import commands.*;

public class GenCommand {
    static String FLAG = "c460f0338c3d541b15e59a1d29dd4252";
    static String privateKey = "MIICXAIBADCCAjUGByqGSM44BAEwggIoAoIBAQCPeTXZuarpv6vtiHrPSVG28y7FnjuvNxjo6sSWHz79NgbnQ1GpxBgzObgJ58KuHFObp0dbhdARrbi0eYd1SYRpXKwOjxSzNggooi/6JxEKPWKpk0U0CaD+aWxGWPhL3SCBnDcJoBBXsZWtzQAjPbpUhLYpH51kjviDRIZ3l5zsBLQ0pqwudemYXeI9sCkvwRGMn/qdgYHnM423krcw17njSVkvaAmYchU5Feo9a4tGU8YzRY+AOzKkwuDycpAlbk4/ijsIOKHEUOThjBopo33fXqFD3ktm/wSQPtXPFiPhWNSHxgjpfyEc2B3KI8tuOAdl+CLjQr5ITAV2OTlgHNZnAh0AuvaWpoV499/e5/pnyXfHhe8ysjO65YDAvNVpXQKCAQAWplxYIEhQcE51AqOXVwQNNNo6NHjBVNTkpcAtJC7gT5bmHkvQkEq9rI837rHgnzGC0jyQQ8tkL4gAQWDt+coJsyB2p5wypifyRz6Rh5uixOdEvSCBVEy1W4AsNo0fqD7UielOD6BojjJCilx4xHjGjQUntxyaOrsLC+EsRGiWOefTznTbEBplqiuH9kxoJts+xy9LVZmDS7TtsC98kOmkltOlXVNb6/xF1PYZ9j897buHOSXC8iTgdzEpbaiH7B5HSPh++1/et1SEMWsiMt7lU92vAhErDR8C2jCXMiT+J67ai51LKSLZuovjntnhA6Y8UoELxoi34u1DFuHvF9veBB4CHEmpCtwxqqMebAtshfrP2cvdJjX89l/FzO6P1/Q=";

    private static Command genCommand() {
        return genCommand("ALL");
    }

    private static Command genCommand(String recipient) {
        return genCommand(recipient, "NOP");
    }

    private static Command genCommand(String recipient, String type) {
        return genCommand(recipient, type, "");
    }

    private static Command genCommand(String recipient, String type, String value) {
        return genCommand(recipient, type, value, 0);
    }

    private static Command genCommand(String recipient, String type, String value, long runAfter) {
        Command cmd;
        switch (type) {
            case "CMD":
                cmd = new Execute();
                break;
            case "GETCFG":
                cmd = new GetConfig();
                break;
            case "SETCFG":
                cmd = new SetConfig();
                break;
            case "NOP":
                cmd = new Nop();
                break;
            default:
                return null;
        }

        cmd.recipient = recipient;
        cmd.value = value;
        cmd.runAfter = Instant.ofEpochMilli(runAfter * 1000);

        return cmd;
    }

    public static void main(String[] args) {
        String filename = "cmd";

        Command c;
        if (args.length == 2)
            c = genCommand(args[0], args[1]);
        else if (args.length == 3)
            c = genCommand(args[0], args[1], args[2]);
        else if (args.length == 4)
            c = genCommand(args[0], args[1], args[2], Long.parseLong(args[3]));
        else if (args.length == 5) {
            c = genCommand(args[0], args[1], args[2], Long.parseLong(args[3]));
            filename = args[4];
        } else {
            System.out.println("Usage: gencmd: RECIPIENT TYPE [VALUE [RUN_AFTER [OUTFILE]]]");
            System.out.println("    RECIPIENT: Id as hexadecimal, or 'ALL'");
            System.out.println("    TYPE:      One of CMD, GETCFG, SETCFG, NOP.");
            System.out.println("    VALUE:     Command specific. Default: ''");
            System.out.println("    RUN_AFTER: Unix timestamp of when to run command. Default: 0 or ASAP");
            System.out.println("    OUTFILE:   Write command to this file. Default: ");
            return;
        }

        if (c == null) {
            System.out.println("Invalid command");
            return;
        }

        try {
            KeyFactory keyFactory = KeyFactory.getInstance("DSA");
            PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(Base64.getDecoder().decode(privateKey.getBytes()));
            PrivateKey priv = keyFactory.generatePrivate(keySpec);
            Signature sign = Signature.getInstance("SHA256withDSA");

            sign.initSign(priv);
            sign.update(c.asString().getBytes());
            c.signature = sign.sign();

            FileOutputStream fileOut = new FileOutputStream(filename);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(c);
            out.close();
            fileOut.close();
            System.out.printf("Wrote command to `%s`\n", filename);
            c.display(System.out);

        } catch (InvalidKeySpecException | NoSuchAlgorithmException | InvalidKeyException | SignatureException
                | IOException e) {
            System.out.println("Signing command failed!");
            e.printStackTrace();
        }
    }
}