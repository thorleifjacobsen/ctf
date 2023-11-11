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
