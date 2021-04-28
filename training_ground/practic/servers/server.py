import socket
from socketserver import ThreadingTCPServer
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ThreadingTCPServer((socket.gethostname(), 5000), EchoHandler)
# Bind the socket to the port
# server_address = (socket.gethostname(), 4000)
print('starting up on {} port {}'.format(*server_address))
# sock.bind(server_address)
server.serve_forever() 
# Listen for incoming connections
# sock.listen(5)
try:
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(4096)
                print('received {!r}'.format(data))
                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print('no data from', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()
finally:
    sock.close()