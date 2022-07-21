from pickletools import TAKEN_FROM_ARGUMENT1
import numpy as np
import random 
from ArrayQueue import ArrayQueue

class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)
            

    def remove(self) -> np.object :
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # --
        #we want to reassign to change randomly selected index to be j
        #swap random i with position

        #target1, target2 = target2, target1

        #same as

        # holder = target1
        # target1 = target2
        # target2 = holder
        if self.n == 0: raise IndexError
        n = (random.randint(0, self.n-1))
        i = self.j+n % len(self.a)
        var = self.a[self.j]
        self.a[self.j] = self.a[i]
        self.a[i] = var
        x = ArrayQueue.remove(self)
        return x
        # --
        #pass 
     




