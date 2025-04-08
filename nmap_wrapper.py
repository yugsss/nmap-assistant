import subprocess

def run_nmap_scan(target, options="-sS"):
    """Run an Nmap scan with given options."""
    try:
        command = f"nmap {options} {target}"
        result = subprocess.run(command.split(), capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[ERROR] Failed to run Nmap: {e}"


