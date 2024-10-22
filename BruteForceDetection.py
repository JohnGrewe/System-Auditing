from collections import Counter

def detect_ssh_brute_force(log_file):
    failed_ips = []
    with open(log_file, 'r') as file:
        for line in file:
            if "Failed password" in line:
                failed_ips.append(line.split()[-4])
    ip_count = Counter(failed_ips)
    for ip, count in ip_count.items():
        if count > 5:
            print(f"Potential brute-force attack from {ip} with {count} failed attempts")

detect_ssh_brute_force("/var/log/auth.log")
