import socket
import argparse
import datetime

MAX_BYTES = 65536

class Server:
    def __init__(self, interface, port):
        self.interface = interface
        self.port = port

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.interface, self.port))
        print(f'Server bind with {sock.getsockname()}')

        while True:
            data, address = sock.recvfrom(MAX_BYTES)

            text = data.decode('ascii')
            print(f"The client {address} says: {text}")
            server_text = f"Hey! I'm a server, your data was {len(data)} bytes long"
            server_data = server_text.encode('ascii')

            sock.sendto(server_data, address)



class Client:
    def __init__ (self, hostname, port):
        self.hostname = hostname
        self.port = port

    def interval(self):
        now = datetime.datetime.now().time()
        if datetime.time(12,0,0) <= now <= datetime.time(16,59,59):  #first interval
            return 1
        elif datetime.time(17,0,0) <= now <= datetime.time(23,59,59):  #second interval
            return 2
        elif datetime.time(0,0,0) <= now <= datetime.time(11,59,59):  #third interval
            return 3

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((self.hostname, self.port))

        text = f'This is the message from the client, we sent it at {datetime.datetime.now()}'
        data = text.encode('ascii')

        delay = 0.1
        while True:
            sock.send(data)
            sock.settimeout(delay)

            try:
                data = sock.recv(MAX_BYTES)
            except socket.timeout:
                if self.interval() == 1:
                    delay *= 2
                    if delay > 2:
                        raise RuntimeError('Something is wrong! But why?!')
                elif self.interval() == 2:
                    delay *= 3
                    if delay > 4:
                        raise RuntimeError('Something is wrong! But why?!')
                elif self.interval() == 3:
                    delay *= 2
                    if delay > 1:
                        raise RuntimeError('Something is wrong! But why?!')
            else:
                break

        print(f"Here is the message from the server: {data.decode('ascii')}")


def main():
    choices = {'client','server'}
    parser = argparse.ArgumentParser()
    parser.add_argument('role', choices = choices)
    parser.add_argument('-p', metavar='PORT', type=int, default=1025)
    parser.add_argument('host')
    args = parser.parse_args()

    if args.role == 'client':
        client = Client(args.host,args.p)
        client.connect()
    elif args.role == 'server':
        server = Server(args.host,args.p)
        server.connect()

if __name__ == "__main__":
    main()
