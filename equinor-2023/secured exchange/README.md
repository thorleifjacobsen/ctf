# SECURED EXCHANGE

Our financing department has developed their own ultra secure methods of transferring vital financial reports. See if you can find a flaw in their plan

[secured.pcap](secured.pcap])

# Writeup

I quickly open the PCAP file in WireShark and see some HTTP Requests to [secure.html](secure.html):

![ws-http](ws-http.png)

It hints to a FTP so I change the filter to FTP and see this:

![ws-ftp](ws-ftp.png)

I see they are downloading a list of files and a flag.zip

![Alt text](ws-ftp-files.png)

So I follow the tcp stream to get all the data and convert to raw and downloads it as [flag.zip](flag.zip)

![stream](ws-tcp-stream.png)
![export](ws-exportzip.png)

Trying to unzip the file shows that it is password protected:

```bash
└─$ unzip flag.zip 
Archive:  flag.zip
[flag.zip] flag.txt password: 
```

Looking for more in the dump I see a mail there in there it tells me a password:

![mail](ws-smtp.png)

And unzipping with that gives me [flag.txt](flag.txt)

# Flag

```
EPT{DuDe_WheRe_Is_My_FlAg}
```