// Load values from file:
const fs = require("fs");
let days = fs.readFileSync("input.txt", "utf-8");

// Parse data:
days = days.split("\n") // Split data into days
           .map(day => day.split(",") // Split days into hours
           .map(value => parseInt(value))); // Convert value to number

// Loop through days and hours:
let wallet = 200000n;
for (const day of days) {
  let bestDiff = 0;
  let bestBuyPrice = 0;
  let bestSellPrice = 0;

  // Loop to find the best buy and sell price:
  for (let price of day) {
    // Loop through the rest of the day to find the best sell price and see the diff.
    for (let hour = day.indexOf(price)+1; hour < day.length; hour++) {
      let diff = day[hour]-price;
      if (diff > bestDiff) {
        bestDiff = diff;
        bestBuyPrice = price;
        bestSellPrice = day[hour];
      }    
    }
  }
  

  // Now lets buy and sell.  
  const eligableToBuy = wallet / BigInt(bestBuyPrice); // BigInt always rounds down
  wallet -= eligableToBuy * BigInt(bestBuyPrice);
  wallet += eligableToBuy * BigInt(bestSellPrice);

  // Print result for debugging and overview:
  process.stdout.write(`Day: ${(days.indexOf(day)+1).toString().padEnd(10)}`);
  process.stdout.write(`Buy: ${bestBuyPrice.toString().padEnd(8)}`);
  process.stdout.write(`Sell: ${bestSellPrice.toString().padEnd(8)}`);
  process.stdout.write(`Earning: ${(bestSellPrice-bestBuyPrice).toString().padEnd(10)}`);
  process.stdout.write(`Number: ${eligableToBuy.toString().padEnd(20)}`);
  process.stdout.write(`Wallet: ${wallet}\n`);
}

console.log(`Total at end: ${wallet}`);