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
        time.sleep(0.1)

    else:
        grovepi.digitalWrite(led,0)     #if flag is an odd number, turn LED off
        print ("LED_OFF!")
        flag = flag - 1 #flag -- to make flag = 0
        time.sleep(0.1)


def lcd_callback(client, userdata, message):
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload)))

    data = str(message.payload, "utf-8")
    setText(data)
    print (data)



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("anrg-pi14/led")
    client.subscribe("anrg-pi14/lcd")
    client.subscribe("anrg-pi14/humidity")
    client.subscribe("anrg-pi14/temperature")
    client.message_callback_add("anrg-pi14/lcd", lcd_callback)
    client.message_callback_add("anrg-pi14/led", led_callback)



if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    #use the port address for usc eclipse
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()
    setRGB(0,255,0)


            



    while True:

        try:
            # This example uses the blue colored sensor. 
            # The first parameter is the port, the second parameter is the type of sensor.
            [temp,humidity] = grovepi.dht(sensor,blue)  
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                T = str(round(temp, 2))
                H = str(round(humidity, 2))
                client.publish("anrg-pi14/temperature", T + " C")
                client.publish("anrg-pi14/humidity", H + "%")
                time.sleep(0.1)

        except IOError:
            print ("Error")
            

