import socket
import threading
from queue import Queue
import time

print_lock = threading.Lock()
target = 'pythonprogramming.net'

server_ip = socket.gethostbyname(target)
print(server_ip)

def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # print(port)
        con = s.connect((target, port))
        with print_lock:
            print('Port', port, 'is open!')
        con.close()
    except:
        pass


q = Queue()

def threader():
    while True:
        worker = q.get()
        pscan(worker)
        q.task_done()


for x in range(50):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
start = time.time()
for worker in range(1, 1000):
    q.put(worker)

q.join()
print('Entire time cost', time.time() - start)
