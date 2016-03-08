import socket
#import time

#UDP_IP = "RYAN_DELL_XPS_WIN8" #Dell desktop @ home
#UDP_PORT = 7002
#UDP_IP = "RYAN-iMac-CP-WIN10" #iMac @ CP/media lab wifi
#UDP_PORT = 7001
#UDP_IP = "RYAN_YOGA_2_PRO" #Yoga @ CP/media lab wifi
#UDP_PORT = 7002
#UDP_IP = "18.85.26.132" #iMac @ CP/media lab wifi
#UDP_PORT = 7003
UDP_IP = "18.85.27.198" #Yoga @ CP/media lab wifi
UDP_PORT = 7004
#UDP_IP = "192.168.0.11" #Yoga @ home wifi
#UDP_PORT = 7001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

outputPath = "C:/Users/RYAN/Documents/GitHub/Realtime_Sim/Data/ColortizerData.txt"

# first run
previousData, addrv = sock.recvfrom(5000) # buffer size is 1024 bytes
print "first run receied message:", data

# loop run
count = 0
while True:
    count ++
    data, addrv = sock.recvfrom(5000) # buffer size is 1024 bytes
    print "loop run - count: ", count, ", receied message:", data
    if data != previousData:
        f = open(outputPath, "w")
        f.write(data)
        f.close()
    previousData = data
    #time.sleep(1.0) #sleep will cause delay issue!!!