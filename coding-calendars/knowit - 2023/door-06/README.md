# Reiserute

Julenissen skal levere pakker til alle byene i landet og har fått utlevert en rute av alvene sine. Ruten forteller julenissen koordinatene til alle byene som skal besøkes i hvilke rekkefølge. Noen byer må besøkes flere ganger pga. høye fjell i området rundt byene. Julenissen er miljøbevist og ønsker ikke å ta med seg for mye lyng og lav til reinsdyrene sine. Men han ønsker hvertfall ikke ta med seg for lite lyng og lav. Da blir både Rudolf og reinsdyret Euclid gretten og julenissen kommer seg ikke gjennom hele ruta i tide!

Ruta ligger i denne fila rute.txt. Hver linje i fila representerer koordinatet til én by. Julenissen starter og avslutter reisen sin i samme by med koordinatet -1000,-400. Dette koordinatet betyr at byen ligger 1000 km vestover og 400 km sørover.

Hvert reinsdyr spiser 1 kg lyng og lav per tusende kilometer. Julenissen har ni reinsdyr. Hvor mange kg lyng og lav trenger julenissen ta med seg? Han orker ikke måle så nøye så rund opp til nærmeste heltall.

# Solution

```javascript
// Load values from file:
const fs = require("fs");
let route = fs.readFileSync("rute.txt", "utf-8");


// Parse data:
route = route.split("\n") // Split data into days
           .map(value => value.split(",")); // Convert value to number


lastStop = route.shift();
totalDistance = 0;

for (nextStop of route) {
    totalDistance += Math.sqrt(Math.pow(lastStop[0] - nextStop[0], 2) + Math.pow(lastStop[1] - nextStop[1], 2));
    lastStop = nextStop;
}

console.log(Math.ceil(totalDistance/1000*9));

```

or 

```bash
awk -F',' '{x[NR]=$1;y[NR]=$2} END{for(i=1;i<NR;i++){d+=sqrt((x[i]-x[i+1])^2 + (y[i]-y[i+1])^2)};print int(d/1000*9+0.5)}' rute.txt
```