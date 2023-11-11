De strenge alvene har skrevet ned et julekodeord, men i den ivrige sorteringen av pakker har det skjedd en horribel feil og alt er blitt rot! Ordet har blitt borte i det som ser ut som et virrvarr av tilfeldig tekst! Nå trenger de hjelp til å gjenfinne ordet. De har null peiling på hvor langt ordet er. Kan du å gjenfinne ordet?

\- Mellomleder

📎random_text.bin

# Writeup

I saw in VSCode that the file had null bytes. So I made a script to split it by this. Then I tried to extract lines containing the flag start and `{` `}`. Saw I only found two lines starting with the characters. I googlec "Null Pointer" (Ref: Null Peiling) it was something to do with address. This was a big rabbit hole and gave me nothing. 

So I thought maybe it had to be the first letter in each line. Making a script to output that was not hard but it made no sense,  i see that the `}` occured long before the `{`. Then I tried to `rotate` it (Ref: `rot` in challeng text). So next I thought I had to sort it by something. All I had which made sense was the length. Doing so revealed quickly a flag! :) 

After second thought it makes sense as `sorting` is a keyword all along the challenge text.


```javascript
const fs = require("fs");
let data = fs.readFileSync("random_text.bin", "utf-8");

data = data.split("\u0000").sort((a, b) => a.length - b.length);

for (let val of data) {
  process.stdout.write(val.charAt(0));
  if(val.charAt(0) == "}") break 
}
```