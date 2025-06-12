# Nahamcon 2025

I participated a small amount here helping on team Dugnad, team Dugnad ended up in first place the following tasks were the one I did something in

![alt text](image.png)

## My Third CTF

This was some kind of fuzzing challenge on the URL but we had no idea on what the url was. According to the first and second of this they had a random "rot-1" and "rot-2" on them. So with the given `easy.txt` dictionary I made this script to rotate everything:

```python
def rotate(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rotated = chr((ord(char) - base + shift) % 26 + base)
            result.append(rotated)
        else:
            result.append(char)
    return ''.join(result)

with open("easy.txt", "r") as infile:
    content = infile.read()

with open("all_easy.txt", "w") as outfile:
    for i in range(1, 28):
        outfile.write(f"ROT+{i}:\n{rotate(content, i)}\n\n")
    for i in range(1, 28):
        outfile.write(f"ROT-{i}:\n{rotate(content, -i)}\n\n")
```

Then running ffuf on the domain multiple times until I found a flag:

`ffuf -w alls27_easy.txt -u http://challenge.nahamcon.com:30000/FUZZ -ac`

Once done I found the path: `/qbhf/oguucig/wrnhq/lewl/` which seems to be: -1, -2, -3 and -4 rotation for `page/message/token/hash`. [CyberChef](https://cyberchef.org/#recipe=ROT13(true,true,false,-4)&input=L3FiaGYvb2d1dWNpZy93cm5ocS9sZXdsLw) link just press -1 on it and see the words appear.

## 🩸 Access All Areas

Website has a `Download Log` button which downloads a log in PDF. There is a method to post data to the log but we did not find more. The `log.php` seems to take a filename and there we found a entry:

Opening `http://challenge.nahamcon.com:30244/api/log.php?log=../var/log/nginx/access.log` gives me access to the Nginx logs. So it seems to be able to dump all `.log` files, from there on a Discord user MrFreddi007 found that if you added HTML to your user agent it would be rendered when dumping nginx access logs. So his attempt was:

`curl http://challenge.nahamcon.com:31644/ -H "User-Agent: <iframe src='file:///etc/passwd'></iframe>"`

Then do the access log dump and you could see a iframe with the content.

[source](https://www.triskelelabs.com/microstrategy-ssrf-through-pdf-generator-cve-2020-24815)