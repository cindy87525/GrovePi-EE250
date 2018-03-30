import paho.mqtt.client as mqtt
import time

# MQTT variables
broker_hostname = "eclipse.usc.edu"
broker_port = 11000
ultrasonic_ranger1_topic = "ultrasonic_ranger1"
ultrasonic_ranger2_topic = "ultrasonic_ranger2"

sam_buf = [0,0,0,0,0,0,0,0,0,0]
avg_dist = [0,0,0,0,0,0,0,0,0,0]
a = [64, 73, 77, 70, 75]
l1 = 5
l = 10
for k in range(0, l1):
	sam_buf[l - 1] = a[k]
	s = 0


	for i in range(0, l):
		#print(sam_buf[i])
		s = s + sam_buf[i]
	avg_dist[l - 1] = s/10.0


	if k != l1 - 1:
		for j in range(0, l - 1): #move elements backwards
			avg_dist[j] = avg_dist[j + 1]
			sam_buf[j] = sam_buf[j + 1]
			


print("sample")
for o in range(0,10):
	print(sam_buf[o])
print("avg_dist")
for o in range(0,10):
	print(avg_dist[o])