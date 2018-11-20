import os
import sys
import time

def get(url):
    start_time = time.time()
    os.system('wget ' + url)
    elapsed_time = time.time() - start_time
    return elapsed_time

def main():
    if len(sys.argv) != 2:
        print("Usage: \"python client.py IP_ADDR\"")
    else:
        total_time = 0
        for _ in range(30):
            total_time += get(sys.argv[1] + ":8080/?nom=Loic")
        print(total_time / 30)

main()
