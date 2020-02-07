print("Multiple comparison in 1 if")
a = [1, 2, 3, 4, 5, 6]
for item in a:
    if 2 <= item <= 4:
        print(item, end=" ")
print("")

print("Dic comprehension")
a = ["apple", "banana", "cake", "diamond"]
dic = {i:a[i] for i in range(4)}
print(dic)

print("Filtered list comprehension")
a = [i for i in range(10) if 10 <= i * i < 100]
print(a)

print("Multi-for list comprehension")
a = [i for j in range(5) for i in range(j)]
print(a)

print("String conversion with str.translate")
table = str.maketrans("ab", "cd", "e")
a = "abcdef".translate(table)
print(a)

from math import hypot
print("Euclidian dist with hypot")
dist = hypot(1, 1)
print(dist)

print("Get col easily")
a = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
print("row")
for row in a:
    print(row)
print("col")
for col in zip(*a):
    print(list(col))
