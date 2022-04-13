from server_config import *

try:
  import usocket as socket
except:
  import socket

#from machine import Pin

import esp
esp.osdebug(None)

import gc
gc.collect()


import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.ifconfig((ip_srv, ip_mask, ip_gw, ip_dns))
sta_if.connect(essid, netpw)
sta_if.isconnected()

while sta_if.isconnected() == False:
  pass

print('...')
print('Connection successful')
print(sta_if.ifconfig())

#led = Pin(2, Pin.OUT)
#Define pines
#No usar ni el 1 ni el 3

