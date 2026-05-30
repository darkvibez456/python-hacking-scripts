import socket
import argparse
import sys
from datetime import datetime

# Colors for professional UI
G = '\033[92m'  # Green
Y = '\033[93m'  # Yellow
R = '\033[91m'  # Red
C = '\033[96m'  # Cyan
W = '\033[0m'   # White

BANNER = f"""{C}
  _____             _     __      ___ _             
 |  __ \           | |    \ \    / (_) |            
 | |  | | __ _ _ __| | __  \ \  / / _| |__   ___ ____
 | |  | |/ _` | '__| |/ /   \ \/ / | | '_ \ / _ \_  /
 | |__| | (_| | |  |   <     \  /  | | |_) |  __/ / / 
 |_____/ \__,_|_|  |_|\_\     \/   |_|_.__/ \___/___|
                                                     
          {Y}PYTHON HACKING SCRIPTS - PORT SCANNER{W}
          {G}MADE BY: DARK VIBEZ | v1.0{W}
"""

def port_scan(target, ports):
    print(f"{G}[*]{W} Scanning Target: {C}{target}{W}")
    print(f"{G}[*]{W} Scan Started At: {Y}{datetime.now().strftime('%H:%M:%S')}{W}")
    print(f"{C}" + "-" * 50 + f"{W}")

    open_ports = []
    try:
        for port in range(ports[0], ports[1] + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{G}[+]{W} Port {Y}{port}{W} is {G}OPEN{W}")
                open_ports.append(port)
            sock.close()
    except KeyboardInterrupt:
        print(f"\n{R}[-]{W} Scan interrupted by user.")
        sys.exit()
    
    print(f"{C}" + "-" * 50 + f"{W}")
    print(f"{G}[*]{W} Scan Finished.")
    if open_ports:
        print(f"{G}[+]{W} Total Open Ports: {Y}{len(open_ports)}{W}")
    else:
        print(f"{R}[-]{W} No open ports found.")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Professional Port Scanner")
    parser.add_argument("-t", "--target", help="Target IP or Hostname")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (default: 1-1024)")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
        port_range = args.ports.split('-')
        ports = (int(port_range[0]), int(port_range[1]))
        port_scan(target_ip, ports)
    except Exception as e:
        print(f"{R}[-]{W} Error: {e}")

if __name__ == "__main__":
    main()
