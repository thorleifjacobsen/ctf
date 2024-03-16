const express = require('express')
const app = express()
const port = 1337

app.get('/', (req, res) => {
    res.sendFile(__dirname + "/index.html");
})

app.get('/chat', (req, res) => {

    console.log(req.socket.remoteAddress);

    if (req.socket.remoteAddress != '127.0.0.1') //make sure flag is just for locally
        do {
            req.query.message = req.query.message.replace(/(flag)/i, "");
        } while (req.query.message.indexOf("flag") > -1)

    if (/hi|hello|hey/i.test(req.query.message))
        return res.json({ message: "Hi, nice to meet you! My name is Chad Jeepeetee!" });

    if (/what|who|were|when|why/i.test(req.query.message))
        return res.json({ message: "I don't know!" });

    if (/flag/i.test(req.query.message))
        return res.json({ message: "The flag is " + (process.env.flag ?? "1753c{fake_flag_for_testing}") });

    return res.json({ message: "Maybe..." });
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})