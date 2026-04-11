# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
num = input().split() 


ans = all(int(i) > 0 for i in num) and any(i == i[::-1] for i in num)

print(ans)
