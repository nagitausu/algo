import sys
import math
input = sys.stdin.readline

class CumulativeSum2D:
    def __init__(self, field):
        self.h = len(field)
        self.w = len(field[0])
        self.h_offset = 2
        self.w_offset = 2
        self.field = field
        self.cumsum = [[0] * (self.w + self.w_offset * 2) for _ in range(self.h_offset)]
        for line in self.field:
            self.cumsum.append([0] * self.w_offset + line + [0] * self.w_offset)
        for i in range(self.h_offset):
            self.cumsum.append([0] * (self.w + self.w_offset * 2))
    
    def calc_horizontal_cumsum(self):
        # Calc horizontal cumlative sum
        for i in range(self.h_offset, self.h_offset + self.h):
            for j in range(self.w_offset, self.w_offset + self.w):
                self.cumsum[i][j] += self.cumsum[i][j-1]
        # Calc vertical cumlative sum
        for i in range(self.w_offset, self.w_offset + self.w):
            for j in range(self.h_offset, self.h_offset + self.h):
                self.cumsum[j][i] += self.cumsum[j-1][i]

    def calc_diagonal_cumsum(self):
        # Calc ul to dr
        for h in range(self.h_offset, self.h_offset + self.h):
            delta = 1
            while delta + h < self.h_offset * 2 + self.h and self.w_offset + delta < self.w_offset * 2 + self.w:
                self.cumsum[h + delta][self.w_offset + delta] += self.cumsum[h + delta-1][self.w_offset + delta-1]
                delta += 1
        for w in range(self.w_offset + 1, self.w_offset + self.w):
            delta = 1
            while delta + w < self.w_offset * 2 + self.w and self.h_offset + delta < self.h_offset * 2 + self.h:
                self.cumsum[self.h_offset + delta][w + delta] += self.cumsum[self.h_offset + delta - 1][w + delta - 1]
                delta += 1
        # Calc ur to dl
        for h in range(self.h_offset * 2 + self.h - 1, - 1, -1):
            delta = 1
            while delta + h < self.h_offset * 2 + self.h and self.w_offset * 2 + self.w - 1 - delta >= 0:
                self.cumsum[h + delta][self.w_offset * 2 + self.w - 1 - delta] += self.cumsum[h + delta - 1][self.w_offset * 2 + self.w - 1 - delta + 1]
                delta += 1
        for w in range(self.w_offset * 2 + self.w - 2, -1, -1):
            delta = 1
            while w - delta >= 0 and delta < self.h_offset * 2 + self.h:
                self.cumsum[delta][w - delta] += self.cumsum[delta - 1][w - delta + 1]
                delta += 1
    
    # Get horizontal sum in l <= x < r, u <= y < d
    # x: right, y: down
    def get_horizontal_sum(self, x1, y1, x2, y2):
        ret = self.cumsum[y2-1 + self.h_offset][x2-1 + self.w_offset]
        ret -= self.cumsum[y2-1 + self.h_offset][x1-1 + self.w_offset]
        ret -= self.cumsum[y1-1 + self.h_offset][x2-1 + self.w_offset]
        ret += self.cumsum[y1-1 + self.h_offset][x1-1 + self.w_offset]
        return ret
    
    # Get horizontal sum in x1 <= x <= x2, y1 <= y <= y2 
    def get_diagonal_sum(self, x1, y1, x2, y2):
        if ((x1 + y1) - (x2 + y2)) % 2 == 1:
            return None
        u2 = x2 + y2 
        v2 = x2 - y2
        u1 = x1 + (y1 - 2)
        v1 = x1 - (y1 - 2)
        x3 = (u2 + v1) // 2
        y3 = (u2 - v1) // 2
        x4 = (u1 + v2) // 2
        y4 = (u1 - v2) // 2
        ret = self.cumsum[y2 + self.h_offset][x2 + self.w_offset]
        ret -= self.cumsum[y3 + self.h_offset][x3 + self.w_offset]
        ret -= self.cumsum[y4 + self.h_offset][x4 + self.w_offset]
        ret += self.cumsum[y1-2 + self.h_offset][x1 + self.w_offset]
        return ret
        

    def print(self):
        print("h:", self.h, "w:", self.w)
        for i in range(self.h_offset, self.h_offset + self.h):
            print(self.cumsum[i][self.w_offset:self.w_offset + self.w])

if __name__ == "__main__":
    field = [[1, 1, 1],
             [1, 1, 1],
             [0, 0, 1],
             [1, 1, 1]]
    cs1 = CumulativeSum2D(field)
    cs1.calc_horizontal_cumsum()
    cs1.print()
    print(cs1.get_horizontal_sum(0, 0, 4, 4))

    cs2 = CumulativeSum2D(field)
    cs2.calc_diagonal_cumsum()
    cs2.print()
    print(cs2.get_diagonal_sum(0, 0, 1, 3))