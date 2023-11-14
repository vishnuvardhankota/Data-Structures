class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,itr,None)

    def insert(self,index,data):
        if index < 0 or index > self.get_size():
            raise Exception("Invalid index")
        
        if index == 0:
            node = Node(data,None ,self.head)
            self.head.prev = node
            self.head = node
            return
        if index == self.get_size():
            self.append(data)
            return
        
        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                node = Node(data,itr,itr.next)
                itr.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_values(self,list):
        for i in list:
            self.append(i)


    def pop(self, index=None):
        if self.is_empty():
            raise Exception("Linked List is Empty")
        else:
            if index is not None:
                if index < 0 or index >= self.get_size():
                    raise Exception("Invalid index")
                if index == 0:
                    self.head.next.prev = None
                    self.head = self.head.next
                    return
            
                count = 0
                itr = self.head
                while itr.next:
                    if count == index - 1:
                        itr.next = itr.next.next
                        itr.next.prev = itr
                        break
        
                    itr = itr.next
                    count += 1
            else:
                if self.get_size() > 1:
                    itr = self.head
                    while itr.next:
                        if itr.next.next is None:
                            itr.next = None
                            break
                        itr = itr.next
                else:
                    self.head = None

    def remove(self,data):
        if self.is_empty():
            raise Exception("Linked List is Empty")
        else:
            if self.head.data == data:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                found = False
                itr = self.head
                while itr.next:
                    if itr.next.data == data:
                        found = True
                        if itr.next.next is None:
                            itr.next = None
                            break
                        else:
                            itr.next.next.prev = itr
                            itr.next = itr.next.next
                    itr = itr.next
                if not found:
                    print("Value {} is not found to remove".format(data))
    

    def get_size(self):
        size = 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    def is_empty(self):
        return self.head is None
    
    def get_first_node(self):
        return self.head
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def to_string(self):
        string = ""
        current_node = self.head
        while current_node is not None:
            string += str(current_node.data) + ("->" if current_node.next is not None else "")
            current_node = current_node.next
        return string
    
    def reverse_string(self):
        string = ""
        current_node = self.get_last_node()
        while current_node is not None:
            string += str(current_node.data) + ("->" if current_node.prev is not None else "")
            current_node = current_node.prev
            
        return string
    
if __name__ == "__main__":

    double_linked_list = DoubleLinkedList()
   
    double_linked_list.append(9)
    double_linked_list.append(8)
    double_linked_list.append(7)
    double_linked_list.append(6)
    double_linked_list.append(5)
    double_linked_list.insert(5,4)
    double_linked_list.insert_values([3,2])
    print("Nodes are   :- {}".format(double_linked_list.to_string()))
    print("Nodes are   :- {}".format(double_linked_list.reverse_string()))
    print("last element removed")
    double_linked_list.pop()
    print("Nodes are   :- {}".format(double_linked_list.to_string()))
    print("Nodes are   :- {}".format(double_linked_list.reverse_string()))
    print("element removed at 3rd index")
    double_linked_list.pop(3)
    print("Nodes are   :- {}".format(double_linked_list.to_string()))
    print("Nodes are   :- {}".format(double_linked_list.reverse_string()))
    print("removed element of value 8")
    double_linked_list.remove(8)
    print("Nodes are   :- {}".format(double_linked_list.to_string()))
    print("Nodes are   :- {}".format(double_linked_list.reverse_string()))



