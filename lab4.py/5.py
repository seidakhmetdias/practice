def con(a):
    for i in range(a,-1,-1):
        yield i
b=int(input())
for i in con(b):
    print(i)
