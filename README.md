<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=00FFAA&center=true&vCenter=true&width=600&lines=OwlNet+%F0%9F%A6%89;MultiTool+for+Security+Testing;WebDoS+%7C+Spammer+%7C+Nuker" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

---

## 🦉 **OwlNet** — The Ultimate Discord & Web Security Testing Suite

OwlNet is a powerful, modular multi-tool written in Python, designed for **educational purposes** and **authorized penetration testing**. With a sleek terminal interface and robust proxy support, it's built for security researchers and ethical hackers who need reliable tools for testing and analysis.

---

## 🎯 **What's Inside**

| Tool | Description |
|------|-------------|
| 🌐 **WebDoS** | Layer 7 DoS attack simulator with proxy rotation, randomized headers, and user-agent spoofing. |
| 🕸️ **Discord Webhook Spammer** | Mass-spam any Discord webhook with custom messages, rotating usernames, avatars, and proxies. |
| 💥 **Discord Server Nuker** | Full server takeover toolkit — delete channels/roles, ban/kick members, create webhooks, spam, rename server, and much more. |

---

> ⚠️ **DISCLAIMER**: This tool is intended **strictly for educational and authorized security testing purposes**. Any unauthorized or malicious use is prohibited. The author assumes **no liability** for any damages or legal consequences resulting from misuse.

---

## ✨ **Key Features**

- 🔄 **Proxy Rotation** — Automatically scrapes and tests proxies from multiple sources for anonymity.
- ⚡ **Async & Multi-threading** — High-performance concurrent requests for maximum efficiency.
- 🎨 **Beautiful Terminal UI** — Color-coded output, banners, and user-friendly menus.
- 🧩 **Modular Design** — Each tool is independent and easily customizable.
- 🛡️ **Anti-Rate Limit Bypass** — Smart retry logic and proxy rotation to avoid IP bans.
- 📦 **Zero External Databases** — All proxies are scraped live from public lists.


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

## 📦 **Dependencies**

OwlNet requires the following Python packages (automatically installed via `requirements.txt`):

- `colorama` — Terminal colors and styling.
- `requests` — HTTP requests for API calls.
- `aiohttp` — Asynchronous HTTP client.
- `asyncio` — Async/await support.
- `pystyle` — Beautiful terminal animations and gradients.
- `beautifulsoup4` — HTML parsing for proxy scraping.
- `rich` — Enhanced terminal formatting.

---

## 🧩 **Modules Overview**

```
OwlNet/
├── OwlNet.py                # Main menu and launcher
├── OwlDoS.py                # WebDoS attack tool
├── OwlSpammer.py            # Discord webhook spammer
├── d-proxy.py               # Proxy scraper utility
├── requirements.txt         # Python dependencies
├── tools/
│   └── OwlNuke/
│       └── main.py          # Discord server nuker
└── Plugins/
    ├── colors.py            # Color palettes
    ├── funcs.py             # Utility functions
    ├── logger.py            # Logging system
    ├── nuking.py            # Nuker core logic
    └── tools.py             # API wrappers and helpers
```

---

## 🚀 **Usage Guide**

### 🌐 **WebDoS**
```bash
python OwlDoS.py
```
- Enter the target URL and number of requests.
- The tool scrapes proxies, rotates IPs, and launches the attack.

### 🕸️ **Discord Webhook Spammer**
```bash
python OwlSpammer.py
```
- Provide webhook URL, username, avatar, and message.
- Proxies are scraped, tested, and rotated automatically.

### 💥 **Discord Server Nuker**
```bash
python tools/OwlNuke/main.py
```
- Enter your Discord bot token and guild ID.
- Choose from **18+ nuke options**:
  1. Delete All Channels
  2. Delete All Roles
  3. Ban All Members
  4. Kick All Members
  5. Create Channels
  6. Create Roles
  7. Unban All Members
  8. Webhook Spam Guild
  9. Message Spam Guild
  10. Rename All Channels
  11. Rename All Roles
  12. Nick All Users
  13. UnNick All Users
  14. Change Guild Name
  15. Change Guild Icon
  16. Remove All Emojis
  17. DM All Members
  18. NUKE — Full Server Wipe

---

## 🔒 **Legal & Ethical Use**

This tool is provided **for educational and research purposes only**. By using OwlNet, you agree to:

- ✅ Use it only on systems you own or have explicit permission to test.
- ✅ Comply with all applicable laws and regulations.
- ❌ **Not** use it for illegal activities, harassment, or unauthorized access.

> **The author is not responsible for any misuse of this tool.**

---

## 🤝 **Contributing**

Contributions are welcome! If you'd like to improve OwlNet, add new features, or fix bugs:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## ⭐ **Support the Project**

If you find OwlNet useful, please give it a ⭐ on GitHub and share it with the community!

---

<p align="center">
  <b>Made with ❤️ by Venex</b>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/esfelurm/OwlNet?style=social" />
  <img src="https://img.shields.io/github/forks/esfelurm/OwlNet?style=social" />
  <img src="https://img.shields.io/github/watchers/esfelurm/OwlNet?style=social" />
</p>
