def check(n):
    n = abs(n)  

    while n != 0:
        digit = n % 10

        if digit % 2 != 0:   
            print("Not valid")
            return

        n //= 10

    print("Valid")


x = int(input())
check(x)
