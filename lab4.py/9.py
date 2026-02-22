def power(a):
    for i in range(a+1):
        yield 2**i
b=int(input())
for i in power(b):
    print(i,end=" ")