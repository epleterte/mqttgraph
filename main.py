#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

import sys, os, socket, json, time

#DEBUG = True
DEBUG = False

config = { 'server': 'sasha', 'topic': 'arduino/bedroom/sensor2', 'carbon_server': 'brynaws', 'carbon_port': 2003 }

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

def on_message_carbon(client, userdata, message):
      print(message.payload)
      data = json.loads(message.payload.decode("utf-8"))
      value = data['moisture']
      timestamp = int(time.time())
      metric_path = config['topic'].replace('/', '.') + '.moisture'
      payload = '%s %s %d\n' % (metric_path, value, timestamp)
      #log('sending message to carbon:\n%s' % message)
      if DEBUG:
          print(payload)
          return
      sock = socket.socket()
      sock.connect((config['carbon_server'], config['carbon_port']))
      sock.sendall(payload.encode())
      sock.close()




print(config['server'])
print(config['topic'])

#if DEBUG:
#    subscribe.callback(on_message_print, config['topic'], hostname=config['server'])
#else:
#    subscribe.callback(on_message_carbon, config['topic'], hostname=config['server'])
#
subscribe.callback(on_message_carbon, config['topic'], hostname=config['server'])


