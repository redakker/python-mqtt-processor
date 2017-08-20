#!/usr/bin/python

# In this script defined a function which process the messages and contains the business logic

# msg should be an mqtt message object
def process (msg, client):    
    if msg.topic == "/home/users/away":
	client.publish("/home/device/bedroom/sonoff", "0", 0, True);
	
    if msg.topic == "/home/users/home":
	client.publish("/home/device/bedroom/sonoff", "1", 0, True);