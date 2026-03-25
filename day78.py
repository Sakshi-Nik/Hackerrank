# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations


s, n = input().split()
n = int(n)


chars = sorted(s)


for r in range(1, n + 1):
    for i in combinations(chars, r):
        print("".join(i))

