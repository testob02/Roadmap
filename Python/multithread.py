import threading
import time

def meh(i):
    print(f'Sleeping {i}')
    time.sleep(3)
    print(f'Done Sleeping {i}')

for i in range(10):
    t = threading.Thread(target=meh,args=(i,))
    t.start()
    print(f'\nActive threads: {threading.active_count()}')
