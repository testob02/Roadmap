class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinarySearchTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self,val):
        if self.data == val:
            return True
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements +=self.right.in_order_traversal()
             
        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def calculate_sum(self):
        if self.left:
            sums_left = self.left.calculate_sum()
        else:
            sums_left = 0
        
        if self.right:
            sums_right = self.right.calculate_sum()
        else:
            sums_right = 0
        
        return self.data + sums_left + sums_right
            
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        elif val == self.data:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
        
            maxi = self.left.find_max()
            self.data = maxi
            self.left.delete(maxi)

        return self

countries = [15,12,7,14,27,20,88,23]
country_tree = BinarySearchTreeNode(countries[0])
for i in countries[1:]:
    country_tree.add_child(i)
print(country_tree.in_order_traversal())
print(country_tree.pre_order_traversal())
print(country_tree.post_order_traversal())
print(country_tree.calculate_sum())
print(country_tree.find_max())
print(country_tree.find_min())
print(country_tree.search(27))
print(country_tree.search(278))
country_tree.delete(7)
print(country_tree.in_order_traversal())
