import math

def cala(x):
    return math.ceil(pow(x , 5/3) + math.tan(math.radians(x)))

def calb(x):
    return math.floor(pow(math.pi , 2 + math.atan(pow(math.radians(x), 2))))

# Main
x = float(input())
a = cala(x)
b = calb(x)
print(math.gcd(a , b))
