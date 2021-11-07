import socket
import pycustomdigits
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 7543))

sock.listen()


def client(sock, addr):
    while True:
        try:
            h = sock.recv(1024)
        except ConnectionError:
            print(f'USER: [{addr}]: DISCONNECTED')
        if h:
            print(F'NEW MSG FROM [{addr}] : {h.decode()}')

while True:
    socket, addr = sock.accept()
    print('NEW CONNECTION: ', addr)
    th = threading.Thread(target=client, args=(socket, addr))
    th.start()