import sys
import socket
import threading
from datetime import datetime

print("Port Scanner V1.0a")
ip_scan = input("Web URL or IP address: ")
st_port = int(input("Please enter a starting port. Deafult = 1 ") or 1)
ed_port = int(input("Please enter a end port. Default = 8000 ") or 8000)


def scan_ports(port):
    """
    AF_INET is used to designate the type of Adress Family.
    INET refers to IPV4 - we can change this to AF_INET6, if
    we wanted to address IVP6.

    SOCK_STREAM is address TCP, we can use
    SOCK_DGRAM if we need to address UDP
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    """
    This does the same as .connect() except it returns and error indicator 
    instead of raising an exception. 
    """
    connection = sock.connect_ex((target, port))
    if (not connection):
        print(f"Port {port}: Open")
    
    sock.close()


try:
    target = socket.gethostbyname(str(ip_scan))

# Exception for Get Address Info.
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

if __name__ == "__main__":
    print("\nStarting Scan")
    for port in range(st_port, ed_port + 1):
        thread = threading.Thread(target=scan_ports, args=(port,))
        thread.start()

    print("finished.")
