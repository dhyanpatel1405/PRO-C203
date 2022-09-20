# ------- Bolierplate Code Start -----


import socket
from  threading import Thread
IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None
clients = {}

def handleclients():
    pass

def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()                                    
        #print(client, addr)
        client_name = client.recv(4096).decode().lower()
        clients[client_name]={
            'Client':client,
            'address':addr,
            'connectedwith':'',
            'filename':'',
            'filesize':'',
            'filetype':''
        }     

        print('connection estlablished with {addr}')
        thread = Thread(target = handleclients)
        thread.start()                                                                  

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    # Getting global values
    global PORT
    global IP_ADDRESS
    global SERVER


    SERVER  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup_thread = Thread(target=setup)           #receiving multiple messages
setup_thread.start()

# ------ Bolierplate Code End -----------
