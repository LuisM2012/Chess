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

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

def start():
    answer = input("Would yoou like to connect to server? (yes/no)")
    if answer.lower() != "yes":
        return

    connection = connect()
    
    while True:
        msg = input("Message:")

        if msg == "Q":
            break
        
        send(connection, msg)
        
    send(connection, "!DISCONNECT")
    time.sleep(1)
    print("Disconnected")

start()

client = connect()
send(client, "TEst")
time.sleep(1)
send(client, "!DISCONNECT")

