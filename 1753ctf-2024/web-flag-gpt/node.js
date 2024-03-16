let msg = "flaflagg hehe"

do {
    console.log(msg, msg.indexOf("flag"));
    msg = msg.replace(/(flag)/i, "");
} while (msg.indexOf("flag") > -1)

