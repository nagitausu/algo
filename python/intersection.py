ax, ay, bx, by = [int(item) for item in input().split()]
n = int(input())
xy = [[int(item) for item in input().split()] for _ in range(n)]
xy += [xy[0]]

def is_cross(ax, ay, bx, by, cx, cy, dx, dy):
    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)
    return tc * td < 0 and ta * tb < 0

ans = 0
for i in range(n):
    cx, cy = xy[i]
    dx, dy = xy[i+1]
    if is_cross(ax, ay, bx, by, cx, cy, dx, dy):
        ans += 1

print(ans // 2 + 1)
