import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 65433)

user = input("Enter username: ")
pw = input("Enter password: ")
print(f"sending {user}, {pw}")
client_socket.sendto(f"{user},{pw}".encode(), server_address)

response,_ = client_socket.recvfrom(2048)
print(response.decode())

if "successful" not in response.decode():
    print("Failed login attempt. Goodbye.")
    exit()

while True:
    message = input("Client: ")
    #send message to server
    client_socket.sendto(message.encode(), server_address)

    reply,_ = client_socket.recvfrom(2048)
    
client_socket.close()