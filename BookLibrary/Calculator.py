import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)
        
    def matched_expression(self, s : str) -> bool :
        # todo
        # -- 
        stack = ArrayStack.ArrayStack()
        for i in s:
            if i =='(' :
                stack.push('(')
            elif i == ')':
                try: 
                    stack.pop()  
                except IndexError: 
                    return False
        size = stack.size()
        if size == 0:
            return True
        else:
            return False

        # --
        pass 

    def build_parse_tree(self, exp : str) ->str:
        # todo
        pass 

    def _evaluate(self, root):
        op = { '+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        # todo
        pass 

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
        
        
