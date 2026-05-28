import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
from datetime import datetime

init(autoreset=True)

print(Fore.CYAN + """
========================================
        PYTHON PORT SCANNER
========================================
""")

target = input(Fore.YELLOW + "Enter target IP or domain: ")

start_port = int(input(Fore.YELLOW + "Enter start port: "))
end_port = int(input(Fore.YELLOW + "Enter end port: "))

print(Fore.CYAN + "\n----------------------------------------")
print(Fore.CYAN + f"Scanning Target: {target}")
print(Fore.CYAN + f"Time Started: {datetime.now()}")
print(Fore.CYAN + "----------------------------------------\n")

open_ports = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:

            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "Unknown Service"

            print(Fore.GREEN + f"[OPEN] Port {port} | Service: {banner}")

            open_ports.append((port, banner))

        s.close()

    except:
        pass


with ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(start_port, end_port + 1):
        executor.submit(scan_port, port)

with open("scan_results.txt", "w") as file:
    file.write(f"Target: {target}\n")
    file.write(f"Scan Time: {datetime.now()}\n\n")

    for port, banner in open_ports:
        file.write(f"Port {port} OPEN | Service: {banner}\n")

print(Fore.CYAN + "\n----------------------------------------")
print(Fore.CYAN + "Scan Complete.")
print(Fore.CYAN + f"Total Open Ports Found: {len(open_ports)}")
print(Fore.CYAN + "Results saved to scan_results.txt")
print(Fore.CYAN + "----------------------------------------")