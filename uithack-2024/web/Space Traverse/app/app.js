const express = require("express");
const fs = require("fs");
const path = require("path");
const app = express();
const port = 8001;

app.use(express.static("static"));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

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

app.listen(port, () => {
  console.log(`Listening at port: ${port}`);
});
