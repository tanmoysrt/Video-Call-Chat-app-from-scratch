import socket
import sys
import threading

if len(sys.argv) == 5:
    # Get "IP address of Server" and also the "port number" from

    ip_sender = sys.argv[1]
    port_sender = int(sys.argv[2])
    ip_receiver = sys.argv[3]
    port_receiver = int(sys.argv[4])
else:
    print("Run like : python3 server.py <sender_ip> <sender_port> <receiver_ip> <receiver_port>")
    exit(1)


def receiver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip_sender, port_sender))
    while True:
        msg = s.recvfrom(1024)
        print("\n"+msg[0].decode())
        if "exit" in msg[0].decode() or "bye" in msg[0].decode():
            sys.exit()


def sender():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = "hello"
    while True:
        if "bye" in text or "exit" in text or "finish" in text:
            exit()
        else:
            text = input(ip_receiver + " : ")
            text = ip_receiver +":"+text
            s.sendto(text.encode(), (ip_receiver, port_receiver))


send = threading.Thread(target=sender)
receive = threading.Thread(target=receiver)

send.start()
receive.start()