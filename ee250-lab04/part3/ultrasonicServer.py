import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')

#use UDP
import socket

def Process1():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '10.0.2.15'
    port = 9000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Process 1 Server Started")
    while True:
        print("Receiving Data")
        data, addr = s.recvfrom(1024)
        print("received Data")
        #data = data.decode('utf-8')
        print("Message From: " + str(addr))
        print("From connected user: " + str(data))
        #data = data.upper()

    c.close()

if __name__ == '__main__':
    Process1()