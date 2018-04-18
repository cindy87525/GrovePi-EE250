import sys
sys.path.append('../../Software/Python/')
import paho.mqtt.client as mqtt
import time
import grovepi
import math
from grove_rgb_lcd import *

button = 2
led = 3
sensor = 4
blue = 0
ultrasonic_ranger = 4
flag = 1
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(button,"INPUT")

def led_callback(client, userdata, message):
    global led
    global flag
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload)))

    data = str(message.payload, "utf-8")

    

    if flag % 2 == 0: #if flag is an even number, turn LED on
        grovepi.digitalWrite(led,1)
        print ("LED_ON!")
        flag = flag + 1 #flag ++ to make flag != 0
        time.sleep(1)

    else:
        grovepi.digitalWrite(led,0)     #if flag is an odd number, turn LED off
        print ("LED_OFF!")
        flag = flag - 1 #flag -- to make flag = 0
        time.sleep(1)


def lcd_callback(client, userdata, message):
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload)))

    data = str(message.payload, "utf-8")
    #if data == "w":
    setText(data)
    print (data)
    #if data == "a":
    #    setText("a")
    #    print ("a")
    #if data == "s":
    #    setText("s")
    #    print ("s")
    #if data == "d":
    #    setText("d")
    #    print ("d")



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("anrg-pi14/led")
    client.subscribe("anrg-pi14/lcd")
    client.subscribe("anrg-pi14/humidity")
    client.subscribe("anrg-pi14/temperature")
    client.message_callback_add("anrg-pi14/lcd", lcd_callback)
    client.message_callback_add("anrg-pi14/led", led_callback)



#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()
    setRGB(0,255,0)


            



    while True:

        #flag = flag + 1
        #print(grovepi.ultrasonicRead(ultrasonic_ranger))
        #if grovepi.digitalRead(button) == 1:     # Send HIGH to switch on LED
        #    print ("Button_pressed!")
        #    client.publish("anrg-pi14/button", "Button_pressed!")
        #time.sleep(1)
        try:
            # This example uses the blue colored sensor. 
            # The first parameter is the port, the second parameter is the type of sensor.
            [temp,humidity] = grovepi.dht(sensor,blue)  
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
                time.sleep(0.5)

        except IOError:
            print ("Error")
            

