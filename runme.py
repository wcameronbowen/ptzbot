from ptzoptics import *
import socket
import json

#module settings
socket.setdefaulttimeout(5)

#static variables
port = 1259

#parse json
print("parsing json input")
f = open("camera-config.json",)
data = json.load(f)

#intialize arrays
hosts = []
for object, details in data.items():
    print(f"loading {object}")
    hosts.append(details["ip"])



#functions

#for host in hosts:
#
#    r = setPosition(host, port, pan, tilt)
#    if r.hex() == "904yFF" :
#        print("command received")
#    print(r.hex())


for host in hosts:
    for preset in data["camera-1"]["presets"]:
        try:
            print(preset)
            recallPreset(host, port, preset)
            print(getPanTiltPosition(host, port).hex())
            print(getZoomPosition(host, port).hex())
        except socket.timeout:
            print("doesn't seem to be anything listening")


#for host in hosts:
#    for preset in data["camera-1"]["presets"]:
#        pan = preset["pan"]
#        tilt = preset["tilt"]
#        zoom = preset["zoom"]
#        setPanTiltPosition(host, port, pan, tilt)
#        setZoomPosition(host, port, zoom)
#        setPreset(host, port, preset)