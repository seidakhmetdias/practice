def even(n):
    for i in range(2, n + 1, 2):
        yield i
b=int(input())
for i in even(b):
    print(i,end=" ")