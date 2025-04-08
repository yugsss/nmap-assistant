import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return result == 0
    except Exception:
        return False

def scan_range(host, start, end, threads=100, timeout=1, log_output=False):
    open_ports = []

    def task(port):
        if scan_port(host, port, timeout):
            if log_output:
                print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(start, end + 1):
            executor.submit(task, port)

    return open_ports
