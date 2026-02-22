def con(a):
    for i in range(0,a+1,12):
        yield i
b=int(input())
for i in con(b):
    print(i,end=" ")