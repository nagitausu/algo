def binary_search(a, key):
    lft = -1
    rgt = len(a)

    while(rgt - lft > 1):
        mid = lft + (rgt - lft) // 2
        if a[mid] >= key:
            rgt = mid
        else:
            lft = mid
    return rgt

if __name__ == "__main__":
    a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]
    print(binary_search(a, 52))
