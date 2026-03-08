a=int(input())
sum=0
b=list(map(int,input().split()))
for i in b:
    sum+=i**2
print(sum)