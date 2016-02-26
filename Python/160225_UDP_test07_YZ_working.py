import socket

UDP_IP = "RYAN_YOGA_2_PRO"
UDP_PORT = 7001
#UDP_IP = "RYAN_DELL_XPS_WIN8"
#UDP_PORT = 7002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(9999) # buffer size is 1024 bytes
    print "received message:", data