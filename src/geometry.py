import math
eps = 1e-12

def intersection_points(circle0, circle1):
    x0, y0, r0 = circle0
    x1, y1, r1 = circle1
    d = math.hypot(x0 - x1, y0 - y1)
    if d > r0 + r1 or d < abs(r0 - r1):
        return []
    ret = []
    if r0 + r1 == d:
        a = r0
        h = 0.0
    else:
        a = (r0**2 - r1**2 + d**2) / (2.0 * d)
        h = math.sqrt(r0**2 - a**2)
    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d
    x3 = x2 + h * (y1 - y0) / d
    y3 = y2 - h * (x1 - x0) / d
    ret.append((x3, y3))
    if h == 0:
        return ret
    x4 = x2 - h * (y1 - y0) / d
    y4 = y2 + h * (x1 - x0) / d
    ret.append((x4, y4))
    return ret

def is_cross(segment0, segment1):
    ax, ay, bx, by = segment0
    cx, cy, dx, dy = segment1
    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)
    return tc * td < 0 and ta * tb < 0