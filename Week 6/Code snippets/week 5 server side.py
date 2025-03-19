import threading

import socket
# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))
server_socket.listen(1) # Allow 1 pending connection
print("TCP Server is listening...")

clients = []

def broadcast(message,sender_socket): #broadcast message to every client
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)    

def client_handle(client_socket,client_address): #handle each client
    print(f"Connected to {client_address}")
    clients.append(client_socket)

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"{client_address}: {data.decode()}")
            broadcast(data,client_socket)
        except:
            break
    print(f"{client_address} disconnected")
    clients.remove(client_socket)
    client_socket.close()    

with open("received_file.txt", "wb") as f:
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
        print("File received!")
        client_socket.close()    
while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=client_handle, args=(client_socket, client_address))
    thread.start()