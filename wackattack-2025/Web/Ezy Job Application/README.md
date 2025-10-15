# Ezy Job Application

Apply here to get your first job at WackCorp! We look at all applications 👀

[🔗 http://13.49.221.255:80](http://13.49.221.255:80)

[⬇️ ez-job-application.tar.gz](./ez-job-application.tar.gz)

# Writeup

Analyzing main.go:

This has the main website we see, then it has a few more endpoints only for local use. When we register it puts our data into an array of sorts then gets the bot.ts to open `/admin/registration/{id}` with puppteer which renders the same template we see but with a twist:

```html
{{if .Address}}
<div class="result" role="status" aria-live="polite">
    <p>Thanks — your application is received and you're on the waitlist.</p>
    <p class="small">LinkedIn: <a href="{{.LinkedIn}}" target="_blank" rel="noopener noreferrer" id="linkedin">LinkedIn Profile</a></p>
    <p class="small">Registered email: <span class="meta">{{.Address}}</span></p>
    <p class="small">Your position in line: <span class="meta">{{.Id}}</span></p>
</div>
{{end}}
```

These fields will be populated for the bot and any script we can inject will be run. The exploit is most likely in the linkedin url which only is checked that it basically starts with `https://www.linkedin.com` and everything after is modifiable.




# Flag

```
flag{goes_here}
```