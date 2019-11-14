import os
import sys
import subprocess
# print("Hhhh")
from subprocess import Popen, PIPE
import time

while True:
    # os.system('sudo su')
    os.system('gcloud compute instances start i-ao-acoustic-train-2k19')
    os.system('sudo gcloud beta compute --project "athenas-owl-dev" ssh --zone "us-east1-c" "i-ao-acoustic-train-2k19"')
    # time.sleep(40)
    # os.system('gcloud compute instances stop i-ao-acoustic-train-2k19')
    time.sleep(70)