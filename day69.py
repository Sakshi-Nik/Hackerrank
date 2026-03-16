# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
shoe_size = list(map(int, input().split()))
stock=Counter(shoe_size)
customer = int(input())

money=0

for i in range(customer):
    size,price=map(int,input().split())
    
    if stock[size] > 0:
        money+=price
        stock[size]-=1
print(money)