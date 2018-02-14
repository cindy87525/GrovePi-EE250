import sys
import grovepi
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
    ultrasonic_ranger = 4
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Process 1 Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        #data = data.decode('utf-8')
        print("Message From: " + str(addr))
        print("From connected user: " + data)
        #data = data.upper()
        print("Sending: " + data)
        s.sendto(grovepi.ultrasonicRead(ultrasonic_ranger), addr)#s.sendto(data.encode('utf-8'), addr)

    c.close()

if __name__ == '__main__':
    Process1()