class reverse:
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return self.string[::-1]
a = input()
print(reverse(a))

    