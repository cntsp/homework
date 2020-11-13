import socket
import sys

HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])
data = input(">>>:").strip()


# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    try:
        c1 = sock.connect((HOST, PORT))
        print("line 13:", c1)
        sock.sendall(bytes(data + "\n", "utf-8"))
    except Exception as e:
        print("error:", e)

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))