import psutil

susprocess = False

def check_suspicious_processes():
    suspicious_processes = ["netcat", "nc", "nmap", "tcpdump"]
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in suspicious_processes:
            print(f"Suspicious process found: {proc.info['name']} (PID: {proc.info['pid']})")
            susprocess = True


check_suspicious_processes()
print(susprocess)