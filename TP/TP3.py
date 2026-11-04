# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 08:19:39 2026

@author: lefau
"""
from time import *

# P = [2, 3, 0, 5]

def evaluer_naif(P, x):
    a=0
    for i in range (len(P)):
        a=a+P[i]*x**i
    return a

# print (evaluer_naif(P,2))

def evaluer(P, x):
    L=P[:]
    a=0
    b=0
    while len(L) != 0 :
        b=L.pop()
        a=a*x+b
    return a

# print (evaluer(P,2))

# je pense que Horner sera environ 2 fois plus rapide

# P1 = [1] * 1001
# P2 = [1] * 5001
# P3 = [1] * 20001 
# t_naif=0
# t_horner=0
# b=0

# for P in [P1, P2, P3]:
#     b=perf_counter()
#     evaluer_naif(P, 1.0001)
#     t_naif=perf_counter()-b
    
#     b=perf_counter()
#     evaluer(P,1.0001)
#     t_horner=perf_counter()-b
    
#     print(len(P) - 1, t_naif / t_horner)


# P4 = [1] * 201
# P5 = [1] * 401
# P6 = [1] * 801
# t2_naif=0
# t2_horner=0

# for P in [P4, P5, P6]:
#     b=perf_counter()
#     evaluer_naif(P, 3)
#     t2_naif=perf_counter()-b

#     b=perf_counter()
#     evaluer(P, 3)
#     t2_horner=perf_counter()-b

#     print(len(P) - 1, t2_naif / t2_horner)

def deriver(P):
    L=P[:]
    L.pop(0)
    for k in range (1,len(L)):
        L[k]=L[k]*(k+1)
    return L
    
# print (deriver(P))


def f(x):
    return x*x - 2

# a=0
# b=2
# tolerance=10**(-12)

def dichotomie(f, a, b, tolerance):
    if tolerance <= 0: 
        return "tolerance doit être supérieure à 1"
    if f(a)==0:
        return a
    if f(b)==0:
        return b
    if f(a)*f(b) > 0:
        return "f(a) et f(b) doivent être de signe opposés"
    while (b-a) > tolerance:
        m=(a+b)/2
        if f(m)==0:
            return m
        if f(m)*f(b) > 0:
            b=m
        elif f(m)*f(a) > 0:
            a=m
    return (a+b)/2
    
# print(dichotomie(f, a, b, tolerance))

P = [2, -2, 0, 1]
tolerance = 1e-10
depart=0

def newton(P, depart, tolerance):
    d=deriver(P)
    x=depart
    x2=0
    while True:
        h = evaluer(d,x)
        if h==0:
            return "erreur"
        x2=x-evaluer(P, x)/h
        if abs(x2-x) < tolerance:
            return x2
        else:
            x=x2

# print(newton(P, depart, tolerance))
Q=[-5,-2,0,1]
print(newton(Q,2,tolerance))
NbIterations=10        #j'ai pris 10 au hasard
def newton2(x, NbIterations):
    for n in range(NbIterations):
        f = x**3 - 2*x + 2
        derivee = 3*x**2 - 2
        print(f"x_{n} = {x}")
        if derivee == 0:
            print("La dérivée est nulle : impossible de continuer.")
            break
        x = x - f / derivee

newton2(0, NbIterations)

#Newton a un soucis, la fonction varrie a l'infinie entre 0 et 1












def newton_tours(P,depart,tolerance):
    d=deriver(P)
    x=depart
    c=0
    while True:
        h=evaluer(d,x)
        x2=x-evaluer(P,x)/h
        c=c+1
        if abs(x2-x)<tolerance:
            return x2,c
        x=x2

for x in [2,1,0]:
    r,c=newton_tours(Q,x,tolerance)
    print("départ",x,":",c,"tours, racine",round(r,9))

import matplotlib.pyplot as plt

xs=[]
ys=[]
for i in range (-300,301):
    xs.append(i/100)
    ys.append(evaluer(Q,i/100))

plt.figure()
plt.plot(xs,ys,label="x^3 - 2x - 5")
plt.axhline(0,linewidth=0.8)
plt.axvline(0,linewidth=0.8)
plt.ylim(-20,20)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend()
plt.title("Un polynome et son unique racine reelle")
plt.show()

#La courbe coupe l'axe une seule fois
#Cette racine est celle trouvée par Newton
#Un polynôme de degré 3 a 3 racines, les 2 autres sont complexes
#Un graphique ne montre que les racines réelles

def somme(P,Q):
    n=max(len(P),len(Q))
    A=P[:]
    B=Q[:]
    while len(A)<n:
        A.append(0)
    while len(B)<n:
        B.append(0)
    R=[]
    for i in range (n):
        R.append(A[i]+B[i])
    return R

def produit_poly(P,Q):
    R=[0]*(len(P)+len(Q)-1)
    for i in range (len(P)):
        for j in range (len(Q)):
            R[i+j]=R[i+j]+P[i]*Q[j]
    return R

print(somme([1,2],[0,0,3]))
print(produit_poly([1,1],[1,1]))
print(produit_poly([-1,1],[1,1]))

B=[1]
for k in range (10):
    B=produit_poly(B,[1,1])
print(B)
s=0
for k in range (len(B)):
    s=s+B[k]
print(s,2**10)

from math import *

def derivee_avant(f,x,h):
    return (f(x+h)-f(x))/h

def derivee_centree(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

exacte=cos(1.0)
for h in [1e-1,1e-2,1e-4,1e-6,1e-8,1e-10,1e-12]:
    e1=abs(derivee_avant(sin,1.0,h)-exacte)
    e2=abs(derivee_centree(sin,1.0,h)-exacte)
    print("h =",h,": avant",e1,"| centrée",e2)

def rectangles(f,a,b,n):
    h=(b-a)/n
    s=0
    for i in range (n):
        s=s+f(a+i*h)
    return h*s

def trapezes(f,a,b,n):
    h=(b-a)/n
    s=(f(a)+f(b))/2
    for i in range (1,n):
        s=s+f(a+i*h)
    return h*s

def simpson(f,a,b,n):
    if n%2==1:
        n=n+1
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range (1,n,2):
        s=s+4*f(a+i*h)
    for i in range (2,n,2):
        s=s+2*f(a+i*h)
    return h/3*s

def carre(x):
    return x*x

for n in [10,100,1000]:
    e1=abs(rectangles(carre,0,1,n)-1/3)
    e2=abs(trapezes(carre,0,1,n)-1/3)
    e3=abs(simpson(carre,0,1,n)-1/3)
    print("n =",n,": rectangles",e1,"| trapèzes",e2,"| simpson",e3)

def fonction_pi(x):
    return 4/(1+x*x)

a1=trapezes(fonction_pi,0,1,1000)
a2=simpson(fonction_pi,0,1,1000)
print(a1,abs(a1-pi))
print(a2,abs(a2-pi))
