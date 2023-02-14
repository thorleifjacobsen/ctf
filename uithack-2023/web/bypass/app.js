const express = require("express");
const bodyParser = require("body-parser");
const utils = require("./utils");
const app = express();

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

const port = 8007;
const adminCode = utils.generateCode();
const user = {"profilePicture": false};

app.get("/", (req, res) => {
  res.render("index");
});

app.post("/flag", (req, res) => {
  if(req.body.admin && req.body.code !== adminCode){
    res.status(401).render("unauthorized");
    return;
  }
  let userAuth = Object.assign(user, req.body);
  if(userAuth.admin || utils.verifyUser(req.body.username, req.body.password)){
    res.render("flag");
  } else {
    res.status(401).render("unauthorized");
  }
})

app.listen(port, () => {
  console.log(`Listening at port: ${port}`);
});
