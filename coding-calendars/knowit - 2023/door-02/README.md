# Klikk klikk klakk 

På fritida driv alven Alfred med låssport, kompetativ dirking av låsar. Han har kjøpt inn ein stor mengde låsar og prøvar å løyse alle så fort som råd. Kvar lås har 7 låsestifter i sylinderen. Alle stiftene startar i låst posisjon. Når han dirkar kan han anten få løfta ein av stiftene i låsen opp i ulåst posisjon med eit tilfredsstillande klikk, eller så kan ein allereide løfta stift falle ned i låst posisjon med eit demotiverande klakk.

### Oppgåve

I eit forsøk på å bli meir datadreven i hobbyen sin har Alfred loggført dirkinga si i [denne fila](log.txt). Han går ikkje vidare til ein ny lås før han har dirka opp den han held på med. Kor mange låsar har Alfred dirka opp?

# Solution

```javascript
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
// Number of picked locks: 393
```