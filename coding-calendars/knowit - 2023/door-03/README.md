# Businessnissing

For å finansisere verksemda si som kvasi-guddommeleg gåveutdeler og absolutt dommer av snill og slem har Julenissen sett seg nødt til å spe på inntekta. Han har spart opp kapital og har byrja med aksjehandel. Aksjen han har sett seg ut, Foobar IT AS, er svært volatil, og svingar veldig frå time til time. Heldigvis er Nissen ein skarping (og har moglegens klarsyn som ein av evnane sine) og nyttar dette til å maksimere profitt.

## Oppgåve

Nissen startar med 200 000 NOK. Kvar dag kjøpar han så mange aksjar han har råd til, og sel alle saman før dagen er over. Han avsluttar altså alle dagar med 0 aksjar, og han kan kun kjøpe og selje ein gang pr dag. Nissen må kjøpe og selge kvar dag, men han gjer alltid den optimale handelen.

I [denne fila](./input.txt) viser kvar linje aksjekursen time for time så lenge børsen er open for ein gitt dag. Kor mykje pengar sit nissen att med når månaden er over?

## Døme

For desse tre dagane, og med ein startkapital på 1 000 kroner sit Julenissen att med 14 210 kroner.

```
112,85,65,192,172,213
```
```
165,146,188,102,119,156
```
```
123,187,92,71,208,148
```

# Solution

```javascript
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
// Total at end: 4536319363554735560
```