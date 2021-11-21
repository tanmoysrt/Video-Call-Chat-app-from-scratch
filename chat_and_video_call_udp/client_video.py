import socket
import sys
import base64
import cv2
import numpy as np

np.set_printoptions(threshold=sys.maxsize)


if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)

BUFF_SIZE = 12288

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
print("Do Ctrl+c to exit the program !!")


s.sendto("hello".encode('utf-8'), (ip, port))
# Let's send data through UDP protocol
while True:
    packet, address = s.recvfrom(BUFF_SIZE)
    data = base64.b64decode(packet,' /')
    npdata = np.fromstring(data,dtype=np.uint8)
    print(len(npdata))
    print("\n\n")
    frame = cv2.imdecode(npdata,1)
    cv2.imshow("RECEIVING VIDEO",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# close the socket
s.close()
