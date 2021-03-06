import math
def convert(n,b,t):
    if(n > 36 or t > 36):
        return "Base must be >= 36, in order for the result to be expressed with alphanumeric characters!"
    sum_in_ten = 0
    for i in range(len(b)):
        b[i] = ord(b[i]) - 55 if (ord(b[i]) > 65) else ord(b[i]) - 48
        sum_in_ten += b[i]*(n**(len(b) - i - 1))
    base = math.floor(math.log(sum_in_ten,t))
    new = ""
    for i in range(base,-1,-1):
        x = sum_in_ten // (t**base)
        if(x > 9):
            x = chr(x + 55)
        sum_in_ten %= (t**base)
        new += str(x)
        base -= 1
    return new

n = int(input("Enter base:"))
b = list(input("Enter number in said base:"))
t = int(input("Enter the new base:"))

print(convert(n,b,t))
