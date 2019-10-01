## Inverse Mobius Transform
# Cumlative sum of subset
f = [1] * 8 
d = 3
for i in range(d):
    for j in range(1 << d):
        if j & (1 << i):
            f[j] += f[j ^ (1 << i)]
print(f)

# Cumlative sum of superset
f = [1] * 8 
d = 3
for i in range(d):
    for j in range(1 << d):
        if not j & (1 << i):
            f[j] += f[j | (1 << i)]
print(f)

# Mobius Transform
# Diff of subset
f = [1, 2, 2, 4, 2 ,4, 4, 8] 
d = 3
for i in range(d):
    for j in range(1 << d):
        if j & (1 << i):
            f[j] -= f[j ^ (1 << i)]
print(f)

# Diff of superset
f = [8, 4, 4, 2, 4, 2, 2, 1] 
d = 3
for i in range(d):
    for j in range(1 << d):
        if not j & (1 << i):
            f[j] -= f[j | (1 << i)]
print(f)