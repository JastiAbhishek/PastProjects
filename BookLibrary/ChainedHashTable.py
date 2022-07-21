from Interfaces import Set
from DLList import DLList
import numpy as np

class ChainedHashTable(Set):
    class Node() :
        def __init__(self, key, value) :
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList) :
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=np.object)
        for i in range(n):
            t[i] = self.dtype()
        return t


    def _hash(self, key : int) -> int :
        return self.z * hash(key) % (2**self.w) >> (self.w - self.d) 

    def size(self) -> int:
        return self.n
        
    def find(self, key : object) -> object :
        # todo
        # --
        h = self._hash(key)
        for i in range(0,(self.t[h].size())):
            if self.t[h][i].key == key:
                return self.t[h][i].value
        return None
        # --
    
        
    def add(self, key : object, value : object) :
        # todo
        # -- 
        if self.find(key) != None:
            return False
        if(self.n == len(self.t)):
            self.resize()        
        hashValue = self._hash(key)
        self.t[hashValue].append(self.Node(key, value))
        self.n = self.n+1
        # -- 


    def remove(self, key : int)  -> object:
        # todo
        # -- 
        
        if self.find(key) == None:
            return None
        hashValue = self._hash(key)
        list = self.t[hashValue]
        var = None
        for i in range(0, list.size()):
            if list[i].key == key:
                var = self.t[hashValue].remove(i)
                self.n = self.n-1
        if len(self.t) > 3*self.n:
            self.resize()
        return var
        # -- 
    
    def resize(self):
        # todo
        # --
        if self.n == 2**self.d:
            self.d = self.d+1
        elif 2**self.d >= 3*(self.n):
            self.d = self.d-1
        var = self.alloc_table(2**self.d)
        for i in range(0, len(self.t), 1):
            for j in range(0, self.t[i].size(), 1):
                current_element = self.t[i][j]
                h = self._hash(current_element.key)
                var[h].append(current_element)
        self.t = var
        # -- 


    def __str__(self):
        s = "\n"
        for i in range(len(self.t)):
            s += str(i) + " : "
            for j in range(self.t[i].size()):
                k = self.t[i][j]  # jth node at ith list
                s += "(" + str(k.key) + ", " + str(k.value) + "); "

            s += "\n"
        return s


# a = ChainedHashTable()
# a.add(1,"s")
# a.add(2,"e")
# a.add(3,"s")
# a.add(4,"e")
# a.add(5,"s")
# a.add(6,"e")
# a.add(7,"s")
# a.add(8,"e")
# a.add(9,"s")
# a.add(10,"e")
# print(a)
# print(a.remove(6))
# print(a)

