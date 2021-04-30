import socket, os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8888))
sock.listen(5)
os.environ.get('PORT')
while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print('Message', result.decode('utf-8'))
