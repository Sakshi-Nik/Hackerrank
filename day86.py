# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

item_records = OrderedDict()
n = int(input())

for _ in range(n):
    
    data = input().split()
      
    item_name = " ".join(data[:-1])
    
    price = int(data[-1])
    if item_name in item_records:
        item_records[item_name] += price
    else:
        item_records[item_name] = price

for item, net_price in item_records.items():
    print(f"{item} {net_price}")
