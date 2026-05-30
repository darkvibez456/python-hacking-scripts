import requests
import argparse
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Colors
G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
C = '\033[96m'
W = '\033[0m'

BANNER = f"""{C}
  _____             _     __      ___ _             
 |  __ \           | |    \ \    / (_) |            
 | |  | | __ _ _ __| | __  \ \  / / _| |__   ___ ____
 | |  | |/ _` | '__| |/ /   \ \/ / | | '_ \ / _ \_  /
 | |__| | (_| | |  |   <     \  /  | | |_) |  __/ / / 
 |_____/ \__,_|_|  |_|\_\     \/   |_|_.__/ \___/___|
                                                     
          {Y}PYTHON HACKING SCRIPTS - XSS DETECTOR{W}
          {G}MADE BY: DARK VIBEZ | v1.0{W}
"""

def scan_xss(url):
    payload = "<script>alert('XSS')</script>"
    print(f"{G}[*]{W} Target URL: {C}{url}{W}")
    print(f"{C}" + "-" * 50 + f"{W}")

    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        forms = soup.find_all('form')
        print(f"{G}[*]{W} Found {Y}{len(forms)}{W} forms.")

        for form in forms:
            action = form.get('action')
            post_url = urljoin(url, action)
            method = form.get('method', 'get').lower()
            
            print(f"{G}[+]{W} Testing form at: {Y}{post_url}{W}")
            
            if method == 'post':
                r = requests.post(post_url, data={'q': payload})
            else:
                r = requests.get(post_url, params={'q': payload})
            
            if payload in r.text:
                print(f"{R}[!!!] XSS VULNERABILITY DETECTED!{W}")
                print(f"{R}[!!!] Payload: {W}{payload}")
            else:
                print(f"{G}[*]{W} Form seems secure.")

    except Exception as e:
        print(f"{R}[-]{W} Error: {e}")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Professional XSS Detector")
    parser.add_argument("-u", "--url", help="Target URL to scan")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()
    scan_xss(args.url)

if __name__ == "__main__":
    main()
