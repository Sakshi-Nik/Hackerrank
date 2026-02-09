M = int(input())
m = set(map(int,input().split()))
N=int(input())
n=set(map(int,input().split()))

result=m.symmetric_difference(n)
r=sorted(result)

for i in r:
    print(i)