import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ('localhost', 9090)

print('Server running on: ', address)

sock.bind(address)
sock.listen(1)
client, ad = sock.accept()
while True:
    data = client.recv(1024)
    if data:
        print('Received from client ', data)
        client.send(data)
client.close()