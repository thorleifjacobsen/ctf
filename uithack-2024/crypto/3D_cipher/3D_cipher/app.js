const express = require("express");
const app = express();
const port = 7000;

app.use(express.static("static"));

app.get("/", (req, res) => {
  res.sendFile("index.html");
});

app.listen(port, () => {
  console.log(`Listening at port: ${port}`);
});
