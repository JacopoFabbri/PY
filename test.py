import os
import subprocess
import logging
import threading
import time

#os.system("new.py")

def thread_function():
    subprocess.call('start /wait python new.py', shell=True)

x = threading.Thread(target=thread_function)
x.start()
os.system("new.py")