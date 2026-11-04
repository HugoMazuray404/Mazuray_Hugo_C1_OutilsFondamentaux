import numpy as np
import matplotlib.pyplot as plt
from random import *
from time import *

def transposee(A):
    L=[]
    for j in range (len(A[0])):
        M=[]
        for i in range (len(A)):
            M.append(A[i][j])
        L.append(M)
    return L

print(transposee([[1,2,3],[4,5,6]]))

def produit(A,B):
    n=len(A)
    p=len(A[0])
    if len(B)!=p:
        return "dimensions incompatibles"
    q=len(B[0])
    C=[]
    for i in range (n):
        L=[]
        for j in range (q):
            a=0
            for k in range (p):
                a=a+A[i][k]*B[k][j]
            L.append(a)
        C.append(L)
    return C

identite=[[1,0,0],[0,1,0],[0,0,1]]
A=[[1,2,2],[1,3,-2],[3,5,8]]
print(produit(A,identite)==A)
print(produit([[1,2],[3,4]],[[0,1],[1,0]]))

def matrice_aleatoire(n):
    L=[]
    for i in range (n):
        M=[]
        for j in range (n):
            M.append(random())
        L.append(M)
    return L

for n in [40,80,120]:
    A=matrice_aleatoire(n)
    B=matrice_aleatoire(n)
    b=perf_counter()
    produit(A,B)
    print("n =",n,":",round(perf_counter()-b,4),"s")

n=120
A=matrice_aleatoire(n)
B=matrice_aleatoire(n)

b=perf_counter()
produit(A,B)
t_python=perf_counter()-b

An=np.array(A)
Bn=np.array(B)
b=perf_counter()
An@Bn
t_numpy=perf_counter()-b

print("python pur :",round(t_python,4),"s")
print("numpy :",round(t_numpy,6),"s")
print("rapport :",round(t_python/t_numpy))

def resoudre(A,b,tolerance=1e-14):
    n=len(A)
    M=[]
    for i in range (n):
        L=A[i][:]
        L.append(b[i])
        M.append(L)
    for k in range (n):
        imax=k
        for i in range (k+1,n):
            if abs(M[i][k])>abs(M[imax][k]):
                imax=i
        if abs(M[imax][k])<=tolerance:
            return "système singulier ou mal posé"
        M[k],M[imax]=M[imax],M[k]
        for i in range (k+1,n):
            facteur=M[i][k]/M[k][k]
            for j in range (k,n+1):
                M[i][j]=M[i][j]-facteur*M[k][j]
    x=[0.0]*n
    for i in range (n-1,-1,-1):
        a=M[i][n]
        for j in range (i+1,n):
            a=a-M[i][j]*x[j]
        x[i]=a/M[i][i]
    return x

A=[[1,2,2],[1,3,-2],[3,5,8]]
b=[2,-1,8]
x=resoudre(A,b)
R=[]
for v in x:
    R.append(round(v,10))
print(R)

V=[]
for i in range (3):
    a=0
    for j in range (3):
        a=a+A[i][j]*x[j]
    V.append(round(a,10))
print(V)

n=50
A=matrice_aleatoire(n)
b=[]
for i in range (n):
    b.append(random())
x=resoudre(A,b)
y=np.linalg.solve(np.array(A),np.array(b))
e=0
for i in range (n):
    if abs(x[i]-y[i])>e:
        e=abs(x[i]-y[i])
print("écart maximal :",e)
print(e<1e-9)

def hilbert(n):
    H=[]
    for i in range (n):
        L=[]
        for j in range (n):
            L.append(1.0/(i+j+1))
        H.append(L)
    return np.array(H)

n=12
H=hilbert(n)
x_vrai=np.ones(n)
b=H@x_vrai

x_solve=np.linalg.solve(H,b)
x_inverse=np.linalg.inv(H)@b

print("erreur avec solve :",np.max(np.abs(x_solve-x_vrai)))
print("erreur avec inv @ b :",np.max(np.abs(x_inverse-x_vrai)))
print("conditionnement :",np.linalg.cond(H))

#solve donne la solution la plus proche de la vraie

#Une IA propose souvent inv(A) @ b

def rotation(angle):
    c=np.cos(angle)
    s=np.sin(angle)
    return np.array([[c,-s],[s,c]])

maison=np.array([[0,0],[2,0],[2,1.5],[1,2.5],[0,1.5],[0,0]]).T

plt.figure(figsize=(5,5))
plt.plot(maison[0],maison[1],label="depart")
for angle in [np.pi/6,np.pi/3,np.pi/2]:
    image=rotation(angle)@maison
    plt.plot(image[0],image[1],label="rotation "+str(int(np.degrees(angle)))+" degres")
plt.axis("equal")
plt.legend()
plt.title("Une matrice fait tourner une figure")
plt.show()

g=rotation(np.pi/3)@rotation(np.pi/6)
d=rotation(np.pi/2)
print(np.allclose(g,d))
print(np.round(d,10))

def determinant(A):
    n=len(A)
    M=[]
    for i in range (n):
        M.append(A[i][:])
    det=1.0
    for k in range (n):
        imax=k
        for i in range (k+1,n):
            if abs(M[i][k])>abs(M[imax][k]):
                imax=i
        if abs(M[imax][k])<1e-14:
            return 0.0
        if imax!=k:
            M[k],M[imax]=M[imax],M[k]
            det=-det
        det=det*M[k][k]
        for i in range (k+1,n):
            facteur=M[i][k]/M[k][k]
            for j in range (k,n):
                M[i][j]=M[i][j]-facteur*M[k][j]
    return det

A=[[1,2,2],[1,3,-2],[3,5,8]]
print(determinant(A),np.linalg.det(np.array(A)))
print(determinant([[1,2],[2,4]]))

from fractions import Fraction

def hilbert_exacte(n):
    H=[]
    for i in range (n):
        L=[]
        for j in range (n):
            L.append(Fraction(1,i+j+1))
        H.append(L)
    return H

n=12
H_exacte=hilbert_exacte(n)
b_exact=[]
for i in range (n):
    a=0
    for j in range (n):
        a=a+H_exacte[i][j]
    b_exact.append(a)

print(resoudre(H_exacte,b_exact))
x_exact=resoudre(H_exacte,b_exact,0)
print(x_exact)
ok=True
for v in x_exact:
    if v!=1:
        ok=False
print(ok)

def translation(tx,ty):
    return np.array([[1.0,0.0,tx],[0.0,1.0,ty],[0.0,0.0,1.0]])

def rotation_h(angle):
    c=np.cos(angle)
    s=np.sin(angle)
    return np.array([[c,-s,0.0],[s,c,0.0],[0.0,0.0,1.0]])

point=np.array([1.0,0.0,1.0])
T=translation(3,1)
R=rotation_h(np.pi/2)

print(np.round(R@T@point,10))
print(np.round(T@R@point,10))
