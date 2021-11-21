import socket
import sys
import cv2
import base64
import imutils


if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from

    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
    exit(1)

BUFF_SIZE = 12288

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)

# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

vid = cv2.VideoCapture(1)
addressClient = ""
while True:
    print("####### Server is listening for one connection #######")
    data, address = s.recvfrom(BUFF_SIZE)
    addressClient = address
    break
   
while(True):
    _,frame = vid.read()
    frame = imutils.resize(frame,width=300)
    encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
    message = base64.b64encode(buffer)
    # cv2.imshow("HEEE", frame)
    s.sendto(message, address)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
