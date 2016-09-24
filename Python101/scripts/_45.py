import threading
from queue import Queue
import time


print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(2)

    with print_lock:
        print(threading.current_thread().name, worker)


def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()


q = Queue()

for worker in range(20):
    q.put(worker)

q.join()


for x in range(20):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()



print('Entire job took: ', time.time() - start)
