from ptzoptics import *
import socket

#variables
hosts = ['172.20.1.50']
port = 1259
presetNumber = input("what preset do you want to recall (e.g. 01): ")
command = f'8101043F02{presetNumber}FF'


#functions

for host in hosts:
    recallPreset(host, port, command)