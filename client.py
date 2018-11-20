import os
import time

def get(url):
    start_time = time.time()
    os.system('wget ' + url)
    elapsed_time = time.time() - start_time
    return elapsed_time

def main():
    total_time = 0
    for _ in range(30):
        total_time += get("132.207.12.229:8080/?nom=Loic")
    print(total_time / 30)

main()
