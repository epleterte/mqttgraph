#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

import sys, os, socket, json, time

#DEBUG = True
DEBUG = True

config = { 'mqtt_server': 'sasha', 'mqtt_topics': { 'arduino/bedroom/sensor2': ['moisture'] }, 'carbon_server': 'brynaws', 'carbon_port': 2003 }
#config = { 'mqtt_server': 'sasha', 'topic': 'arduino/bedroom/sensor2', 'carbon_server': 'brynaws', 'carbon_port': 2003 }

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

def on_message_carbon(client, userdata, message):
    """ Send MQTT JSON metric objects to carbon server """
    print(message.payload)
    data = json.loads(message.payload.decode("utf-8"))
    for metric in config['mqtt_topics'][message.topic]:
        value = data['moisture']
        value = data[metric]
        timestamp = int(time.time())
        metric_path = message.topic.replace('/', '.') + '.' + metric
        payload = '%s %s %d\n' % (metric_path, value, timestamp)
        #log('sending message to carbon:\n%s' % message)
        if DEBUG:
            print(message.topic)
            print(payload)
            return
        sock = socket.socket()
        sock.connect((config['carbon_server'], config['carbon_port']))
        sock.sendall(payload.encode())
        sock.close()




print(config['mqtt_server'])
print(config['mqtt_topics'])

#if DEBUG:
#    subscribe.callback(on_message_print, config['topic'], hostname=config['server'])
#else:
#    subscribe.callback(on_message_carbon, config['topic'], hostname=config['server'])
#
#for topic in 
#subscribe.callback(on_message_carbon, config['topic'], hostname=config['mqtt_server'])

for topic in config['mqtt_topics']:
    subscribe.callback(on_message_carbon, topic, hostname=config['mqtt_server'])


