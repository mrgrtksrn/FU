import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 9090)
print('Connecting to port ', address)

try:
    sock.connect(address)
    msg = input('Your message: ')
    while msg != 'exit':
        sock.sendall(msg.encode('utf-8'))
        data = sock.recv(1048)
        print('Received from server ', data.decode('utf-8'))
        msg = input('Your message: ')
except socket.gaierror as e:
    print('Socket error: ', str(e))
except Exception as e:
    print(e)
finally:
    sock.close()
