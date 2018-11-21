import os
import sys
import time
import asyncio

def get(url):
    os.system('wget ' + url)

def main():
    if len(sys.argv) != 2:
        print("Usage: \"python client.py IP_ADDR\"")
    else:
        total_time = 0
        for _ in range(30):
            start_time = time.time()
            get(sys.argv[1] + ":8080/?nom=Loic")
            elapsed_time = time.time() - start_time
            total_time += elapsed_time
        print(total_time / 30)

main()
