import socket
import time


"""
class: Connection - used for connecting user to server and join online games
"""
class Connection:
    def __init__(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost" #change to hosting server
        self.port = 2000        #change to hosting port
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        """Connect user to server."""
        self.client.connect(self.addr)

    def disconnect(self):
        """Disconnect user to server."""
        self.client.close()

    def reconnect(self):
        """Reconnect user to server when internet fails."""
        for _ in range(3):
            try:
                self.connect()
                break
            except:
                print("[RECONNECTION] try checking your internet")
                time.sleep(5)
        print("[CONNECTION ERROR] could not connect to internet")

    def send(self, msg:str):
        """Send message to server."""
        try:
            self.client.send(msg.encode())
        except socket.error as e:
            print(e)

    def listen(self):
        """Listen for server message."""
        msg = self.client.recv()
        return msg

