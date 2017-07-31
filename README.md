Mqtt processor without business logic.

Special thanks for the basic libary implementation
https://pypi.python.org/pypi/paho-mqtt/1.1

mqtt_worker.py - does the connection (connection setup inside this file)

mqtt_processor.py - process the messages, put business logic here

config.py - contains the config data for the connection, log etc.

mqtt_worker.sh - init.d script to create daemon from this python script

mqtt_daemon.service - basic systemd script to start the python script as service
