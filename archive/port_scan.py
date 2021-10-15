import socket
import subprocess
import sys
from datetime import datetime

subprocess.call("clear", shell = True)


def scan():
    global remote_server_IP
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_server_IP, port))
            if result == 0:
                print(f"Port {port}: Open")
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print("Could not connect to server. Exiting")
        sys.exit()


if __name__ == "__main__":

    remote_server = input("Please enter remote host to scan:\n")
    remote_server_IP = socket.gethostbyname(remote_server)

    print("-" * 60)
    print("Starting scan for open ports")
    print("-" * 60)

    start_time = datetime.now()

    scan()

    end_time = datetime.now()

    final_time = end_time - start_time

    print(f"Process completed in {final_time}!")
