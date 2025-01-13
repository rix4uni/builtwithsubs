import requests
from lxml import html
import urllib3
import re
import sys
import argparse
import time

# Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# prints the version message
version = "v0.0.1"

def PrintVersion():
    print(f"Current builtwithsubs version {version}")

def PrintBanner():
    banner = rf"""
    __            _  __ __             _  __   __                  __         
   / /_   __  __ (_)/ // /_ _      __ (_)/ /_ / /_   _____ __  __ / /_   _____
  / __ \ / / / // // // __/| | /| / // // __// __ \ / ___// / / // __ \ / ___/
 / /_/ // /_/ // // // /_  | |/ |/ // // /_ / / / /(__  )/ /_/ // /_/ /(__  ) 
/_.___/ \__,_//_//_/ \__/  |__/|__//_/ \__//_/ /_//____/ \__,_//_.___//____/"""
    print(f"{banner}\n\t\t\t\t\tCurrent builtwithsubs version {version}\n")

# Argument parser setup
parser = argparse.ArgumentParser(description="Scrape builtwith relationships with cookie and api key.")
parser.add_argument('--timeout', default=15, type=int, help='Timeout (in seconds) for http client (default 15)')
parser.add_argument('--silent', action='store_true', help='Run without printing the banner')
parser.add_argument('--version', action='store_true', help='Show current version of builtwithsubs')
args = parser.parse_args()

if args.version:
    PrintBanner()
    PrintVersion()
    exit(1)

if not args.silent:
    PrintBanner()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Process each line from standard input
for domain in sys.stdin:
    domain = domain.strip()  # Remove leading/trailing whitespaces

    if domain:  # If the line is not empty
        response = requests.get(f'https://builtwith.com/relationships/{domain}', headers=headers, timeout=args.timeout).content
        html = html.fromstring(response)

        for target in html.xpath('//td[@class="hbomb"]/a/text()'):
            print(target)