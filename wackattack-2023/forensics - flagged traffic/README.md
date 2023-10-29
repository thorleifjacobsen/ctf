# Flagged Traffic (beginner)

I think someone is downloading flags on my network, but I couldn't find anything. Can you find something in this packet capture?

Author: Oblivion

📎 [Flagged_traffic.pcapng](Flagged_traffic.pcapng)

# Writeup

Using wireshark I quickly find HTTP traffic:

![wireshark.png](wireshark.png)

It seems to be PNG images, so exporting those by selecting one of the images and click like this:

![export.png](export.png)

Gives me all the flags I want. The interesting is the 1337 one:

![Fl4g_0f_P0l4nd.png](Fl4g_0f_P0l4nd.png)

# Flag

```
wack{7h3_gr34t_fl4g_f1nd3r}
```