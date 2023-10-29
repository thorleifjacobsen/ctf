# Markup (beginner)

The flag is hidden in the website's code!

Author: martcl

http://www.wackattackntnumarkup.s3-website.eu-north-1.amazonaws.com/

# Writeup

Inspecting the HTML shows the flag:

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hidden</title>
</head>
<body>
    <h1>Vi har gjemt flagget på denne nettsiden!</h1>
    <!-- wack{wow_a_hidden_flag!}   -->
</body>
</html>
```

# Flag

```
wack{wow_a_hidden_flag!}
```