// Load values from file and split into array:
const fs = require("fs");
const log = fs.readFileSync("log.txt", "utf-8").toLowerCase().split(",");

// Object to keep track of lockstate and pickedLocks
let lockState = {
  pinStatus: Array(7).fill(false),
  pickedLocks: 0,
  isOpen() { return this.pinStatus.every(value => value === true); },
  lock() { this.pinStatus = Array(7).fill(false); }
};

for (let logEntry of log) {

  // Parse log entry
  logEntry = logEntry.trim().toLowerCase().split(" ");
  const pin = parseInt(logEntry[2])-1;
  const isOpen = logEntry[0] === "klikk";

  // Set pin state:
  lockState.pinStatus[pin] = isOpen;

  // If open we add it to picked and locks it up again:
  if(lockState.isOpen()) { 
    lockState.pickedLocks ++;
    lockState.lock();
  }
}

console.log(`Number of picked locks: ${lockState.pickedLocks}`);