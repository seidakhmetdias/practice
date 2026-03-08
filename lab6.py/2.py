def even(x):
    if x % 2 == 0:
        return True
a=int(input())
b=list(map(int,input().split()))
res=list(filter(even,b))
print(len(res))
