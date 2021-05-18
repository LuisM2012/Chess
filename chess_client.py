import socket
from threading import Thread


class NoPlayerActive(Exception):
    pass


"""
class: Connection - used for connecting user to server and join online games
"""
class Connection:
    def __init__(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost" #change to hosting server
        self.port = 2020        #change to hosting port
        self.addr = (self.server, self.port)
        self.resp = []
        self.connect()

    def connect(self):
        """Connect user to server."""
        try:
            self.client.connect(self.addr)
        except ConnectionRefusedError:
            print("ConectionRefusedERROR: Connection not Available at this Time.")
            raise

    def disconnect(self):
        """Disconnect user to server."""
        self.client.close()

    def send(self, msg:str):
        """Send message to server."""
        try:
            self.client.send(msg.encode())
        except socket.error as e:
            print(e)

    def listen(self):
        """Listen for server message."""
        print("listening")
        Thread(target=self.sub_listen).start()
        
    def sub_listen(self):
        self.resp.clear()
        msg = self.client.recv(1024).decode()
        self.resp.insert(0, msg)

        print(f"msg: {msg}")
        if msg=="TIMEOUT":
            print("NoPlayerActive: No players active at this time.")
            raise NoPlayerActive("No players active at this time.")

    def init_player(self):
        msg = self.client.recv(1024).decode()
        print(msg)
        return msg
