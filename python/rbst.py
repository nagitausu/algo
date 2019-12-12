import random
from random import randint
random.seed()

class RandomizedBinarySearchTree:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.lch = None
            self.rch = None
            self.cnt = val is not None 
        
        def __bool__(self):
            return self.val is not None

    def __init__(self):
        self.tree = self.Node()
    
    def __str__(self):
        arr, max_depth = self.dump(self.tree)
        msg = " ".join([str(item) for item in arr]) + "\n"
        msg += "max depth:" + str(max_depth)
        return msg

    def dump(self, t):
        ret = []
        ret.append(t.val)
        ld = rd = 0
        if t.lch:
            larr, ld = self.dump(t.lch)
            ret.extend(larr)
        if t.rch:
            rarr, rd = self.dump(t.rch)
            ret.extend(rarr)
        return ret, max(ld, rd) + 1 

    def count(self, t):
        return t.cnt if t else 0

    def update(self, t):
        t.cnt = self.count(t.lch) + self.count(t.rch) + 1
        return t

    def merge(self, left, right):
        if not left or not right:
            return left or right
        if randint(1, left.cnt + right.cnt) <= left.cnt:
            left.rch = self.merge(left.rch, right)
            return self.update(left)
        else:
            right.lch = self.merge(left, right.lch)
            return self.update(right)

    def split(self, t, k):
        if not t: 
            return t, t 
        if k <= self.count(t.lch):
            s1, s2 = self.split(t.lch, k)
            t.lch = s2
            return s1, self.update(t)
        else:
            s1, s2 = self.split(t.rch, k - self.count(t.lch) - 1)
            t.rch = s1
            return self.update(t), s2

    def insert(self, t, k, v):
        new_node = self.Node(v)
        s1, s2 = self.split(t, k)
        merged = self.merge(s1, new_node)
        self.update(merged)
        merged = self.merge(merged, s2)
        return self.update(merged)
    
    def insert_key(self, v):
        # TODO: implement bisect_left and enable sorted insert_key
        self.tree = self.insert(self.tree, 0, v)

if __name__ == "__main__":
    RBST = RandomizedBinarySearchTree()
    for i in range(100):
        RBST.insert_key(i)
    print(RBST)