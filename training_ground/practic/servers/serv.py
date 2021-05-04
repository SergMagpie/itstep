from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('waiting for a connection')
        print('connection from:', self.client_address)
        while True:
            msg = self.request.recv(8192)
            print('received {!r}'.format(msg))
            if not msg:
                break
            self.request.send(msg)
            print('sending data back to the client')


if __name__ == '__main__':
    server = ThreadingTCPServer(('127.0.0.1', 8888), EchoHandler)
    server.serve_forever()
