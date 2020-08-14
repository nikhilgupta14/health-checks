#!/usr/bin/env python3

import shutil
import psutil
import sys

def check_disk_usage(disk, min_percent, min_absolute):
    du = shutil.disk_usage(disk)
    du_percent = du.free / du.total
    percent_free = 100 * du.free / du.total
    gigabyte_free = du.free / 2 ** 30
    if percent_free < min_percent or gigabyte_free < min_absolute:
        print("Gigabyte Free: ", gigabyte_free);
        return False
    return True


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage('/', 2, 10) or not check_cpu_usage():
    print("ERROR: Not enough disk space.")
    sys.exit(1)

print("Everything is okk😂")
sys.exit(0)
