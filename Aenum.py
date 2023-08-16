#!/usr/bin/env python
import sys
import subprocess
import threading
from queue import Queue

# Read IP addresses from a file
def read_ip_addresses(filename):
    with open(filename, 'r') as file:
        ip_addresses = [line.strip() for line in file.readlines()]
    return ip_addresses

# Run enum4linux on an IP address with additional flags
def run_enum4linux(ip_address, flags):
    output_filename = ip_address + "-enum4linux-scan.txt"
    command = ['enum4linux'] + flags + [ip_address]
    with open(output_filename, 'w') as output_file:
        subprocess.call(command, stdout=output_file, stderr=subprocess.STDOUT)
    print(f"enum4linux scan for {ip_address} complete. Output saved to {output_filename}")

def worker():
    while True:
        ip_address = ip_queue.get()
        if ip_address is None:
            break
        run_enum4linux(ip_address, flags)
        ip_queue.task_done()

if __name__ == "__main__":
    if len(sys.argv) < 2 or "--help" in sys.argv:
        print("Usage: python Aenum.py [path] [threads] [enum_flags]\n")
        print("  path: Path to the file containing IP addresses, separated by newlines.")
        print("  threads: Number of threads for concurrent scanning. Be careful setting this too high!!")
        print("  enum_flags: Additional flags to pass to enum4linux.")
        sys.exit(0)

    input_filename = sys.argv[1]
    num_threads = int(sys.argv[2])
    flags = sys.argv[3:]
    
    ip_addresses = read_ip_addresses(input_filename)
    ip_queue = Queue()

    for ip in ip_addresses:
        ip_queue.put(ip)
    
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)
    
    ip_queue.join()
    
    # Stop workers
    for _ in range(num_threads):
        ip_queue.put(None)
    
    for thread in threads:
        thread.join()
                      
