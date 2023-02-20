from socketserver import StreamRequestHandler, TCPServer
import json
import datetime


IP = '172.27.63.138' #Server IP. This needs to be the ZeroTier IP of the PC that runs the script
PORT = 5000

logs = open("MyFile.txt", "w")

def print_data(data: bytes) -> None:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    data = json.loads(data)
    print(data)
    logs.write(current_time + ": ")
    logs.write(str(data))
    logs.write("\n")

# This class handles receiving JSON packets from the transmitter and calls print_data
class DumpHandler(StreamRequestHandler):
    def handle(self) -> None:
        """receive json packets from client"""
        print('connection from {}:{}'.format(*self.client_address))
        try:
            while True:
                data = self.rfile.readline()
                if not data:
                    break
                print_data(data)
        finally:
            print('disconnected from {}:{}'.format(*self.client_address))
            logs.close()

def main() -> None:
    server_address = (IP, PORT)
    print('starting up on {}:{}'.format(*server_address))
    with TCPServer(server_address, DumpHandler) as server:
        print('waiting for a connection')
        server.serve_forever()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
