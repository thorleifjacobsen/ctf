# Comms Flag (2)

Next was `Comms` and guessing it has something to do with communication (`RX`/`TX`) on the board I hook up the FTDI, this time I search the code for baud and find the [baud rate of 38400](https://github.com/So11Deo6loria/bsidesKristiansand2025Badge/blob/main/firmware/constants.py#L75).

Hooking up my FTDI adapter with RX to TX and vise versa + ground I can now open a serial session on baud 38400 and restart the device.

```bash
$ screen /dev/ttyUSB0 38400
INITIALIZED
```

Now I can press the button on the comms page

![Alt text](comms.png) 

and Voila flag 2 `Comms` pops up!

```bash
$ screen /dev/ttyUSB0 38400
INITIALIZED
DUCK_9FEDF9_C0MM5_2_0F9D6
```