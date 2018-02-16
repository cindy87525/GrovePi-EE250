import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')



# use TCP
import socket

def Process1():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 


    host = '127.0.0.1'
    port = 5000

    s = socket.socket() #by default, the socket constructor creates an TCP/IPv4 socket
    s.connect((host,port))

    while True:
        #tuples are immutable so we need to overwrite the last tuple
        server = (server_addr, int(dst_port))


        # for UDP, sendto() and recvfrom() are used instead
        data = s.recv(1024).decode('utf-8') 
        print(data)
    s.close()
    


if __name__ == '__main__':
    Process1()