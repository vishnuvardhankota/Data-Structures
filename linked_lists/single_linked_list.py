class Node:
    def __init__(self, data,next):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert(self,index,data):
        if index < 0 or index > self.get_size():
            raise Exception("Invalid index")
        
        if index == 0:
            node = Node(data,self.head)
            self.head = node
            return
        if index == self.get_size():
            self.append(data)
            return
        
        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                node = Node(data,itr.next)
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
                    self.head = self.head.next
                    return
            
                count = 0
                itr = self.head
                while itr.next:
                    if count == index - 1:
                        itr.next = itr.next.next
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
                            itr.next = itr.next.next
                    itr = itr.next
                if not found:
                    print("Value {} is not found to remove".format(data))
    
    def get_first_node(self):
        return self.head
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    
    def get_size(self):
        size = 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    def is_empty(self):
        return self.head is None

    def to_string(self):
        string = ""
        current_node = self.head
        while current_node is not None:
            string += str(current_node.data) + ("->" if current_node.next is not None else "")
            current_node = current_node.next
        return string
    
if __name__ == "__main__":

    single_linked_list = SingleLinkedList()
   
    single_linked_list.append(9)
    single_linked_list.insert(1,1)
    single_linked_list.insert_values([8,2,0,8,0,0,1,9,9,6,7])
    single_linked_list.pop()
    single_linked_list.pop(8)
    single_linked_list.remove(6)
   


    print("No.of nodes :- {}".format(single_linked_list.get_size()))
    print("Nodes are   :- {}".format(single_linked_list.to_string()))

    print(single_linked_list.get_first_node().data)
    print(single_linked_list.get_last_node().data)