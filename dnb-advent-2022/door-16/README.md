# Writeup

Looking at the source from that link, adding ?test gives source. 
So it seems like the server is configured somehow to render index.php if it starts with the index.php in url.

Visiting http://santasbingo.norwayeast.azurecontainer.io/index.php/abc still worked so. Lets add config.php and see if we trigger that if statement.

http://santasbingo.norwayeast.azurecontainer.io/index.php/config.php/

```text
Ha ha ha! You didn't say the magic word!! And this is not a Unix System... oh wait...
```

So to bypass this we just look at the regexp:

```php
if (preg_match('/config\.php\/*$/i', $_SERVER['PHP_SELF'])) {
```

```Breakdown
/config\.php\/*$/i

- config matches the characters config literally (case insensitive)
- \. matches the character . with index 4610 (2E16 or 568) literally (case insensitive)
- php matches the characters php literally (case insensitive)
- \/ matches the character / with index 4710 (2F16 or 578) literally (case insensitive)
- * matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
- $ asserts position at the end of the string, or before the line terminator right at the end of the string (if any)

Global pattern flags 
- i modifier: insensitive. Case insensitive match (ignores case of [a-zA-Z])
```

Based on this for it to match it needs to be exactly `config.php/` and end with a /. So adding anything else e.g. `config.php/test/` will fail this check and load the regular index page.

Now looking at the ?test function. The basename function keeps us within the directory, no way to bypass that as far as I know. The PHP_SELF is basically just the path in your domain. so `url.com/this/is/what/is/in/php_self/`.

So loading `index.php/config.php/?test` without that check would make the highlight function load config.php as that is the file basename of php_self would get.

So to bypass this we can send something to avoid that regexp but still make a valid config.php resolvement for the software. I tried with a space:

```
http://santasbingo.norwayeast.azurecontainer.io/index.php/config.php%20/?test


Warning: highlight_file(config.php ): failed to open stream: No such file or directory in /var/www/html/index.php on line 9

Warning: highlight_file(): Failed opening 'config.php ' for highlighting in /var/www/html/index.php on line 9
```

So I guess I have to send something that `basename` would not use but the regexp would see.

```
basename() is locale aware, so for it to see the correct basename with multibyte character paths, the matching locale must be set using the setlocale() function. If path contains characters which are invalid for the current locale, the behavior of basename() is undefined.
```

So I went to this [HTML URL-encoding Reference](https://www.eso.org/~ndelmott/url_encode.html) and tried some of the blank ones. No-one worked. Then from the 90-> range it seems like most of them actually works. So guessing that is multibyte characters. So adding /%90 at the end gives us a eureka moment! 

```http://santasbingo.norwayeast.azurecontainer.io/index.php/config.php/%90?test```

```php
<?php
define('FLAG', '${M@n_5@n7@_5ur3_Luvz_P4P_Y3t_I_4@73_I7!!!}');
?>
<!--- Creds to st98 for the original chall -->
```
