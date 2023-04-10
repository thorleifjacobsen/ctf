# Azure Function Enumeration

In the previous challenge you found an Azure Function. This function holds functionality which you must discover. Azure Functions with a HTTP trigger responds to GET and POST parameters, can you find the needed parameter?

# Writeup

```
URL: https://function-lab-rivsec.azurewebsites.net/api/RivSecFunction1?code=kGwB9axaK4N7sTdBzO1SfPzNjsp17KCR25yQ4dTYBePoAzFuii5p_w==
```

So seeing the docs I saw that you can set the script to accept both GET and POST parameters. I guess they have added an `if GET['whatever'] exists { show flag 2 }`. 

So I tried to add `&flag=1`, I tried to brute with a few million words. Common english words, dirbuster wordlists e.t.c.

Nothing hit. It might be anything, so there must be some kind of hint? The website shows:

```
Well done, you've found the authentication code! This allowed you to authenticate to the function and you could now explore its functionality. Todays challenge ends here, with a 🚩: RSXC{AUTHENTICATED_AZURE_FUNCTION}. We at River Security (rivsec) are proud of you!
```

Analyzing this and the challenge description I cannot find anything smart. I tried `viewAccess`, `grantAccess`, `a` from the previous [View Access](../View%20Access/) challenge. Nothing! Seems like a wild goosechase. So I made a list of words in the message and challenges:

```
flag
access
give
show
grant
function
azure
enumeration
trigger
respond
parameter
hidden
secret
functionality
explore
rivsec
proud
```

Using `wfuzz` I try to fuzz all them with other words using a list of 370105 words. I uppercased the words as it is most likely camel case. This wold create words like `flagShow`.

```console
toffe@kali:~$ wfuzz -t100 --hh 264 -u "https://function-lab-rivsec.azurewebsites.net/api/RivSecFunction1?code=kGwB9axaK4N7sTdBzO1SfPzNjsp17KCR25yQ4dTYBePoAzFuii5p_w==&FUZ1ZFUZ2Z=1" -z file,customWords.txt -z file,words_upper.txt
```

This makes it get the first word from [customWords.txt](customWords.txt) and combine it with every word in [words_upper.txt](words_upper.txt). Then it goes to the next word in `customWords`. So with around 4441260 words at 500 requests/sec it will take around two hours to go through all. 

But every time I set it up it eats RAM and crashes in the end. So I get to around 100k words. This makes me just play around with hundres of more wordlists and nothing seems to work. Trying to fix this problem I find this [issue](https://github.com/xmendez/wfuzz/issues/323#issuecomment-1458891395) where he mention `ffuf`. I try that and fall in love! New tool to the toolbox! :) 

I kinda gave up as I felt there was no clues to how the format of the variable was, how many words, what words.. But then someone took my 2nd place. I was thinking about giving up but a bit of motivation speech and i retried my original attempt with ffuf instead.

```console
toffe@kali:~$ ffuf -t 100 \
     -fs 267 \
     -u "https://function-lab-rivsec.azurewebsites.net/api/RivSecFunction1?code=kGwB9axaK4N7sTdBzO1SfPzNjsp17KCR25yQ4dTYBePoAzFuii5p_w==&FIRSTLAST=1" \
     -w customWords.txt:FIRST \
     -w words_upper.txt:LAST
```

So I let this go and leave it. But after a quick YouTube video I see it popped up with something:

```console
        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : https://function-lab-rivsec.azurewebsites.net/api/RivSecFunction1?code=kGwB9axaK4N7sTdBzO1SfPzNjsp17KCR25yQ4dTYBePoAzFuii5p_w==&FIRSTLAST=1
 :: Wordlist         : FIRST: customWords.txt
 :: Wordlist         : LAST: words_upper.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 100
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 267
________________________________________________

[Status: 200, Size: 204, Words: 32, Lines: 1, Duration: 171ms]
    * LAST: Admin
    * FIRST: rivsec
```

I have no idea on how ffuf did that, rivsec is nearly at the end but it had only completed around 60k words.. Seems like this takes the first word of the biggest list agains the words in the smallest. Which makes it hit quicky as "Admin" is around number 4000. "rivsec" is 11.. That is ~44000 attempts.

Well visiting that shows this message:

````
Oh, wow 🔥 You've found a secret input parameter. This could provide you access to more of the functions capabilities. For now, the challenge ends here, and here is your 🎌: RSXC{FUNCTION_ENUMERATION}
```

# Flag

```
RSXC{FUNCTION_ENUMERATION}
```