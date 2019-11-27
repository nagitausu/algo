from collections import deque

class SlidingWindowAggregation:
    def __init__(self, a=None):
        # Operator
        self.op = lambda a, b : max(a, b)
        self.back_deq = deque()
        self.front_deq = deque()
        if a:
            self.initialize(a)

    def initialize(self, a):
        s = x = a.pop()
        self.front_deq.appendleft((x, x))
        for x in a[::-1]:
            s = self.op(x, s)
            self.front_deq.appendleft((x, s))

    def fold(self):
        if not self.front_deq:
            return self.back_deq[-1][1]
        if not self.back_deq:
            return self.front_deq[0][1]
        else:
            return self.op(self.front_deq[0][1], self.back_deq[-1][1])

    def push(self, x):
        if not self.back_deq:
            self.back_deq.append((x, x))
        else:
            self.back_deq.append((x, self.op(x, self.back_deq[-1][1])))

    def pop(self):
        if not self.front_deq:
            # Reorder
            x, _ = self.back_deq.pop()
            self.front_deq.appendleft((x, x))
            s = x
            while self.back_deq:
                x, _ = self.back_deq.pop()
                s = self.op(s, x)
                self.front_deq.appendleft((x, self.op(x, s)))
        self.front_deq.popleft()
    

if __name__ == "__main__":
    print("fold front : back")
    a = [2, 20, 10]
    SWAG = SlidingWindowAggregation(a)
    print(SWAG.fold(), list(SWAG.front_deq), ":", list(SWAG.back_deq)) 
    SWAG.push(14)
    print(SWAG.fold(), list(SWAG.front_deq), ":", list(SWAG.back_deq)) 
    SWAG.pop()
    print(SWAG.fold(), list(SWAG.front_deq), ":", list(SWAG.back_deq)) 
    SWAG.push(7)
    print(SWAG.fold(), list(SWAG.front_deq), ":", list(SWAG.back_deq)) 
    SWAG.push(8)
    print(SWAG.fold(), list(SWAG.front_deq), ":", list(SWAG.back_deq)) 
    SWAG.pop()
    print(SWAG.fold(), list(SWAG.front_deq), ":", list(SWAG.back_deq)) 
    SWAG.pop()
    print(SWAG.fold(), list(SWAG.front_deq), ":", list(SWAG.back_deq)) 
    SWAG.pop()
    print(SWAG.fold(), list(SWAG.front_deq), ":", list(SWAG.back_deq)) 
    SWAG.push(4)
    print(SWAG.fold(), list(SWAG.front_deq), ":", list(SWAG.back_deq)) 