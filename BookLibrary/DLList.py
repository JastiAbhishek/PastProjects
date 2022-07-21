from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        # todo
        # --
        if i < 0 or i > self.n:
            return None
        if i < self.n/2:
            temp = self.dummy.next
            for j in range(0, i, 1):
                temp = temp.next 
        else:
            temp = self.dummy
            for j in range(0, self.n-i, 1):
                temp = temp.prev
        return temp
        # -- 
        
    def get(self, i) -> np.object:
        # todo
        # --
        if i < 0 or i >= self.n:
            raise IndexError
        return self.get_node(i).x
        # -- 

    def set(self, i : int, x : np.object) -> np.object:
        # todo
        # --
        if i < 0 or i >= self.n:
            raise IndexError
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y        
        # -- 

    def add_before(self, w : Node, x : np.object) -> Node:
        # todo
        # --
        if w is None:
            raise ValueError
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n = self.n+1
        return u
        # -- 
            
    def add(self, i : int, x : np.object)  :
        # todo
        # --
        if i < 0 or i > self.n:
            raise IndexError
        return self.add_before(self.get_node(i), x)
        # -- 

    def _remove(self, w : Node) :
        # todo
        # --
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n = self.n-1
        # --
    
    def remove(self, i :int) :
        if i < 0 or i >= self.n:  raise IndexError
        w = self.get_node(i)
        self._remove(w)
        return w


    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        # todo
        # --        
        f = self.dummy
        b = self.dummy
        for i in range(0, self.n//2, 1):
            f = f.next
            b = b.prev
            if(f.x != b.x):
                return False
        return True   
        # -- 
    
    def reverse(self):
        h = self.dummy.next
        t = self.dummy.prev
        prev = self.dummy
        current = self.dummy.next
        curr_next = current.next
        while(current != self.dummy):
            current.next = prev
            current.prev = curr_next
            prev = current
            current = curr_next
            curr_next = curr_next.next
        self.dummy.next = t
        self.dummy.prev = h


    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
