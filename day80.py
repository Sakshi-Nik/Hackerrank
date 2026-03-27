# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
eng=set(map(int, input().split()))

m=input()
fre=set(map(int, input().split()))
print(len(eng^fre))