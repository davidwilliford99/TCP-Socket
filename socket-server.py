"""
Server for socket programming assignment
"""

import random
from socket import *

server_ip = "127.0.0.1"
server_port = 8000
server_name = "Server of David Williford"

# create a sever socket 
server_socket = socket(AF_INET, SOCK_STREAM)

# binding ip and port to server socket 
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print("Server is ready to receive!!")


while True:

    # allowing and capturing client msg and address
    client_message, client_address = server_socket.accept()
    sentence = client_message.recv(1024).decode()

    # extracting information from client message 
    client_split = sentence.split(",")
    client_name = client_split[1]
    client_number = client_split[0]

    # picking a random number 1-100
    server_number = random.randint(1,100)
    number_sum = int(client_number) + server_number

    # print output for debuggin purposes
    print("\n")
    print(client_name)
    print(server_name)
    print("Number from server: " + str(server_number))
    print("Number from client: " + str(client_number))
    print("Sum of both numbers: " + str(number_sum))
    print("\n")

    
    server_message = str(server_number) + " " + client_name

    # send server message back to client 
    server_socket.sendto(server_message.encode(), client_address)
    server_socket.close()