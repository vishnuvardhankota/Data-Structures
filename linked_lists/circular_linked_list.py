class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def get_size(self):
        if self.head is None:
            return 0
        else:
            size = 1
            current_node = self.head
            while current_node != self.tail:
                size += 1
                current_node = current_node.next
            return size

    def get_at(self, index):
        if index < 0 or index >= self.get_size():
            raise IndexError
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            return current_node.data

    def set_at(self, index, data):
        if index < 0 or index >= self.get_size():
            raise IndexError
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            current_node.data = data

    def remove(self, index):
        if index < 0 or index >= self.get_size():
            raise IndexError
        else:
            if index == 0:
                self.head = self.head.next
                self.tail = self.tail.next
            else:
                current_node = self.head
                for _ in range(index - 1):
                    current_node = current_node.next
                current_node.next = current_node.next.next

    def to_string(self):
        if self.head is None:
            return ""
        else:
            string = ""
            current_node = self.head
            while current_node != self.tail:
                string += str(current_node.data) + " "
                current_node = current_node.next
            string += str(current_node.data)
            return string


def main():
    circular_linked_list = CircularLinkedList()
    circular_linked_list.add(1)
    circular_linked_list.add(2)
    circular_linked_list.add(3)
    print(circular_linked_list.to_string())
    print(circular_linked_list.get_size())
    print(circular_linked_list.get_at(1))
    circular_linked_list.set_at(1, 5)
    print(circular_linked_list.to_string())
    circular_linked_list.remove(1)
    print(circular_linked_list.to_string())


if __name__ == "__main__":
    main()