def c(b,a):
    for i in range(a):
        for j in range(len(b)):
            yield b[j]
b=input().split()
a=int(input())
for i in c(b,a):
    print(i,end=" ")