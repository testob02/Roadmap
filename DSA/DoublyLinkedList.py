class Node:
    def __init__(self,data,prev,next):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_beginning(self, data):
        node = Node(data,None,self.head)
        if self.head is None:
            self.head = node
            return
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        

        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(data,itr,None)
                return
            itr = itr.next

    def print_forward(self):
        if self.head is None:
            print('Doubly Linked List is empty')
            return

        dllist = ''
        itr = self.head
        while itr:
            dllist += f'{itr.data} ---> '
            itr = itr.next
        print(dllist)

    def print_backward(self):
        if self.head is None:
            print('Doubly Linked List is empty')
            return
        itr = self.get_last_node()

        dllist = ''
        while itr:
            dllist += f'{itr.data} ---> '
            itr = itr.prev
        print(f'Linked list in reverse: {dllist}')

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        
        return count
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data,itr,itr.next)
                if itr.next:
                    itr.next.prev = node
                itr.next = node 
                return
            itr = itr.next
            count +=1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                return
            count += 1
            itr = itr.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception('List is empty')
        
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        itr =  self.head.next
        while itr:
            if itr.data == data:
                if itr.prev is not None:
                    itr.prev.next = itr.next
                if itr.next is not None:
                    itr.next.prev = itr.prev
                return
            itr = itr.next
        print(f'{data} not found in the doubly linked list')
        
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception('List is empty')
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr,itr.next)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
        print(f'{data_after} not found in the doubly linked list')

dll = DoublyLinkedList()
dll.insert_values(['mangoes', 12, 'oranges',14,22,29,93])
dll.insert_after_value(12,11)
dll.print_forward()
dll.print_backward()
dll.remove_by_value('mangoes')
dll.print_forward()
dll.print_backward()