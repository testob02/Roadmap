class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node    
    
    def insert_at_end(self,data):
        node = Node(data, None)
        if self.head is None:
            self.insert_at_beginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def insert_values(self, data_list):
        self.head = None    
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0  or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head 
        while count < index-1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0 :
            self.insert_at_beginning(data)
            return
        
        if index == self.get_length()-1:
            self.insert_at_end(data)
            return
        
        count = 0
        itr = self.head
        while count < index-1:
            itr = itr.next
            count += 1
        node = Node(data, itr.next)
        itr.next = node

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        print(f'{data} not found in the linked list')

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception('List is empty')

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                return
            itr = itr.next
        print(f'{data_after} not found in the linked list')

    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        llist = ''
        itr = self.head
        while itr:
            llist += str(itr.data) +' --> '
            itr = itr.next
        print(llist)

ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango","apple")
ll.print()
ll.remove_by_value("orange")
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()