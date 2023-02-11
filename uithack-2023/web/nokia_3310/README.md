# Nokia 3310

This brick of a mobilephone was probably the peak of technology as we know it. It does not break, it will not run out of battery, you can use it as armor and as a weapon! What can this thing not do?!

Use this excellent item to retrive the flag by sending uithack23 flag

motherload.td.org.uit.no:8000/

# Writeup

Tried to type it inn the browser but it seems to have a short timeout, so made a python script to do it. See (script.py)[script.py]

# Revisited:

I asked why I had to send additional characters and the explanation is really simple. The reason was that the server did not "add" the G before a given time as it was waiting for additional presses on the same key in case we wanted another character. So it takes about 0.5 sec before it settles. And when I commited without waiting the message was without the last character. If i just waited 0.5 sec to commit it would work no problems. 