import os
import subprocess
import random
import time
from datetime import date

def runcmd(cmd, verbose = False, *args, **kwargs):
    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    else:
        print(std_err)

def main():
    # get date
    today = date.today()
    print("Downloading request items' information on: {}".format(today))

    # make temporary download directory
    temp_dir = "temp"
    rmdir_cmd = "rm -rf {}".format(temp_dir)
    runcmd(rmdir_cmd, verbose = True)
    mkdir_cmd = "mkdir -p {}".format(temp_dir)
    runcmd(mkdir_cmd, verbose = True)

    # get items to search
    f = open("getracker_items.txt", "r")
    items = [line.strip() for line in f.readlines()]
    f.close()

    num_items = 0
    # download item info
    for item in items:
        if len(item) == 0 or item[0] == "#":
            continue

        wget_cmd = "wget https://www.ge-tracker.com/item/{} -P {}".format(item, temp_dir)
        runcmd(wget_cmd, verbose = False)
        time.sleep(random.randint(1, 400) / 100)
        num_items += 1
        if num_items % 10 == 0:
            print("Sleeping 5 minutes...", end = " ", flush = True)
            time.sleep(300)
            print("Woke up!")

if __name__ == "__main__":
    main()
