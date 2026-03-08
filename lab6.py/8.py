n = int(input())
nums = list(map(int, input().split()))

unique_nums = sorted(set(nums))
print(*unique_nums)