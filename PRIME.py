import math
def checkprime(n):
    for i in range(2, n):
        if n % 2 == 0:
            return False
    else:
        return True
def primeproduct(x):
    p = []
    if x >=0:
        for i in range(2, x):
            if x % i == 0:
                p.append(i)
        #print(len(p))
        if len(p) <= 2:
            if checkprime(p[0]) and checkprime(p[1]):
                if p[0] * p[1] == x:
                    return True
                else:
                    return False
            else:
                return False
        else:
            print("here")
            return False
    else:
        return False


print(primeproduct(-202))
