# Mystic zip and mystic car (OSINT/Cracking easy)

I was sitting at Åpent Bakeri Frogner, enjoying a coffee, when a dark car drove by. A USB flash drive fell out of the window, but I only managed to catch the beginning of the license plate, CD 601, before the car disappeared around a corner. So, I won't be able to return the flash drive either. Moreover, I'm unable to bypass the password on the ZIP file that was on the flash drive, even though I tried both an English and a Norwegian word list.

Author: oksenmu

📎 [secrets.zip](secrets.zip)

# Writeup

The database at `regnr.info` displays a collection of vehicles identifiable by their registration numbers, all commencing with the code CD601. These vehicles are designated as ambassador cars, serving as official vehicles for foreign embassies or diplomatic missions in Norway.

```
CD60100	VOLVO XC90 C CM91	2004	Svart	Personbil
CD60103	SAAB 9-3 YS3F F4F	2004	Svart	Personbil
CD60105	AUDI A6, S6 4F ABMKQ1	2005	Grå	Personbil
CD60106	VOLVO XC70 S SZ71	2006	Blå	Personbil
CD60107	VOLVO XC70 S SZ71	2006	Grå	Personbil
CD60109	FORD FOCUS DAW C9DB1	2001	Sølv	Personbil
CD60110	OPEL VIVARO X83 FJ11	2007	Svart	Personbil
CD60111	BMW 325XI 390X VT11	2007	Svart	Personbil
CD60112	BMW 320D 390L VU51	2007	Sølv	Personbil
CD60113	AUDI A4 B8 ACALAQ1	2008	Grå	Personbil
CD60114	Toyota Prado Gx BK29J	2006	Rød	Personbil
CD60116	Audi A4 Avant Quattro 8E	2005	Grå	Personbil
```

Assuming dark cars means black:


```
CD60100	VOLVO XC90 C CM91	2004	Svart	Personbil
CD60103	SAAB 9-3 YS3F F4F	2004	Svart	Personbil
CD60110	OPEL VIVARO X83 FJ11	2007	Svart	Personbil
CD60111	BMW 325XI 390X VT11	2007	Svart	Personbil
```

Then only two of them are still in use:

```
CD60100	VOLVO XC90 C CM91	2004	Svart	Personbil
CD60103	SAAB 9-3 YS3F F4F	2004	Svart	Personbil
```

My plan was to find the owner of the cars online but `BankID` required to sign in and see car owners was down this night. Complaining to friend he told me that all cars starting with that number belongs to the `Netherlands` so that sped things up.

[Here is a site with overview for thos interested](http://www.olavsplates.com/norway_diplomat_codelist.html)

I then used `fcrackzip` with a dutch wordlist to get the key:

```bash
└─$ fcrackzip  -b -D -p Dutch_Norm_All.txt -u ./secrets.zip 
```

Key was: `vennootschapsbelasting`

Then just extract the zip and there was a base64 encoded file which contained the flag.

```bash
└─$ echo d2Fja3sxNG45dTQ5M181cDNjMWYxY193MHJkXzExNTc1XzRyM19uMWMzfQ== | base64 -d
wack{14n9u493_5p3c1f1c_w0rd_11575_4r3_n1c3}
```

# Flag

```
wack{14n9u493_5p3c1f1c_w0rd_11575_4r3_n1c3}
```