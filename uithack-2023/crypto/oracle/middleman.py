from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from binascii import unhexlify
import requests

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        try:
            url_value = self.path[1:].encode()
            ciphertext = bytearray(unhexlify(url_value))

            response = requests.post("http://motherload.td.org.uit.no:8004", data=ciphertext)

            if response.status_code == 200:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'')
            else:
                self.send_error(400, "")
            return
        except: 
            self.send_error(400, "")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

run()