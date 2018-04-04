import paho.mqtt.client as mqtt
import time

# MQTT variables
broker_hostname = "eclipse.usc.edu"
broker_port = 11000
ultrasonic_ranger1_topic = "ultrasonic_ranger1"
ultrasonic_ranger2_topic = "ultrasonic_ranger2"

# Lists holding the ultrasonic ranger sensor distance readings. Change the 
# value of MAX_LIST_LENGTH depending on how many distance samples you would 
# like to keep at any point in time.
MAX_LIST_LENGTH = 10
ranger1_dist = [0,0,0,0,0,0,0,0,0,0]
ranger2_dist = [0,0,0,0,0,0,0,0,0,0]

def ranger1_callback(client, userdata, msg):
    global ranger1_dist
    ranger1_dist.append(int(msg.payload))
    #truncate list to only have the last MAX_LIST_LENGTH values
    ranger1_dist = ranger1_dist[-MAX_LIST_LENGTH:]

def ranger2_callback(client, userdata, msg):
    global ranger2_dist
    ranger2_dist.append(int(msg.payload))
    #truncate list to only have the last MAX_LIST_LENGTH values
    ranger2_dist = ranger2_dist[-MAX_LIST_LENGTH:]

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(ultrasonic_ranger1_topic)
    client.message_callback_add(ultrasonic_ranger1_topic, ranger1_callback)
    client.subscribe(ultrasonic_ranger2_topic)
    client.message_callback_add(ultrasonic_ranger2_topic, ranger2_callback)

# The callback for when a PUBLISH message is received from the server.
# This should not be called.
def on_message(client, userdata, msg): 
    print(msg.topic + " " + str(msg.payload))



if __name__ == '__main__':
    # Connect to broker and start loop    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_hostname, broker_port, 60)
    client.loop_start()


    avg1_i = 185
    avg2_i = 515

    while True:
        """ You have two lists, ranger1_dist and ranger2_dist, which hold a window
        of the past MAX_LIST_LENGTH samples published by ultrasonic ranger 1
        and 2, respectively. The signals are published roughly at intervals of
        200ms, or 5 samples/second (5 Hz). The values published are the 
        distances in centimeters to the closest object. Expect values between 
        0 and 512. However, these rangers do not detect people well beyond 
        ~125cm. """
        
        # TODO: detect movement and/or position
        

        #initialize buffers
        sam_buf1 = [0,0,0,0,0,0,0,0,0,0]
        avg_dist1 = [0,0,0,0,0,0,0,0,0,0]
        sam_buf2 = [0,0,0,0,0,0,0,0,0,0]
        avg_dist2 = [0,0,0,0,0,0,0,0,0,0]
        l1 = MAX_LIST_LENGTH
        l = MAX_LIST_LENGTH



        for k in range(0, l1):
            sam_buf1[l - 1] = ranger1_dist[k]
            sam_buf2[l - 1] = ranger2_dist[k]
            s1 = 0
            s2 = 0


            for i in range(0, l):
                #print(sam_buf[i])
                s1 = s1 + sam_buf1[i]
                s2 = s2 + sam_buf2[i]
            avg_dist1[l - 1] = s1/10.0
            avg_dist2[l - 1] = s2/10.0


            if k != l1 - 1:
                for j in range(0, l - 1): #move elements backwards
                    avg_dist1[j] = avg_dist1[j + 1]
                    sam_buf1[j] = sam_buf1[j + 1]
                    avg_dist2[j] = avg_dist2[j + 1]
                    sam_buf2[j] = sam_buf2[j + 1]

        sum1 = 0
        sum2 = 0

        for q in range(0, MAX_LIST_LENGTH):
            sum1 = sum1 + avg_dist1[q]
            sum2 = sum2 + avg_dist2[q]




        avg1 = sum1 / (MAX_LIST_LENGTH + 1)
        avg2 = sum2 / (MAX_LIST_LENGTH + 1)




        slope1 = (avg1 - avg1_i) / 2
        slope2 = (avg2 - avg2_i) / 2


        avg1_i = avg1
        avg2_i = avg2


        s = ""
        #determine present or not
        if avg1 > 120 and avg2 > 400:
            s = "out of range :^( "

        #present: at the left -> in the range of sensor2
        elif avg2 < 400:
            #if it's moving left
            if slope2 < -3:
                s = "moving left"
            #if it's moving right
            if slope2 > 3:
                s = "moving right"
            else:
                #still
                if avg2 < 52:
                    #left
                    s = "still: left"
                if 69 < avg2 < 72:
                    s = "still: middle"


        #present: at the right -> in the range of sensor1
        elif avg1 < 120:
            #if it's moving left
            if slope1 < 0:
                s = "moving right"
            #if it's moving right
            if slope1 > 3:
                s = "moving left"
            else:
                #still
                if avg1 < 50:
                    #right
                    s = "still: right"
                if 69 < avg1 < 72:
                    s = "still: middle"







        print("ranger1: " + "{0:.2f}".format(avg1) + ", ranger2: " + "{0:.2f}".format(avg2) + s + "    slope1 = " + "{0:.2f}".format(slope1) + "    slope2 = " + "{0:.2f}".format(slope2))
        

        
        time.sleep(0.2)