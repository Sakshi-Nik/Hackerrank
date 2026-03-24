# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s,k=input().split()

words = list(permutations(sorted(s), int(k)))

for w in words:
    print("".join(w))