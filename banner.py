import socket

host = input("give the host :")
port = input("give the port number :")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host, int(port)))
sock.send(b"master in hack")
data  = sock.recv(1024)
print("banner is :",str(data))