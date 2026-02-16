def a(b,c):
    if b<c:
        print("Insufficient Funds")
    else:
        print(b-c)
b,c=map(int,input().split())
