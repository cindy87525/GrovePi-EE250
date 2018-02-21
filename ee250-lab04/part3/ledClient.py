import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`


sys.path.append('../../Software/Python/')

import socket

def Main():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 


    host = '192.168.1.209'
    port = 5001
    #server_addr = '10.0.2.15'

    s = socket.socket() #by default, the socket constructor creates an TCP/IPv4 socket
    s.connect((host,port))
    message = input("LED ON or OFF?")
    while True:
        #server = (server_addr, 5002)
        s.send(message.encode('utf-8')) 
        #1024 is the receive buffer size. It's enough for us, and it's a nice number. 
        message = input("LED ON or OFF?")

        
    s.close()
    


if __name__ == '__main__':
    Main()