```markdown
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=3000&pause=1000&color=00FFAA&center=true&vCenter=true&width=600&lines=OwlNet+%F0%9F%A6%89;MultiTool+for+Security+Testing;WebDoS+%7C+Discord+Spammer+%7C+Nuker" alt="Typing SVG" />
</p>

---

## 🦉 **OwlNet** — The Ultimate Discord & Web Security Testing Suite

OwlNet is a powerful multi-tool written in Python, designed for **educational purposes** and **authorized penetration testing**. It includes:

- 🌐 **WebDoS** – Layer 7 DoS tool with proxy rotation and spoofed headers.
- 🕸️ **Discord Webhook Spammer** – Spam Discord webhooks with rotating proxies and custom messages.
- 💥 **Discord Server Nuker** – Wipe, ban, create, rename, and raid Discord servers using a bot token.

> **⚠️ DISCLAIMER**: This tool is for educational and authorized security testing only. Unauthorized use is strictly prohibited. The author is not responsible for any misuse.

---

## 🚀 **Features**

| Feature                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **WebDoS**               | Layer 7 DoS attacks with IP rotation, random headers, and user agents. |
| **Discord Webhook Spammer** | Mass-spam any Discord webhook with custom messages, usernames, and avatars. |
| **Discord Nuker**        | Full server takeover: delete channels/roles, ban/kick members, create webhooks, spam, and more. |
| **Proxy Support**        | Automatically scrapes and rotates proxies for anonymity and reliability.   |
| **Async & Multi-threading** | High-performance concurrent requests for maximum impact.                  |
| **Customizable**         | All tools are modular and configurable via CLI or input prompts.           |

---

## 📸 **Screenshots**

> *(Add your own screenshots here to showcase the tool in action)*

---

## 🛠️ **Installation**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/OwlNet.git
cd OwlNet
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run OwlNet**
```bash
python OwlNet.py
```

---

## ⚙️ **Requirements**

- Python 3.8 or higher
- `colorama`, `requests`, `aiohttp`, `asyncio`, `pystyle`, `rich`, `beautifulsoup4`

All dependencies are listed in `requirements.txt`.

---

## 🧩 **Modules Overview**

| File/Folder            | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `OwlNet.py`            | Main menu for launching all tools.                                         |
| `OwlDoS.py`            | Web DoS attack with proxy rotation and custom headers.           |
| `OwlSpammer.py`        | Discord webhook spammer with rotating proxies.                             |
| `tools/OwlNuke/main.py` | Full Discord server nuker (delete, ban, create, spam, etc.).              |
| `Plugins/`             | Core modules for logging, color palettes, API wrappers, and utilities.    |
| `requirements.txt`     | All required Python packages.                                              |
| `d-proxy.py`           | Proxy scraper utility (fetches SOCKS4/5, HTTP, HTTPS proxies).            |

---

## 📖 **Usage**

### **WebDoS**
```bash
python OwlDoS.py
```
- Enter target URL and number of requests.
- The tool will automatically scrape proxies and start the attack.

### **Discord Webhook Spammer**
```bash
python OwlSpammer.py
```
- Provide webhook URL, username, avatar URL, and message.
- The tool will scrape and test proxies, then spam the webhook.

### **Discord Server Nuker**
```bash
python tools/OwlNuke/main.py
```
- Enter your Discord bot token and guild ID.
- Choose from 18+ nuke options including:
  - Delete channels/roles
  - Ban/kick members
  - Create channels/roles
  - Webhook spam
  - Message spam
  - Rename server
  - Change server icon
  - And more...

---

## 🧠 **Proxy Scraping**

OwlNet automatically scrapes proxies from multiple public sources:
- `proxyscrape.com`
- `openproxylist.xyz`
- `github.com` (multiple proxy lists)
- `socks-proxy.net`
- And more...

Proxies are tested and rotated for each request to avoid rate limits.

---

## 🛡️ **Legal & Ethical Use**

This tool is intended for:
- ✅ Security research and testing on systems you own or have permission to test.
- ✅ Educational purposes to understand how DDoS and Discord APIs work.
- ❌ **NOT** for illegal activities, harassment, or unauthorized access.

> By using OwlNet, you agree to take full responsibility for your actions.

---

## 🤝 **Contributing**

Contributions are welcome! If you have improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.


## ⭐ **Support**

If you find this project useful, please give it a ⭐ on GitHub and share it with your friends!

---

<p align="center">
  <img src="https://img.shields.io/github/license/esfelurm/OwlNet?color=00FFAA&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-success?style=for-the-badge" />
</p>
```
