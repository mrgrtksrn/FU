import socket
import time

# host = socket.gethostbyname(socket.gethostname())
host ="127.0.0.1"
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
print("Server started")

while not quit:
    try:
        data, address = s.recvfrom(1024)

        if address not in clients:
            clients.append(address)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + address[0] + "]=[" + str(address[1]) + "]=[" + itsatime + "]/", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if address != client:
                s.sendto(data, client)
    except:
        print("\nServer Stopped")
        print(clients)
        quit = True

s.close()