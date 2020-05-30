from subprocess import call
import os
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

while True:
    call(["python3", "yomitori.py"], cwd=dir_path)
    print('run spider')
    time.sleep(30)