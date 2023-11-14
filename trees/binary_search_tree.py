class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, newdata):
        if newdata == self.data:
            return
        if newdata < self.data:
            if self.left:
                self.left.add_child(newdata)
            else:
                self.left = BinarySearchTreeNode(newdata)
        else:
            if self.right:
                self.right.add_child(newdata)
            else:
                self.right = BinarySearchTreeNode(newdata)

    def in_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = []
        # visit base node
        elements.append(self.data)
        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()
        # visit base node
        elements.append(self.data)

        return elements
    
    def search_value(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search_value(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search_value(value)
            else:
                return False
        
    
    def delete_value(self,value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_value(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_value(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_value(min_val)
        
        return self
    
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
        sum = 0
        elements = self.in_order_traversal()
        for i in elements:
            sum += i
        return sum


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [15,23,27,12,7,20,88,14]
    tree = build_tree(numbers)
    print(tree.in_order_traversal())
    # print(tree.pre_order_traversal())
    # print(tree.post_order_traversal())
    print(tree.find_min())
    # print(tree.find_max())
    # print(tree.calculate_sum())
    tree.delete_value(40)
    print(tree.in_order_traversal())
