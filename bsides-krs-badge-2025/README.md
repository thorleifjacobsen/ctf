# BSides Kristiansand 2025 Badge

I've heard there was a badge to hack at the BSides Kristiansand cybersecurity conference and since I was attending I brought my computer, FTDI adapter and some jumper wires.

# Initial Thoughts

When arriving we recieved the badge and two batteries. Looking at it I initially found:

- UART Pin header
- Raspberry Pi Pico with micro usb
- Toggle Switch
- Morse Code Table
- GitHub link

The device has to work offline so all flags are stored on them, accessing the file system would likely give me all flags. Also looking at the source as long as you know the device ID you can re-generate all flags based on the source of [flagManager.py](https://github.com/So11Deo6loria/bsidesKristiansand2025Badge/blob/main/firmware/flagManager.py)

But lets not start there, lets do it the intended way.

## Badge Images

![badge](./badge_front.png)
![badge](./badge_back1.png)
![badge](./badge_back2.png)

# Flags

[Flag 1 - Easy](./flag1/)
[Flag 2 - Comms](./flag2/|)
[Flag 3 - Creds](./flag3/)
[Flag 4 - Firmware](./flag4/)
[Flag 5 - Authorized](./flag5/)
[Flag 6 - Respond](./flag6/)
[Flag 7 - Secure](./flag7/)
[All - Alternative way](./fastlane/)

# Conclusion

The badge as my first was a fun challenge, Used a bit too long to get a stable connection but when we figured out what the problem was and I got to borrow a USB cable it was all jolly from there.

Thanks for a great new piece on my CTF journey!