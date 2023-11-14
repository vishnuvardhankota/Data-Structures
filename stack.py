# Importing Deque instead of using list for better performance
from collections import deque

class MyStack:
    def __init__(self):
        self.container = deque()

    # Append a value at last
    def push(self,data):
        self.container.append(data)

    # remave a value from last
    def pop(self):
        return self.container.pop()

    # alculate no.of values in a stack
    def count(self):
        return len(self.container)
    

if __name__ == '__main__':
    st = MyStack()
    st.push(5)
    st.push(68)
    st.push(15)
    print(st.container)
    print(st.count())
    st.pop()
    print(st.container)
    print(st.count())
