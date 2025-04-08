import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from scanner import scan_range
from nmap_wrapper import run_nmap_scan
from presets import scan_presets

def launch_gui():
    window = tk.Tk()
    window.title("Nmap Assistant")
    window.geometry("800x600")
    window.resizable(True, True)

    # ---------- Input Fields ----------
    frame = tk.Frame(window)
    frame.pack(pady=10)

    tk.Label(frame, text="Target IP or Domain:").grid(row=0, column=0, sticky="w")
    target_entry = tk.Entry(frame, width=40)
    target_entry.grid(row=0, column=1, padx=5)

    tk.Label(frame, text="Nmap Preset:").grid(row=1, column=0, sticky="w")
    preset_var = tk.StringVar()
    preset_menu = ttk.Combobox(frame, textvariable=preset_var, width=37)
    preset_menu['values'] = list(scan_presets.keys())
    preset_menu.set("Quick Scan")
    preset_menu.grid(row=1, column=1, padx=5)

    tk.Label(frame, text="Custom Nmap Flags (optional):").grid(row=2, column=0, sticky="w")
    custom_flags_entry = tk.Entry(frame, width=40)
    custom_flags_entry.grid(row=2, column=1, padx=5)

    local_scan_var = tk.BooleanVar()
    local_scan_check = tk.Checkbutton(frame, text="Run custom TCP port scan (1–1024)", variable=local_scan_var)
    local_scan_check.grid(row=3, column=1, sticky="w", pady=5)

    # ---------- Output Box ----------
    output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=25, width=100)
    output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # ---------- Run Button ----------
    def run_scans():
        target = target_entry.get().strip()
        preset = preset_var.get()
        custom_flags = custom_flags_entry.get().strip()
        output_text.delete(1.0, tk.END)

        if not target:
            messagebox.showerror("Input Error", "Please enter a valid IP or domain.")
            return

        if local_scan_var.get():
            output_text.insert(tk.END, f"Running custom TCP port scan on {target}...\n")
            open_ports = scan_range(target, 1, 1024, log_output=True)
            output_text.insert(tk.END, f"\nOpen Ports: {open_ports}\n\n")

        if custom_flags:
            output_text.insert(tk.END, f"Running custom Nmap scan: nmap {custom_flags} {target}\n\n")
            result = run_nmap_scan(target, custom_flags)
        else:
            flags = scan_presets.get(preset, "-F")
            output_text.insert(tk.END, f"Running preset scan: {preset} ({flags})\n\n")
            result = run_nmap_scan(target, flags)

        output_text.insert(tk.END, result)

    run_button = tk.Button(window, text="Run Scan", command=run_scans, bg="#4CAF50", fg="white", padx=20, pady=5)
    run_button.pack(pady=10)

    window.mainloop()
