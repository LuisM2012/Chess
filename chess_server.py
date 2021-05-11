from socket import *
from _thread import *
# import pickle #coulds be used for sending board

host = ""     #change to hosting server
port   = 2020   #change to hosting port

server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))

server.listen()
print("[RUNNING] Server is ready...")

connections = list()
games = {}


def communication(client, address, player):
    while True:
        if client in games.keys():
            client.send(f'Player: {player}'.encode())
            break

    while True:
        msg = client.recv(1024).decode()
        if not msg or msg == "QUIT":
            break

        games[client].send(msg.encode())

    del games[client]
    connections.remove(client)

    print(f"[DISCONNECTED] {address} has left")
    client.close()


def match(client):
    if len(connections)%2:
        player = 2
    else:
        player = 1

    connections.append(client)
    if player == 1:
        while client not in games.keys():
            for i in connections:
                if i not in games.keys() and i !=client:
                    games[client] = i
                    games[i] = client

        print("[NEW GAME] ...")
    else:
        connections.append(client)
    
    return player



while True:

    client, addr = server.accept()
    print(f"[CONNECTED] {addr} has joined")

    player = match(client)
    
    start_new_thread(communication, (client, addr, player))

server.close()
print("[STOPPED] Server ended...")