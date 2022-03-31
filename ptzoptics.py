import socket
import time
socket.setdefaulttimeout(5)

def openConnection(host, port, command):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        s.connect((host, port))
        s.send(bytes.fromhex(command))
        r = s.recv(1024)

#        #checking response
#        if r.hex()[0:2] == "90" and r.hex()[4:6] == "FF":
#            print(r.hex())
#            print("command received")
#        else:
#            print(r.hex())
#            print(r.hex()[0:2])
#            print(r.hex()[5:7])
#            print("something failed")
    time.sleep(2)
    return(r)

def recallPreset(host, port, presetNumber):
    if len(presetNumber) == 2:
        command = f"8101043F02{presetNumber}FF"
    else:
        command = f"8101043F020{presetNumber}FF"
    return(openConnection(host, port, command))

def setPreset(host, port, presetNumber):
    if len(presetNumber) == 2:
        command = "8101043F01{presetNumber}FF"
    else:
        command = "8101043F010{presetNumber}FF"
    return(openConnection(host, port, command))

def getPanTiltPosition(host, port):
    command = "81090612FF"
    return(openConnection(host, port, command))

def getZoomPosition(host, port):
    command = "81090447FF"
    return(openConnection(host, port, command))

def setPanTiltPosition(host, port, pan, tilt):
    command = f"810106021410{pan}{tilt}FF"
    return(openConnection(host, port, command))

def setZoomPosition(host, port, zoom):
    command = f"81010447{zoom}FF"
    return(openConnection(host, port, command))

def convertPan(r):
    pan = r.hex()[4:12]
    return(pan)

def convertTilt(r):
    tilt = r.hex()[12:20]
    return(tilt)

def convertZoom(r):
    zoom = r.hex()[4:12]
    return(zoom)