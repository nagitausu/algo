print("Enumerate subset")
n = 5
st = 11
subset = st
while True:
    print("{:05b}".format(subset))
    subset = (subset - 1) & st
    if subset == st:
        break

print("Enumerate superset")
n = 5
st = 11
superset = st
while True:
    print("{:05b}".format(superset))
    superset = (superset + 1) | st
    if superset >= (1 << n):
        break

print("Combination of k item")
n = 5
k = 3
comb = (1 << k) - 1
while comb < (1 << n):
    print("{:05b}".format(comb))
    x = comb & -comb
    y = comb + x
    comb = ((comb & ~y) // x >> 1) | y