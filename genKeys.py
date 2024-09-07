'''
Andrew Rodriguez
CSCI 531
Dr. Ryutov
Assignment 3
'''

import sys
import os

import random

e = 65537

def checkPrime(n, k):
    def decompose(n):
        s = 0
        d = n - 1
        while d % 2 == 0:
            d //= 2
            s += 1
        return s, d

    if n == 2:
        return "prime"
    if n % 2 == 0:
        return "composite"

    s, d = decompose(n)

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return "composite"

    return "prime"

def genPrimes(x):
    count = 0
    primes = []
    while count < 2:

        bits = random.getrandbits(x)
        if checkPrime(bits, 40) == "prime":
            count += 1
            primes.append(bits)

    return primes


primes = genPrimes(1024)

def findN(primes):
    return primes[0] * primes[1]

def findEulersTotient(primes):
    return (primes[0] - 1) * (primes[1] - 1)

def findD(e):


    phiN = findEulersTotient(primes)



    def EUA(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = EUA(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    def modInverse(e, phiN):
        gcd, x, i = EUA(e, phiN)
        if gcd == 1:
            return x % phiN
        return None

    d = modInverse(e, phiN)
    return d

def genKeys():

    n = findN(primes)
    d = findD(e)


    
    publicPair = str(n) + ", " + str(e)
    privatePair = str(n) + ", " + str(d)


    return publicPair, privatePair


def writeKeys(name):

    

    public, private = genKeys()
    with open(name+".pub", "w") as f:
        f.write(public)
    with open(name+".prv", "w") as f:
        f.write(private)
    print("Keys written to", name+".pub and", name+".prv")

writeKeys("loginServer")