#!/usr/bin/env python3

import shutil
import psutil
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_percent, min_gb):
    du = shutil.disk_usage(disk)
    du_percent = du.free / du.total
    percent_free = 100 * du.free / du.total
    gigabyte_free = du.free / 2 ** 30
    if percent_free < min_percent or gigabyte_free < min_gb:
        print("Gigabyte Free: ", gigabyte_free);
        return False
    return True


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

def check_root_full():
    """Return True if the root partition is full, False otherwise"""
    return check_disk_usage(disk='/', min_gb=2, min_percent=10)



# if not check_disk_usage('/', 2, 10) or not check_cpu_usage():
#     print("ERROR: Not enough disk space.")
#     sys.exit(1)
def main():
    if check_reboot():
        print("Pending-Reboot")
        sys.exit(1)
    if check_root_full():
        print("Root partition full")
        sys.exit(1)
        
print("Everything is okk😂")
sys.exit(0)
