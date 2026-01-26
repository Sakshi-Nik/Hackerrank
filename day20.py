a=set()

n1 = int(input())
english = set(map(int, input().split()))


n2 = int(input())
french = set(map(int, input().split()))


only_english = english.difference(french)


print(len(only_english))
