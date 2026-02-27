def prime(a):
    for n in range(2, a + 1):
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
b=int(input())
for i in prime(b):
    print(i,end=" ")
    
        
