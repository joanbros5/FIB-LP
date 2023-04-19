def myLength(L):
    a = 0
    for i in L:
        a = a+1
    return a

def myMaximum(L):
    max = L[0]
    for i in L:
        if i > max:
            max = i
    return max

def average(L):
    avg = 0
    mida = 0
    for x in L:
        avg += x
        mida += 1
    return avg / mida

def buildPalindrome(L):
    mida = myLength(L)
    L2 = []
    for i in range (1, mida+1):
        L2 += [L[mida - i]]
    return L2 + L

# MAL
def remove(L1, L2):
    return [x for x in L1 if x not in L2]

def flatten(L):
    Res = []
    for elem in L:
        if elem != []:
            if isinstance(elem, list):
                Res += flatten(elem)
            else:
                Res.append(elem)
    return Res

def oddsNevens(L):
    LO = []
    LE = []
    for x in L:
        if x % 2:
            LO.append(x)
        else:
            LE.append(x)
    return (LO,LE)

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

def primeDivisors(n):
    return [x for x in range(1,n) if n % x == 0 and isPrime(x)]
