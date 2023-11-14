# Importing Deque instead of using list for better performance
from collections import deque

class MyQueue:
    def __init__(self):
        self.container = deque()

    # Appending a value in queue
    def push(self,data):
        self.container.insert(0,data)

    # Removing a first inserted value in queue
    def pop(self):
        return self.container.pop()

    # alculate no.of values in a stack
    def count(self):
        return len(self.container)
    

if __name__ == '__main__':
    st = MyQueue()
    st.push(5)
    st.push(68)
    st.push(15)
    print(st.count())
    print(st.container)
    st.pop()
    print(st.count())
    print(st.container)
