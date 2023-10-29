# Wires (easy)

On a recent trip I discovered this remarkable machine. It's a bit old, but I wonder what frequency it operates at?

Flag format: wack{frequency}

Author: Oblivion

PS: If you find a range of frequencies, submit the lowest number in the range as a flag.

📎 [wires.jpg](wires.jpg)

# Note

This task was updated with a `PS` after I tried it.

Looking at the floor it looks like Zuse Z1 or something. Googling it shows that this is a 1ghz computer. Testing this: `wack{1}`, failed!

Ok I try to Googling around and find out there is more Z machines. And since I'm 100% certain it must start with Z1 I try Googling `Z11` and so on. I only find the `Z11` and on this [Wikipedia article](https://en.wikipedia.org/wiki/Z11_(computer)) it says:

```
It consumed 2 kW of electricity, and operated mechanically at a frequency of 10 to 20 Hz. Both input and output were in decimal numbers, and it used floating-point arithmetic.
```

Testing 10 and profit!

# Flag

```
wack{10}
```