n = int(input())

for i in range(n):
    n2 = int(input())
    nums = list(map(int, input().split()))
    print(max(nums), min(nums))