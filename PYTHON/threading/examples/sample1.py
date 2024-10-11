import threading
import time

def worker():
    time.sleep(5)

if __name__ == "__main__":
    threads = []
    for i in range(20):
        thread = threading.Thread(target=worker)
        thread.name=f"thread {i}"
        print(f"run thread {i}")
        thread.start()

        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Finished")

