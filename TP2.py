# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:13:52 2026

@author: lefau
"""
def diviseur(n):
    L=[]
    M=[]
    a=0
    for k in range (1,n+1):
        if n%k==0 :
            L.append(n//k)
    for i in range (len(L)):
        a=L.pop()
        M.append(a)
    return M

#print(diviseur(28))

def pgcd_naif(a,b):
    m=1
    for k in range (1,min(a,b)+1):
        if a%k==0 and b%k==0 :
            m=k
    return m
print(pgcd_naif(1071,462))

def pgcd(a,b):
    while b!=0 :
        a,b = b, a%b
    return a

print(pgcd(1071,462))

def est_premier_naif(n):
    if n<2:
        return False
    for d in range (2,n):
        if n%d==0:
            return False
    return True

print(est_premier_naif(97),est_premier_naif(91))

def est_premier(n):
    if n<2:
        return False
    if n%2==0:
        return n==2
    d=3
    while d*d<=n:
        if n%d==0:
            return False
        d=d+2
    return True

print(est_premier(97),est_premier(91),est_premier(2),est_premier(1))

from time import *

def duree(fonction,argument):
    debut=perf_counter()
    fonction(argument)
    return perf_counter()-debut

for n in [10007,100003,1000003]:
    t_naif=duree(est_premier_naif,n)
    t_rac=duree(est_premier,n)
    print(n,"naif:",round(t_naif,5),"racine:",round(t_rac,6))

#Il faut tester n=1 : la bonne réponse est False
#Il faut tester n=2 : la bonne réponse est True

def crible(limite):
    T=[True]*(limite+1)
    T[0]=False
    if limite>=1:
        T[1]=False
    d=2
    while d*d<=limite:
        if T[d]:
            for m in range (d*d,limite+1,d):
                T[m]=False
        d=d+1
    L=[]
    for k in range (limite+1):
        if T[k]:
            L.append(k)
    return L

premiers=crible(100)
print(premiers)
print(len(premiers),"premiers jusqu'à 100")

b=perf_counter()
p=crible(100000)
t_crible=perf_counter()-b

b=perf_counter()
c=0
for k in range (100001):
    if est_premier(k):
        c=c+1
t_un=perf_counter()-b

print(len(p),c)
print("crible:",round(t_crible,4),"un par un:",round(t_un,4))

def facteurs(n):
    L=[]
    d=2
    while d*d<=n:
        while n%d==0:
            L.append(d)
            n=n//d
        d=d+1
    if n>1:
        L.append(n)
    return L

f=facteurs(360)
print(f)
a=1
for x in f:
    a=a*x
print(a)

def fibonacci_recursif(n):
    if n<2:
        return n
    return fibonacci_recursif(n-1)+fibonacci_recursif(n-2)

L=[]
for k in range (15):
    L.append(fibonacci_recursif(k))
print(L)

for n in [20,25,30]:
    print("F(",n,") :",round(duree(fibonacci_recursif,n),4),"s")

appels=[0]*31

def fibonacci_compte(n):
    appels[n]=appels[n]+1
    if n<2:
        return n
    return fibonacci_compte(n-1)+fibonacci_compte(n-2)

r=fibonacci_compte(30)
print("F(30) =",r)
print("appels à F(1) :",appels[1])
total=0
for k in range (31):
    total=total+appels[k]
print("appels en tout :",total)

def fibonacci(n):
    a=0
    b=1
    for k in range (n):
        a,b=b,a+b
    return a

ok=True
for k in range (26):
    if fibonacci(k)!=fibonacci_recursif(k):
        ok=False
print(ok)
print("F(30) en",round(duree(fibonacci,30),6),"s")
grand=fibonacci(10000)
print(len(str(grand)),"chiffres")

def euclide_etendu(a,b):
    if b==0:
        return a,1,0
    g,u,v=euclide_etendu(b,a%b)
    return g,v,u-(a//b)*v

g,u,v=euclide_etendu(1071,462)
print(g,u,v,1071*u+462*v==g)

def puissance_mod_naive(a,e,n):
    r=1
    for k in range (e):
        r=r*a%n
    return r

def puissance_mod(a,e,n):
    r=1
    a=a%n
    while e>0:
        if e%2==1:
            r=r*a%n
        a=a*a%n
        e=e//2
    return r

a=7
e=10**7
n=1000003
print(puissance_mod(a,e,n),pow(a,e,n))

b=perf_counter()
puissance_mod_naive(a,e,n)
t_naive=perf_counter()-b

b=perf_counter()
puissance_mod(a,e,n)
t_rapide=perf_counter()-b

print("naive:",round(t_naive,3),"rapide:",round(t_rapide,6))
