def con(a):
    d=[0,1]
    for i in range(a-2):
        d.append(d[-1]+d[-2])
    for i in d:
        yield i
b=int(input())
ad=con(b)
if b==0:
    print()
elif b==1:
    print(0)
else:
    print(",".join(map(str, ad)))
