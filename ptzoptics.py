import socket

def recallPreset(host, port, command):
    try: 
        #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        #s.connect((host, port))
        #data = bytes.fromhex(command)
        #r = s.send(data)
        #s.close()
        #print(r)
        #return(r)

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((host, port))
            data = bytes.fromhex(command)
            s.send(data)
            r = s.recv(1024)

        print('Received', repr(r))
        return(r)

    except:
        print("there was an error")

