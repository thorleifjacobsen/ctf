# Azure Function

We have found a function app called function-lab-rivsec which has a HTTP trigger named RivSecFunction1. Can you find the application, interact with the function and authenticate to it? Apparently it expects a special input and value to authenticate.

My coworker said he stored it on the CTF platform, but I can't seem to see it. Are you able to?

Note, it is not necesarry to do content-discovery on the CTF platform to solve this task.

# Writeup

Quickly googled "How does azure functions work" ended up at [this website](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-serverless-api) which shows an example url. It shows it requires 3 bits. App name, function name and code.

```
http://<yourapp>.azurewebsites.net/api/<funcname>?code=<functionkey>
```

I have the two first `function-lab-rivsec` and `RivSecFunction1`. The code I have no idea where to find, so I start checking source on every page searching for `<!--`. Nothing, then it strikes me what about all challenges? Going from bottom and up I finally see it .. on THIS challenge.. Darn should have done that earlier.

```
<!--the code is kGwB9axaK4N7sTdBzO1SfPzNjsp17KCR25yQ4dTYBePoAzFuii5p_w== -->
```

So just send the code now and I get the flag:

```console
toffe@kali:~$ curl https://function-lab-rivsec.azurewebsites.net/api/RivSecFunction1?code=kGwB9axaK4N7sTdBzO1SfPzNjsp17KCR25yQ4dTYBePoAzFuii5p_w== 

Well done, you've found the authentication code! This allowed you to authenticate to the function and you could now explore its functionality. Todays challenge ends here, with a 🚩: RSXC{AUTHENTICATED_AZURE_FUNCTION}. We at River Security (rivsec) are proud of you!
```

# Flag

```
RSXC{AUTHENTICATED_AZURE_FUNCTION}
```