# Phish me plz

You are a frequent user of a devious cyberservices marketplace on the Dark Web.

A new contract has been placed by a client seeking financial information from `HackProof Banking Corperation` as username `iceman`. The contract informs you that iceman has received cyber security training to detect phishing. A well crafted phishing attack might still work.

For this contract you could use SilentShadow, a Dark Web PHaaS (phishing-as-a-service) platform. A well crafted phishing email can be sent to the target to lure him to visit a fake website resembling Hackproof Banking Corperation. The user might not detect he is on the wrong website and could accidentally disclose his username and password, aswell as a valid MFA code.

[🔗 https://helsectf2025-42694257c6fdb3976dd6-hackproof-banking.chals.io/login](https://helsectf2025-42694257c6fdb3976dd6-hackproof-banking.chals.io/login)
[🔗 https://helsectf2025-42694257c6fdb3976dd6-silentshadow.chals.io/phish](https://helsectf2025-42694257c6fdb3976dd6-silentshadow.chals.io/phish)

# Writeup

I started by making a NodeJS application replicating the behaivor or `helsectf2025-42694257c6fdb3976dd6-hackproof-banking.chals.io` which redirected me to `/login` then I copied the content of the website into `step1.html` and made a output which shows me what he inputs when logging in. 

To host it I opened up the port `1234` on my router to my computer and sent the URL to the target. 

It resulted in: 

```
Listening on port 1234
Login requested with next=/
Login requested with next=/
Login attempt with username = iceman and password = c56a574eaf7c99a53bbf
```

Then when I tried that I was met with a MFA page which I copied and added to `step2.html`, a modification to handle that was made to my nodejs script to reveal a OTP code:

```
2FA Request
2FA verification with otp = 823495
Login requested with next=/
```

Then I quickly logged in using the username, password and OTP and voila. Flag achived!

# Flag

```
helsectf{bypassing_MFA_was_too_easy!}
```