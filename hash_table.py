class MyHashTable:
    def __init__(self):
        self.size = 10
        self.array = [[] for i in range(self.size)]

    def get_hash(self, key):
        hv = 0
        for char in key:
            hv += ord(char)
        index = hv % self.size
        return index
    
    def __getitem__(self,key):
        index = self.get_hash(key)
        for kv in self.array[index]:
            if kv[0] == key:
                return kv[1]
    
    def __setitem__(self,key,value):
        index = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.array[index]):
            if len(element)==2 and element[0] == key:
                self.array[index][idx] = (key,value)
                found = True
        if not found:
            self.array[index].append((key,value))
    
    def __delitem__(self, key):
        index = self.get_hash(key)
        for idx, kv in enumerate(self.arr[index]):
            if kv[0] == key:
                print("del",index)
                del self.array[index][idx]

if __name__ == '__main__':
    ht = MyHashTable()
    ht['sorravl'] = 23
    ht['raghu'] = 19
    ht['sri'] = 18
    print(ht['sorravl'])
    # del ht['sri']
    print(ht.array)
