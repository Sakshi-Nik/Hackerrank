# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
k = input()

index = S.find(k)

if index == -1:
    print((-1, -1))
else:
    while index != -1:
        print((index, index + len(k) - 1))
        
        index = S.find(k, index + 1)
