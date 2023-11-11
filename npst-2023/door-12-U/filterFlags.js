const fs = require("fs");

// Run dig +x ip 
const exec = require("child_process").execSync;

// Load allflags.txt
const allflags = fs.readFileSync("all_flags.txt", "utf-8").split("\n");

for (flag of allflags) {
  const ip = flag.split(" ")[0];
  const dig = exec(`dig +short -x ${ip}`).toString().split("\n");
  const hostname = dig[0];
  const domain = dig[1];
  const newflag = `${ip} ${hostname} ${domain}`;
  console.log(newflag);
}

// console.log(allflags.join("\n"));