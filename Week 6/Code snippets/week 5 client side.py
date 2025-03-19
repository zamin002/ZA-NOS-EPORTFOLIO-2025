import datetime
import threading

#EXAMPLE CODE
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))


def get_messages(): #get the messages from the server
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(message.decode())
        except:
            print("Connection has been closed")    
            break

thread = threading.Thread(target=get_messages)
thread.start()        

start = datetime.datetime.now()

message = input("Enter message: ")
client_socket.sendall(message.encode())

response = client_socket.recv(1024)
print(f"Server response: {response.decode()}")

with open("file_to_send.txt", "rb") as f:
    client_socket.sendfile(f)

end = datetime.datetime.now()

time_total = end - start
print(f"time taken for TCP transmission: {time_total} seconds")

if message.lower() == "exit":
    client_socket.close()