#!/usr/bin/python -B

# -B avoid to crate pyc cache file

# This script receives all mqtt messages and call another python script 
# which process that message.

# Git project which was used
# https://pypi.python.org/pypi/paho-mqtt/1.1

import paho.mqtt.client as mqtt
import logging
import mqtt_processor as processor
from config import Config

################
# CONFUGRATION #
################

config = Config();
logging.basicConfig(filename=config.logfile,level=logging.DEBUG,format='%(asctime)s %(message)s');

################
################
################


##########################
# MAIN PROCESSING METHOD #
##########################

def process_message (msg):
    logging.debug("Processing topic: " + msg.topic + " - data: " + msg.payload  );
    processor.process(msg);

#################################
# END OF MAIN PROCESSING METHOD #
#################################

###################
# OTHER FUNCTIONS #
###################




###################
###################
###################


##############################################################################
# THIS SECTION CONNECT TO THE BROKER, NOTHING TO DO WITH THAT IN NORMAL CASE #
##############################################################################

# Listneing to all topics and send it to a process method.
# The method defined above

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    logging.debug("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    process_message(msg);

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#Set userid and password
client.username_pw_set(config.user, config.password)

#Connect
client.connect(config.broker, config.port, config.keepalive)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

##############################################################################
##############################################################################
##############################################################################

