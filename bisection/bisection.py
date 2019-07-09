def function(x):
    return (x*3 - x*2 - 10*x - 8)

def df(x):
    return (3*x)**2 - (2*x) - 10
a = float(input("Enter begining of interval: "))
b = float(input("Enter end of interval: "))
p = float(input("Enter p of method: "))

def newton(x):
    h = function(x)/df(x)
    while abs(h) >= p:
        h = function(x)/df(x)
        #x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
    print("Root: ", x)

def bisection(a,b,canCount):
    canCount = True
    if(function(a) * function(b) > 0):
        print("Function has same signs at ends of interval")
        canCount = False
    while(abs(a - b) > p):
        middle = (a + b) / 2
        if(function(a) * function(middle) < 0):
            b = middle
        else:
            a = middle

    print("Root : ", middle)

bisection(a,b,p)
newton(a)