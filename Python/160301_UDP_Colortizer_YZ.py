"""
Realtime Simulator

written by Yan "Ryan" Zhang <ryanz@mit.edu>
for MIT Media Lab, Changing Place Group, CityScope Project
March.1st.2016
"""

import socket

# UDP_IP = "RYAN_DELL_XPS_WIN8" #Dell desktop @ home
# UDP_PORT = 7002
# UDP_IP = "RYAN-iMac-CP-WIN10" #iMac @ CP/media lab wifi
# UDP_PORT = 7001
# UDP_IP = "RYAN_YOGA_2_PRO" #Yoga @ CP/media lab wifi
# UDP_PORT = 7002
# UDP_IP = "18.85.26.132" #iMac @ CP/media lab wifi
# UDP_PORT = 7003
UDP_IP = "18.85.27.198" #Yoga @ CP/media lab wifi
UDP_PORT = 7004
# UDP_IP = "192.168.0.11" #Yoga @ home wifi
# UDP_PORT = 7001
# UDP_IP = "104.131.179.31" #Colotizer Cloud @ Karthik Server. doesn't work
# UDP_PORT = 6666

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

outputPath = "C:/Users/RYAN/Documents/GitHub/Realtime_Sim/Data/ColortizerData.txt"

count = 0

while True:
    if count == 0:
        previousData, addrv = sock.recvfrom(5000) # buffer size is 1024 bytes
        print previousData
        print "above is the first run receied message"
    else:
        data, addrv = sock.recvfrom(5000) # buffer size is 1024 bytes
        print data
        print "above is the loop run receied message - count: ", count
        if data != previousData:
            print "colortizer data changed! "
            f = open(outputPath, "w")
            f.write(data)
            f.close()
            print "writing to text file completed! "
        previousData = data
    count += 1