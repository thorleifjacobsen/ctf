const http = require('http');
const { Buffer } = require('buffer');

const server = http.createServer((req, res) => {
    const hexData = req.url.substring(1);
    const ciphertext = Buffer.from(hexData, 'hex');
    const options = {
        hostname: 'motherload.td.org.uit.no',
        port: 8004,
        path: '',
        method: 'POST'
    };

    const request = http.request(options, response => {
        let data = '';
        response.on('data', chunk => {
            data += chunk;
        });
        response.on('end', () => {
            if (response.statusCode === 200) {
                console.log(hexData + " 200")
                res.writeHead(200, { 'Content-Type': 'text/plain' });
                res.end();
            } else {
                res.writeHead(400);
                console.log(hexData + " 400")
                res.end();
            }
        });
    });

    request.on('error', error => {
        res.writeHead(400);
        res.end();
    });

    request.write(ciphertext);
    request.end();
});

server.listen(8000, () => {
    console.log('Server running at http://localhost:8000/');
});
