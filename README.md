### README.md

# 🔍 Nmap Assistant

A powerful and user-friendly desktop application that combines custom port scanning and advanced Nmap scanning in one place. Perfect for cybersecurity students, enthusiasts, or professionals who want a fast, accessible interface for running network scans.

---

## 🚀 Features

- ✅ **Custom TCP Port Scanner**
- 🧠 **Predefined Nmap Scan Modes**
- 💡 **Support for Custom Nmap Flags**
- 🎛️ **Intuitive GUI with Tkinter**
- 📤 (Upcoming) Export scan results to text or JSON

---

## 📸 Screenshot
> *(Insert screenshot of the GUI here)*

---

## 🧱 Project Structure

```
nmap-assistant/
├── main.py                # Entry point – launches the GUI
├── gui.py                 # GUI built with Tkinter
├── scanner.py             # Custom multithreaded TCP port scanner
├── nmap_wrapper.py        # Wrapper to run Nmap via subprocess
├── presets.py             # Predefined Nmap scan options
├── requirements.txt       # Optional dependency list
├── outputs/               # Folder for future exported results
└── README.md              # You're reading it!
```

---

## 🛠️ Requirements

- Python 3.6+
- Nmap must be installed and available in your system's PATH
- Tkinter (usually included with Python)

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/nmap-assistant.git
cd nmap-assistant
```


## 🧪 Usage

### Run the Application
```bash
python main.py
```

### Inside the App:
- Enter the target IP or domain
- Select a predefined Nmap scan type **OR** enter custom flags
- Optionally check the "Run Custom Port Scanner" box
- Click **Run Scan** to execute
- View results in the scrollable window

---

## 🧠 Nmap Presets

| Mode             | Nmap Flags        |
|------------------|-------------------|
| Quick Scan       | `-T4 -F`          |
| Full Scan        | `-p 1-65535 -T4`  |
| OS Detection     | `-O`              |
| Service Version  | `-sV`             |
| Aggressive Scan  | `-A`              |
| Stealth Scan     | `-sS`             |

---

## 🤝 Contributing

PRs are welcome! Open an issue or submit a pull request to improve the app.

---

## 👨‍💻 Author

**Yugam Chheda**  
[GitHub](https://github.com/yugsss)  
[LinkedIn](https://www.linkedin.com/in/yugam-chheda/)
