a=int(input())
b=list(map(int,input().split()))    
c=list(map(int,input().split()))
sum=0
for x,y in zip(b,c):
    sum+=x*y
print(sum)