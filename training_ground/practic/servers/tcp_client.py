import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 5000))
sock.send(b'Test message')
sock.close()
