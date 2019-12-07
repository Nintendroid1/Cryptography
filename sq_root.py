#For use by Fall 2019 Math 4176 Students Only

import math

def sqRootModp(a,p):
    """Calculate square root of a mod p, where p % 4 == 3"""
    if not p % 4 == 3:
        raise ValueError
    if not pow(a, (p-1)//2, p) == 1:
        raise ValueError
    y = pow(a, (p+1)//4, p)
    return [y, (-y) % p]


def sqRootModn(a,p, q):
    """Calculate square roots of a mod n where n = p * q"""
    sqrt_p = sqRootModp(a,p)
    sqrt_q = sqRootModp(a,q)
    n = p*q
    sqrt_n = []
    y = crtSolver(sqrt_p[0],sqrt_q[0],p,q)
    sqrt_n.append([y, (-y) % n])
    z = crtSolver(sqrt_p[0],sqrt_q[1],p,q)
    sqrt_n.append([z, (-z) % n])
    return sqrt_n
    


def crtSolver(a,b,p,q):
    """Find y such that y % p == a and y % q == b"""
    return (a * q * modInv(q,p) + b * p * modInv(p,q)) % (p * q)

def euclid(a,b):
    """Calculate gcd of integers a, b, not both zero"""
    if a == b == 0:
        raise ValueError
    if b == 0:
        return abs(a)
    r = a % b
    while r != 0:
        b, r = r, b % r
    return abs(b)    


def exEuclid(a,b):
    """Return gcd(a,b), x, y, where gcd(a,b) = ax + by"""
    if a == b == 0:
        raise ValueError
    if b > a:
        a, b = b, a
    s = t_old = 0
    s_old = t = 1
    while b != 0:
        q = math.floor(a/b)
        a, b = b, a % b
        s, s_old = s_old - (s * q), s
        t, t_old = t_old - (t * q), t
    return a, s_old, t_old
        
    

    
def modInv(b,n):
    """Calculate the Inverse of b modulo n"""
    b = b % n
    l = exEuclid(n,b)
    if l[0] != 1:
        raise ValueError
    else:
        return l[2] % n
    
