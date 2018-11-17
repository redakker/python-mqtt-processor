#!/usr/bin/python

# In this script defined a function which process the messages and contains the business logic

# msg should be an mqtt message object
import json
import logging
from foscam import FoscamCamera
import sys, os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def process (msg, client):

    #// msg.topic - topic of the MQTT meaasge
    #// msg.payload - body of the MQTT message

    mycam = FoscamCamera('192.168.1.40', 88, 'redman', 'NorAkhu8')

    try:
	jsonMsg = json.loads(msg.payload);
    except ValueError, e:
	jsonMsg = '{}';
	#print "invalid";
	pass # invalid json
    else:
	#print "valid";
	pass # valid json);

    ############################################################################
    # Use jsonMsg object (converted from json message) for deatiled conditions #
    ############################################################################
    
    #if msg.topic == "/home/users/away":
	#client.publish("/home/device/bedroom/sonoff", "0", 0, True);
	#logging.debug("Message to bedroom sonoff sent (Off)");

    #if msg.topic == "/home/users/home":
	#client.publish("/home/device/bedroom/sonoff", "1", 0, True);
	#logging.debug("Message to bedroom sonoff sent (Off)");

    #############  Camera commands using foscam-python-lib
    #https://github.com/quatanium/foscam-python-lib

    if msg.topic == "/home/camera/Veszprem/irled":
	if msg.payload == "1":
	    mycam.open_infra_led()
	    logging.debug("Camera Veszprem IRLed On");
	if msg.payload == "0":
	    mycam.close_infra_led()
	    logging.debug("Camera Veszprem IRLed Off");

    if msg.topic == "/home/speak/sentence":
	if msg.payload:
	    os.system("/srv/xiaomi_speak/speak.sh -l hu-HU -n -t \"" + msg.payload + "\"");
	    logging.debug("Speak" + msg.payload);
