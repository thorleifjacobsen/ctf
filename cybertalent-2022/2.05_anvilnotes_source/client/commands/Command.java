package commands;

import java.io.PrintStream;
import java.security.InvalidKeyException;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.PublicKey;
import java.security.Signature;
import java.security.SignatureException;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.X509EncodedKeySpec;
import java.time.Instant;
import java.util.Base64;

import utils.Config;

public abstract class Command implements java.io.Serializable {
    public String recipient;
    public Instant runAfter = Instant.now();
    public String value = "";
    public byte[] signature;

    // Run command
    public abstract Boolean execute(PrintStream out, Config cfg);

    // Check signature
    public Boolean verify() {
        String pubkey = "MIIDQjCCAjUGByqGSM44BAEwggIoAoIBAQCPeTXZuarpv6vtiHrPSVG28y7FnjuvNxjo6sSWHz79NgbnQ1GpxBgzObgJ58KuHFObp0dbhdARrbi0eYd1SYRpXKwOjxSzNggooi/6JxEKPWKpk0U0CaD+aWxGWPhL3SCBnDcJoBBXsZWtzQAjPbpUhLYpH51kjviDRIZ3l5zsBLQ0pqwudemYXeI9sCkvwRGMn/qdgYHnM423krcw17njSVkvaAmYchU5Feo9a4tGU8YzRY+AOzKkwuDycpAlbk4/ijsIOKHEUOThjBopo33fXqFD3ktm/wSQPtXPFiPhWNSHxgjpfyEc2B3KI8tuOAdl+CLjQr5ITAV2OTlgHNZnAh0AuvaWpoV499/e5/pnyXfHhe8ysjO65YDAvNVpXQKCAQAWplxYIEhQcE51AqOXVwQNNNo6NHjBVNTkpcAtJC7gT5bmHkvQkEq9rI837rHgnzGC0jyQQ8tkL4gAQWDt+coJsyB2p5wypifyRz6Rh5uixOdEvSCBVEy1W4AsNo0fqD7UielOD6BojjJCilx4xHjGjQUntxyaOrsLC+EsRGiWOefTznTbEBplqiuH9kxoJts+xy9LVZmDS7TtsC98kOmkltOlXVNb6/xF1PYZ9j897buHOSXC8iTgdzEpbaiH7B5HSPh++1/et1SEMWsiMt7lU92vAhErDR8C2jCXMiT+J67ai51LKSLZuovjntnhA6Y8UoELxoi34u1DFuHvF9veA4IBBQACggEADkENe3FyODSBndQfXkLHhXJWJr43CgzKOm3IauPLMOcKLipK3Ta8fzVLMZnnlqzcdiwhqI4wKtUz5K5ZXzuQ6BKAGPPgwYyzAJ32eYiC6GXtvOquBS38WSgz7k5WbJ+gvVAHiWnFtvlLZT0l2rtn2m2AyJaVbCiZxt18qzIPfLV5lNF8y/MOyBiWTJ0ooPwspQchURyl8JbMdHmoYovSscHNygYTPUleg7we00Q2hPiEKYMHrj+UBYzMhrmCSGoNHBV27IjK+KGEKEb1l8JZbu/4hI4S1YeJGLcZ9mROSrb4+BNpHzteZAF+MNDKPvTgVeDjNGAnIi4j+yhp0HqmHA==";
        try {
            KeyFactory keyFactory = KeyFactory.getInstance("DSA");
            X509EncodedKeySpec keySpec = new X509EncodedKeySpec(Base64.getDecoder().decode(pubkey.getBytes()));
            PublicKey pub = keyFactory.generatePublic(keySpec);
            Signature sign = Signature.getInstance("SHA256withDSA");

            sign.initVerify(pub);
            sign.update(asString().getBytes());
            return sign.verify(signature);
        } catch (NoSuchAlgorithmException | InvalidKeyException | InvalidKeySpecException | SignatureException e) {
            return false;
        }
    }

    public void display(PrintStream out) {
        out.print(asString());
    }

    public String asString() {
        runAfter.minusMillis(runAfter.toEpochMilli() % 1000);
        return String.format(
                "- Recipient: %s\n- When: %s\n- Type: %s\n- Value: %s\n",
                recipient, runAfter, getClass(), value);
    }
}
