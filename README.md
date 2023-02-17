# TCP socket connection

## This project demonstrates a TCP connection between sockets of 2 processes (client and server). 
The client sends a message, then the server receives and manipulates the data. My motivation behind this project is to learn more about computer networking and how processes communicate with each other. I built this because I felt like it would be fun and interesting. I love writing code and learning new things. The main takeaways I have from this assignment are the handshaking process of TCP, the unreliability of UDP, and the overall life cycle of a socket.

### TO DEMO: 
First run socket-server.py. Once you see "Server is ready to receive", then run socket-client.py (while server remains running for the entire time). Enter an integer from 0-100. This integer is then sent to the server, where it randomly generates an integer, and adds it's own integer to the one you sepcified.

## Screenshots:
![image info](./assets/images/ss1.png)
![image info](./assets/images/ss1.png)
![image info](./assets/images/ss1.png)


### Author: David Williford