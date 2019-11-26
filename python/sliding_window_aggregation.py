from collections import deque

class SlidingWindowAggregation:
    def __init__(self, a=None):
        self.back_deque = deque()
        self.front_deque = deque()
        if a:
            self.initialize(a)

    def initialize(self, a):
        s = x = a.pop()
        self.front_deque.appendleft((x, x))
        for x in a[::-1]:
            s = min(x, s)
            self.front_deque.appendleft((x, s))

    def query(self):
        if not self.front_deque:
            return self.back_deque[-1][1]
        if not self.back_deque:
            return self.front_deque[0][1]
        else:
            return min(self.front_deque[0][1], self.back_deque[-1][1])

    def push(self, x):
        if not self.back_deque:
            self.back_deque.append((x, x))
        else:
            self.back_deque.append((x, min(x, self.back_deque[-1][1])))

    def pop(self):
        if not self.front_deque:
            # Reorder
            x, _ = self.back_deque.pop()
            self.front_deque.appendleft((x, x))
            s = x
            while self.back_deque:
                x, _ = self.back_deque.pop()
                s = min(s, x)
                self.front_deque.appendleft((x, min(x, s)))
        self.front_deque.popleft()

if __name__ == "__main__":
    print("query front : back")
    a = [2, 20, 10]
    SWAG = SlidingWindowAggregation(a)
    print(SWAG.query(), list(SWAG.front_deque), ":", list(SWAG.back_deque)) 
    SWAG.push(14)
    print(SWAG.query(), list(SWAG.front_deque), ":", list(SWAG.back_deque)) 
    SWAG.pop()
    print(SWAG.query(), list(SWAG.front_deque), ":", list(SWAG.back_deque)) 
    SWAG.push(7)
    print(SWAG.query(), list(SWAG.front_deque), ":", list(SWAG.back_deque)) 
    SWAG.push(8)
    print(SWAG.query(), list(SWAG.front_deque), ":", list(SWAG.back_deque)) 
    SWAG.pop()
    print(SWAG.query(), list(SWAG.front_deque), ":", list(SWAG.back_deque)) 
    SWAG.pop()
    print(SWAG.query(), list(SWAG.front_deque), ":", list(SWAG.back_deque)) 
    SWAG.pop()
    print(SWAG.query(), list(SWAG.front_deque), ":", list(SWAG.back_deque)) 
    SWAG.push(4)
    print(SWAG.query(), list(SWAG.front_deque), ":", list(SWAG.back_deque)) 