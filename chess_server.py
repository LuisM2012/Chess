from socket import *
from _thread import start_new_thread
import time


host = ""     #change to hosting server
port   = 2020   #change to hosting port

server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))

server.listen()
print("[RUNNING] Server is ready...")

connections = list()
games = {}


def communication(client, address, player):
    start = time.time()
    while True:
        if client in games.keys():
            client.send(f'{player}'.encode())
            break
        if (time.time()-start)>20:
            if client in games.keys():
                continue
            client.send("TIMEOUT".encode())
            cut_connect(client, address)
            return
    try:
        while True:
            msg = client.recv(1024).decode()

            if not msg or msg == "QUIT":
                try:
                    games[client].send("QUIT".encode())
                    break
                except:
                    break

            try:
                games[client].send(msg.encode())
            except:
                break
    except Exception as er:
        print(f"{type(er)}: {er}")

    if client in games: del games[client]
    cut_connect(client, address)

def cut_connect(client, address):

    connections.remove(client)
    print(f"[DISCONNECTED] {address} has left")
    client.close()



def match(client, address):
    if len(connections)%2:
        player = 1
    else:
        player = 2

    connections.append(client)
    if player == 1:
        while client not in games.keys():
            for i in connections:
                if i not in games.keys() and i !=client:
                    games[client] = i
                    games[i] = client
        print("[NEW GAME] ...")

    communication(client, address, player)



try:
    while True:

        client, addr = server.accept()
        print(f"[CONNECTED] {addr} has joined")

        
        start_new_thread(match, (client, addr))
        
except Exception as err:
    print(f"{type(err)[8:-2]}: {err}")
    server.close()
    print("[STOPPED] Server ended...")
