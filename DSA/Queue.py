from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.appendleft(data)

    def dequeue(self):
        return self.queue.pop()
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

#-----------------------------------------------------------------

food_order_queue = Queue()
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

def place_orders(orders):
    for order in orders:
        print(f'Placing orders for: {order}')
        food_order_queue.enqueue(order)
        time.sleep(0.5)

def serve_orders():
    while food_order_queue.size != 0:
        if food_order_queue.size() > 0:
            order = food_order_queue.dequeue()
            print(f'Serving: {order}')
            time.sleep(2)
        else:
            break

place = threading.Thread(target=place_orders,args=(orders,))
serve = threading.Thread(target=serve_orders)

place.start()
time.sleep(1)
serve.start()

#-----------------------------------------------------------------

binary_number_queue = Queue()

def generate_sequence(n):
    binary_number_queue.enqueue('1')
    i = 1
    while i <= n:
        x = binary_number_queue.dequeue()
        print(x)
        binary_number_queue.enqueue(f'{x}0')
        binary_number_queue.enqueue(f'{x}1')
        i += 1

generate_sequence(10)




    
