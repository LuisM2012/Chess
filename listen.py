import threading
import socket
import time
PORT = 2021
PORT2 = 3021

SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def start():
    connection = connect()
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        print(msg)

start()