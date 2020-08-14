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
    checks = [
    (check_reboot, "Pending-Reboot"),
    (check_root_full, "Root partition full"),
    (check_cpu_usage, "Not enough disk space")
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False
        if not everything_ok:
            sys.exit(1)

print("Everything is okk😂")
sys.exit(0)
