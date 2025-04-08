scan_presets = {
    "Quick Scan": "-T4 -F",
    "Full Port Scan": "-p 1-65535 -T4",
    "Aggressive Scan": "-A",
    "OS Detection": "-O",
    "Stealth SYN Scan": "-sS",
    "Service Version Detection": "-sV",
    "Ping Scan (discover alive hosts)": "-sn",
    "UDP Scan (basic)": "-sU -T4 --top-ports 20",
    "Firewall Evasion": "-f -T2",
    "Traceroute + OS Fingerprint": "-A --traceroute"
}
