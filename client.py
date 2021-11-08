import socket
import pycustomdigits
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 7543))

x = 1
toaddpi = 0
while 1:
    toaddpi = pycustomdigits.supersum(pycustomdigits.superdivision('1', str(x), 50), '-' + pycustomdigits.superdivision('1', str(x+2), 50))
    sock.send(str(toaddpi).encode())
    x+=8
    sock.recv(24)
    

