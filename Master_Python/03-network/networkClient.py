import socket

host = 'localhost'
# AF_INET:
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (host, 5555)
mysock.connect(addr)


try:
    msg = b'hi, this is a test\n'
    mysock.sendall(msg)
except socket.errno:
    print("Socket error")
finally:
    mysock.close()