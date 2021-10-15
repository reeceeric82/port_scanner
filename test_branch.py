import sys
import socket
import threading
from datetime import datetime as dt

print("-" * 60)
print("Starting Up.")
print("-" * 60)


def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    connection = sock.connect_ex((target, port))
    if (not connection):
        print(f"Port {port} : Open")

    sock.close()


usage = "python3 main.py TARGET START_PORT ENDPORT"

if (len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])

except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target", target)

start_time = dt.now()

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target = scan, args = (port,))
    thread.start()

end_time = dt.now()
finish = end_time - start_time

print(f"Scan completed in {finish}.")

