t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ", n-1)))
    print(sum(a))