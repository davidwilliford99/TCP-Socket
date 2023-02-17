"""
Client for socket programming assignment
"""

from socket import *

server_ip = "127.0.0.1"
server_port = 8000

# creating the client socket 
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# gathering message to send to server 
client_input = input("Type an integer from 1-100: ")
client_name = "Client of David Williford"
client_message = str(client_input) + "," + client_name

# sends client messages (encoded) to the server's IP and port
client_socket.sendto(client_message.encode(), (server_ip, server_port))

# receive message from server 
modified_message = client_socket.recv(2048)

# close the socket
client_socket.close()
