# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement
s,k=input().split()
k=int(k)

s=sorted(s)
comb = combinations_with_replacement(s,k)

for c in comb:
    print(''.join(c))