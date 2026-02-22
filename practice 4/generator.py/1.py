def squer(a):
    for i in range(a):
        yield i ** 2
b=int(input())
for i in squer(b):
    print(i,end=" ")