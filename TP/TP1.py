import sys
from math import *
from fractions import Fraction

n=2026
d=7
q=n//d
r=n%d
print(q,r)
print(q*d+r==n)

n=123456789
print(n%10)
print(n//10)

a=0.0
for k in range (1000):
    a=a+0.1
print(a)
print(a-100)

def presque_egaux(a,b):
    tolerance=1e-9
    return abs(a-b)<=tolerance

print(presque_egaux(0.1+0.2,0.3))
print(presque_egaux(1.0,1.5))

#Il ne faut jamais comparer deux flottants avec == ,si les nombres sont assez proches ou pas

for i in range (1,11):
    print(7,"x",i,"=",7*i)

n=100
a=0
for i in range (1,n+1):
    a=a+i
print(a)
print(n*(n+1)//2)

def nombre_de_chiffres(n):
    c=1
    while n>=10:
        n=n//10
        c=c+1
    return c

print(nombre_de_chiffres(2026))
print(nombre_de_chiffres(7))

def heron(a):
    tolerance=1e-12
    x=a
    while True:
        y=(x+a/x)/2
        if abs(y-x)<tolerance:
            return y
        x=y

print(heron(2))
print(sqrt(2))
print(abs(heron(2)-sqrt(2))<1e-12)

def vers_binaire(n):
    if n==0:
        return "0"
    s=""
    while n>0:
        s=str(n%2)+s
        n=n//2
    return s

print(vers_binaire(37))
print(vers_binaire(0))

eps=1.0
while 1.0+eps/2!=1.0:
    eps=eps/2
print(eps)
print(sys.float_info.epsilon)

def racines_naif(a,b,c):
    d=b*b-4*a*c
    r=sqrt(d)
    return (-b-r)/(2*a),(-b+r)/(2*a)

petite,grande=racines_naif(1.0,-1e8,1.0)
print(petite,grande)
print(petite*grande)

def racines(a,b,c):
    d=b*b-4*a*c
    r=sqrt(d)
    if b>=0:
        x=(-b-r)/(2*a)
    else:
        x=(-b+r)/(2*a)
    y=c/(a*x)
    return min(x,y),max(x,y)

petite,grande=racines(1.0,-1e8,1.0)
print(petite,grande)
print(petite*grande)
for x in [petite,grande]:
    print(x*x-1e8*x+1)

a=Fraction(0)
for k in range (1000):
    a=a+Fraction(1,10)
print(a)
print(a==100)
print(Fraction(1,10)+Fraction(2,10)==Fraction(3,10))
