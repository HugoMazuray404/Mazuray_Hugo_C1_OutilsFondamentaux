# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:59:53 2026

@author: lefau
"""

from math import *
import matplotlib.pyplot as plt
from random import *

def ChargerVilles():
    f = open('Villes.txt', 'r', encoding="utf-8")
    lignes = f.readlines()
    VILLES=[]
    A1=[]
    A2=[]
    for ligne in lignes:
        ligne = ligne.strip()
        if ligne == "":
            continue
        nom, latitude, longitude, population = ligne.split(",")
        latitude=float(latitude)
        longitude=float(longitude)
        #print(nom, latitude, longitude, population)
        VILLES.append([nom, latitude, longitude, population])
        A1.append(latitude)
        A2.append(longitude)
    f.close()
    return VILLES, A1, A2
    
VILLES, A1, A2 = ChargerVilles()

def AfficheParcours(VILLES, P):
    x = []
    y = []
    for i in P:
        ville = VILLES[i]
        x.append(ville[2]) 
        y.append(ville[1])  
    ville_depart = VILLES[P[0]]
    x.append(ville_depart[2])
    y.append(ville_depart[1])
    plt.plot(x, y, marker='o')
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Parcours du voyageur de commerce")
    plt.grid()
    plt.plot(x, y, marker='o')
    plt.scatter(x, y)
    plt.show()

# P=[1,8,9,17]
#AfficheParcours(VILLES, P)
    
    
def Distance(A1,A2,s,f):
    R = 6370.7
    La1=radians(A1[s])
    La2=radians(A1[f])
    Lon1=radians(A2[s])
    Lon2=radians(A2[f])
    D=R*acos(sin(La1)*sin(La2)+cos(La1)*cos(La2)*cos(Lon1-Lon2))
    return D

# s=1
# f=17
# print(VILLES[1])
# print(VILLES[17])
# print("Distance:",round(Distance(A1, A2, s, f), 2),"km")

def DistanceParcours(VILLES,P):
    S=[]
    a=0
    c=0
    for k in range(len(P)):
        S.append(P[k])
    while len(S)!=1:
        b=S.pop(0)
        a=a+Distance(A1,A2,b,S[0])
    c=S.pop(0)
    a=a+Distance(A1,A2,c,P[0])
    return a

# print("Distance Parcours:",round(DistanceParcours(VILLES,P), 2),"km")

def Affiche_Permut(k,L):
    if k==1:
        print(round(DistanceParcours(VILLES,L),0))
    else:
        for i in range (k):
            L[k-1],L[i]=L[i],L[k-1]
            Affiche_Permut(k-1,L)
            L[k-1],L[i]=L[i],L[k-1]
                
def Recherche_Meilleur_Parcours_BOURRIN(k,L,VILLES):
    global D_min,P
    if k==1:
        a=DistanceParcours(VILLES,L)
        if a<D_min:
            D_min=a
            P=L[:]
    else:
        for i in range (k):
            L[k-1],L[i]=L[i],L[k-1]
            Recherche_Meilleur_Parcours_BOURRIN(k-1,L,VILLES)
            L[k-1],L[i]=L[i],L[k-1]
            
def Meilleur_Parcours_BOURRIN(n,VILLES):
    global D_min,P
    P=[k for k in range(n)]
    D_min=DistanceParcours(VILLES,P)
    Recherche_Meilleur_Parcours_BOURRIN(n,P,VILLES)
    return P,D_min

# n=6
# P, D_min = Meilleur_Parcours_BOURRIN(n, VILLES)
# print("Meilleur parcours :", P + [P[0]])
# print("Distance minimale :", round(D_min, 1), "km")


# def f_linéaire(i,M,fmax):
#     return fmax*(1-(i/M))
    
# def f_exponentielle(i, M, fmax):
#     return fmax*exp(-(i / M))

def p(D1,D2,i,M,fmax):
    return exp(-(D2-D1)/(fmax*(1-(i/M))))
    
def Echange(P,i,j):
    P[i],P[j]=P[j],P[i]
    return P
    
def Meilleur_Parcours_2(VILLES,M,fmax):
    P=list(range(0, 58))
    D_best=DistanceParcours(VILLES, P)
    P_best=P[:]
    for k in range(M):
        D1=DistanceParcours(VILLES,P)
        i,j=sample(range(len(P)),2)
        P[i],P[j]=P[j],P[i]
        D2=DistanceParcours(VILLES,P)
        if D2>=D_best:
            pr=p(D1,D2,k,M,fmax)
            a=random()
            if a>pr:
                P[j],P[i]=P[i],P[j]
                D2=D1
        if D2<D_best:
            D_best=D2
            P_best=P[:]
    return P_best, D_best

# P, D = Meilleur_Parcours_2(VILLES, 25000, 100)
# print("Distance :", round(D,1), "km")
#AfficheParcours(VILLES, P)

def OptimisationEchange(VILLES, P):
    P_best = P[:]
    D_best = DistanceParcours(VILLES, P)

    for i in range(len(P)):
        for j in range(1, len(P)):
            L=P[:]
            L[i],L[j]=L[j],L[i]
            New_D=DistanceParcours(VILLES, L)
            if New_D < D_best:
                D_best=New_D
                P_best=L[:]
    AfficheParcours(VILLES, P_best)
    return P_best, D_best


P = list(range(0, 58))
print("parcours optimisé:", OptimisationEchange(VILLES, P))



from time import perf_counter
from sys import getsizeof


def DistanceHaversine(A1,A2):
    R=6370.7
    la1=radians(A1[0])
    la2=radians(A2[0])
    dlat=radians(A2[0]-A1[0])
    dlon=radians(A2[1]-A1[1])
    a=sin(dlat/2)**2+cos(la1)*cos(la2)*sin(dlon/2)**2
    a=min(1,max(0,a))
    return 2*R*asin(sqrt(a))


print("Q19")
A=[47.7504,-3.3666]
for e in [3,0.00005,0.0000005]:
    B=[A[0]+e,A[1]]
    D1=Distance([A[0],B[0]],[A[1],B[1]],0,1)
    D2=DistanceHaversine(A,B)
    ecart=abs(D1-D2)
    print("Distance (km) :",D2,"écart absolu (km) :",ecart,"écart relatif :",ecart/D2)
# Pour les grandes distances, les deux formules donnent presque le même résultat.
# Pour quelques centimètres, la formule avec arccos devient moins précise.
# Haversine convient mieux quand les points sont très proches.


latitude_reference=0
for ville in VILLES:
    latitude_reference=latitude_reference+ville[1]
latitude_reference=latitude_reference/len(VILLES)


def CoordonneesPlanes(A):
    R=6370.7
    x=R*radians(A[1])*cos(radians(latitude_reference))
    y=R*radians(A[0])
    return [x,y]


def DistancePlane(A1,A2):
    A=CoordonneesPlanes(A1)
    B=CoordonneesPlanes(A2)
    return sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)


print("Q20")
print("Latitude de référence :",latitude_reference)
xs=[]
ys=[]
for i in range(len(VILLES)):
    for j in range(i+1,len(VILLES)):
        A=VILLES[i][1:3]
        B=VILLES[j][1:3]
        D1=DistanceHaversine(A,B)
        D2=DistancePlane(A,B)
        xs.append(D1)
        ys.append(100*abs(D2-D1)/D1)
for i,j in [(0,1),(0,8),(0,3),(1,57),(2,5)]:
    if j<len(VILLES):
        A=VILLES[i][1:3]
        B=VILLES[j][1:3]
        D1=DistanceHaversine(A,B)
        D2=DistancePlane(A,B)
        print(VILLES[i][0],VILLES[j][0],round(D1,2),round(D2,2),round(100*abs(D1-D2)/D1,3),"%")
plt.figure()
plt.scatter(xs,ys,s=5)
plt.xlabel("Distance sphérique (km)")
plt.ylabel("Erreur relative (%)")
plt.title("Approximation plane")
plt.grid()
plt.show()
# L'approximation plane est surtout utile pour des villes proches.
# Plus les villes sont éloignées, plus l'erreur peut augmenter.


def MatriceDistances(VILLES):
    n=len(VILLES)
    Latitudes=[]
    Longitudes=[]
    for ville in VILLES:
        Latitudes.append(ville[1])
        Longitudes.append(ville[2])
    D=[]
    for i in range(n):
        L=[]
        for j in range(n):
            L.append(0.0)
        D.append(L)
    for i in range(n):
        for j in range(i+1,n):
            a=Distance(Latitudes,Longitudes,i,j)
            D[i][j]=a
            D[j][i]=a
    return D


def DistanceParcoursMatrice(D,P):
    s=0
    for i in range(len(P)):
        s=s+D[P[i]][P[(i+1)%len(P)]]
    return s


print("Q21")
D=MatriceDistances(VILLES)
P1=[1,8,9,17]
print("Distance normale :",DistanceParcours(VILLES,P1))
print("Distance avec matrice :",DistanceParcoursMatrice(D,P1))
print("Symétrie :",D[1][8]==D[8][1],"diagonale :",D[1][1])
# La matrice est symétrique car aller de A à B donne la même distance que de B à A.
# Sur la diagonale, les distances sont nulles car une ville est à distance 0 d'elle-même.


print("Q22")
nb_parcours=[1,10,100,500,2000]
t1=[]
t2=[]
seuil=None
for n in nb_parcours:
    parcours=[]
    for i in range(n):
        parcours.append(sample(range(len(VILLES)),len(VILLES)))
    debut=perf_counter()
    for P in parcours:
        DistanceParcours(VILLES,P)
    a=perf_counter()-debut
    debut=perf_counter()
    D=MatriceDistances(VILLES)
    for P in parcours:
        DistanceParcoursMatrice(D,P)
    b=perf_counter()-debut
    t1.append(a)
    t2.append(b)
    print(n,"parcours :",round(a,5),"s sans matrice,",round(b,5),"s avec matrice")
    if b<a and seuil==None:
        seuil=n
print("Premier nombre testé rentable :",seuil)
plt.figure()
plt.plot(nb_parcours,t1,marker="o",label="Sans matrice")
plt.plot(nb_parcours,t2,marker="o",label="Avec matrice et construction")
plt.xlabel("Nombre de parcours")
plt.ylabel("Temps (s)")
plt.title("Temps de calcul")
plt.legend()
plt.grid()
plt.show()

memoire=getsizeof(D)
for L in D:
    memoire=memoire+getsizeof(L)
for i in range(len(D)):
    for j in range(i,len(D)):
        memoire=memoire+getsizeof(D[i][j])
print("Mémoire de la matrice de",len(D),"villes :",round(memoire/1024,2),"Ko")
for n in [58,100,500,1000]:
    print(n,"villes, estimation :",round(32*n*n/1024/1024,2),"Mo")
# La matrice évite de refaire les mêmes calculs et devient intéressante pour beaucoup de parcours.
# Le nombre affiché plus haut donne le premier cas rentable parmi les valeurs testées.
# Par contre, plus il y a de villes, plus elle occupe de mémoire.


def resoudre(A,b,tolerance=1e-14):
    n=len(A)
    M=[]
    for i in range(n):
        L=A[i][:]
        L.append(b[i])
        M.append(L)
    for k in range(n):
        imax=k
        for i in range(k+1,n):
            if abs(M[i][k])>abs(M[imax][k]):
                imax=i
        if abs(M[imax][k])<=tolerance:
            return "système singulier ou mal posé"
        M[k],M[imax]=M[imax],M[k]
        for i in range(k+1,n):
            facteur=M[i][k]/M[k][k]
            for j in range(k,n+1):
                M[i][j]=M[i][j]-facteur*M[k][j]
    x=[0.0]*n
    for i in range(n-1,-1,-1):
        a=M[i][n]
        for j in range(i+1,n):
            a=a-M[i][j]*x[j]
        x[i]=a/M[i][i]
    return x


def CoefficientsG(M,fmax):
    A=[[0,0,1],[(M/2)**2,M/2,1],[M*M,M,1]]
    b=[fmax,fmax/4,0]
    return resoudre(A,b)


def g(i,M,fmax):
    a,b,c=CoefficientsG(M,fmax)
    return a*i*i+b*i+c


print("Q23")
M=25000
fmax=100
a,b,c=CoefficientsG(M,fmax)
print("a,b,c :",a,b,c)
print("g(0), g(M/2), g(M) :",g(0,M,fmax),g(M/2,M,fmax),g(M,M,fmax))
xs=[]
ys=[]
positif=True
decroissant=True
for i in range(101):
    x=M*i/100
    y=a*x*x+b*x+c
    xs.append(x)
    ys.append(y)
    if y < -1e-9:
        positif=False
    if i>0 and y>ys[i-1]+1e-9:
        decroissant=False
print("Positive :",positif,"décroissante :",decroissant)
plt.figure()
plt.plot(xs,ys)
plt.xlabel("Itération i")
plt.ylabel("g(i)")
plt.title("Loi polynomiale")
plt.grid()
plt.show()
# Le système donne a=fmax/M**2, b=-2*fmax/M et c=fmax.
# Donc g(i)=fmax*(1-i/M)**2 : elle reste positive et elle diminue jusqu'à 0.


def evaluer(P,x):
    L=P[:]
    a=0
    b=0
    while len(L)!=0:
        b=L.pop()
        a=a*x+b
    return a


def deriver(P):
    L=P[:]
    L.pop(0)
    for k in range(1,len(L)):
        L[k]=L[k]*(k+1)
    return L


def dichotomie(P,a,b,tolerance):
    c=0
    while b-a>tolerance:
        m=(a+b)/2
        if evaluer(P,m)*evaluer(P,a)<=0:
            b=m
        else:
            a=m
        c=c+1
    return (a+b)/2,c


def newton(P,depart,tolerance):
    d=deriver(P)
    x=depart
    c=0
    for i in range(100):
        h=evaluer(d,x)
        if h==0:
            return None,c
        x2=x-evaluer(P,x)/h
        c=c+1
        if abs(x2-x)<tolerance:
            return x2,c
        x=x2
    return x,c


print("Q24")
a,b,c=CoefficientsG(M,fmax)
Q=[c-0.1*fmax,b,a]
x1,n1=dichotomie(Q,0,M,1e-9)
x2,n2=newton(Q,M/2,1e-9)
x_exact=M*(1-sqrt(0.1))
print("Dichotomie :",x1,"tours :",n1,"erreur :",abs(x1-x_exact))
print("Newton :",x2,"tours :",n2,"erreur :",abs(x2-x_exact))
print("Valeurs g :",g(x1,M,fmax),g(x2,M,fmax))
# La valeur cherchée est vers 0,684*M, soit environ 17094 pour M=25000.
# La dichotomie demande plus de tours que Newton, mais les deux donnent une valeur proche.


def Meilleur_Parcours_3(VILLES,M,fmax):
    P=list(range(len(VILLES)))
    D_best=DistanceParcours(VILLES,P)
    P_best=P[:]
    a,b,c=CoefficientsG(M,fmax)
    for k in range(M):
        D1=DistanceParcours(VILLES,P)
        i,j=sample(range(len(P)),2)
        P[i],P[j]=P[j],P[i]
        D2=DistanceParcours(VILLES,P)
        if D2>=D_best:
            if D2<=D1:
                pr=1
            else:
                pr=exp(-(D2-D1)/(a*k*k+b*k+c))
            r=random()
            if r>pr:
                P[i],P[j]=P[j],P[i]
                D2=D1
        if D2<D_best:
            D_best=D2
            P_best=P[:]
    return P_best,D_best


print("Q25")
for i in range(3):
    seed(100+i)
    P2,D2=Meilleur_Parcours_2(VILLES,2500,100)
    seed(100+i)
    P3,D3=Meilleur_Parcours_3(VILLES,2500,100)
    print("Essai",i+1,": linéaire",round(D2,2),"km, polynomiale",round(D3,2),"km")
# La loi polynomiale ne donne pas toujours un meilleur trajet.
# Le résultat dépend aussi du hasard.


def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


def ParcoursModulaire(N,p):
    if pgcd(N,p)!=1:
        return None
    P=[]
    for k in range(N):
        P.append((k*p)%N)
    return P


print("Q26")
N=len(VILLES)
print("Parcours invalide p=2 :",ParcoursModulaire(N,2))
valeurs=[]
for pas in [1,3,5,7,9,11,13,15,17,19]:
    P=ParcoursModulaire(N,pas)
    if P!=None:
        d=DistanceParcours(VILLES,P)
        valeurs.append(d)
        print("p=",pas,"pgcd=",pgcd(N,pas),"distance=",round(d,2))
aleatoires=[]
for i in range(len(valeurs)):
    P=sample(range(N),N)
    aleatoires.append(DistanceParcours(VILLES,P))
print("Moyenne modulaire :",sum(valeurs)/len(valeurs))
print("Moyenne aléatoire :",sum(aleatoires)/len(aleatoires))
# Il faut que pgcd(p,N)=1 pour visiter toutes les villes une seule fois.
# Sinon, certains indices reviennent et d'autres ne sont pas visités.
# Les parcours modulaires ne sont pas forcément plus courts que les parcours aléatoires.


def Essais(fonction,VILLES,M,fmax,n):
    longueurs=[]
    temps=[]
    P_best=[]
    D_best=float("inf")
    t_best=0
    for i in range(n):
        seed(200+i)
        debut=perf_counter()
        P,D=fonction(VILLES,M,fmax)
        t=perf_counter()-debut
        longueurs.append(D)
        temps.append(t)
        if D<D_best:
            D_best=D
            P_best=P[:]
            t_best=t
    moyenne=sum(longueurs)/len(longueurs)
    s=0
    for d in longueurs:
        s=s+(d-moyenne)**2
    ecart=sqrt(s/len(longueurs))
    return P_best,D_best,moyenne,ecart,sum(temps)/len(temps),t_best


print("Q27")
P6,D6=Meilleur_Parcours_BOURRIN(6,VILLES)
print("Recherche exhaustive sur 6 villes :",round(D6,2),"km")
print("Recherche exhaustive non utilisée pour les 58 villes")
resultats=[]
P_final=[]
D_final=float("inf")
methode_finale=""
t_final=0
for nom,fonction in [("Linéaire",Meilleur_Parcours_2),("Polynomiale",Meilleur_Parcours_3)]:
    P,D,moyenne,ecart,temps,t=Essais(fonction,VILLES,3000,100,3)
    resultats.append([nom,D,moyenne,ecart,temps])
    if D<D_final:
        P_final=P[:]
        D_final=D
        methode_finale=nom
        t_final=t

debut=perf_counter()
plt.figure()
P_echange,D_echange=OptimisationEchange(VILLES,P_final)
t_echange=perf_counter()-debut
D_echange=DistanceParcours(VILLES,P_echange)
resultats.append(["Échange",D_echange,D_echange,0,t_echange])
if D_echange<D_final:
    P_final=P_echange[:]
    D_final=D_echange
    methode_finale="Échange"
    t_final=t_echange
print("Méthode | meilleur | moyenne | écart-type | temps moyen")
for L in resultats:
    print(L[0],round(L[1],2),round(L[2],2),round(L[3],2),round(L[4],3))
plt.figure()
plt.bar([L[0] for L in resultats],[L[1] for L in resultats])
plt.ylabel("Meilleure distance (km)")
plt.title("Comparaison des méthodes")
plt.show()
# La recherche exhaustive donne le meilleur résultat pour 6 villes, mais elle est trop lente pour 58.
# Pour 58 villes, les résultats des méthodes aléatoires changent d'un essai à l'autre.
# Le tableau permet de comparer les distances, leur variation et le temps de calcul.


print("Q28")
x1=[]
y1=[]
y2=[]
for m in [1000,3000,6000]:
    x1.append(m)
    for nom,fonction,ys in [("Linéaire",Meilleur_Parcours_2,y1),("Polynomiale",Meilleur_Parcours_3,y2)]:
        P,D,moyenne,ecart,temps,t=Essais(fonction,VILLES,m,100,3)
        ys.append(moyenne)
        print(nom,"M=",m,"fmax=100","moyenne=",round(moyenne,2),"écart=",round(ecart,2),"temps=",round(temps,2))
        if D<D_final:
            P_final=P[:]
            D_final=D
            methode_finale=nom
            t_final=t
plt.figure()
plt.plot(x1,y1,marker="o",label="Linéaire")
plt.plot(x1,y2,marker="o",label="Polynomiale")
plt.xlabel("M")
plt.ylabel("Distance moyenne (km)")
plt.title("Influence du nombre d'itérations")
plt.legend()
plt.grid()
plt.show()

x2=[]
y1=[]
y2=[]
for fm in [30,100,200]:
    x2.append(fm)
    for nom,fonction,ys in [("Linéaire",Meilleur_Parcours_2,y1),("Polynomiale",Meilleur_Parcours_3,y2)]:
        P,D,moyenne,ecart,temps,t=Essais(fonction,VILLES,3000,fm,3)
        ys.append(moyenne)
        print(nom,"M=3000","fmax=",fm,"moyenne=",round(moyenne,2),"écart=",round(ecart,2),"temps=",round(temps,2))
        if D<D_final:
            P_final=P[:]
            D_final=D
            methode_finale=nom
            t_final=t
plt.figure()
plt.plot(x2,y1,marker="o",label="Linéaire")
plt.plot(x2,y2,marker="o",label="Polynomiale")
plt.xlabel("fmax")
plt.ylabel("Distance moyenne (km)")
plt.title("Influence de fmax")
plt.legend()
plt.grid()
plt.show()
# Avec plus d'itérations, on peut trouver un trajet plus court, mais le calcul prend plus de temps.
# Changer fmax modifie les échanges acceptés et donc les résultats.
# Aucun réglage ne garantit à lui seul le meilleur trajet.


print("Q29")
for num,(nom,fonction) in enumerate([("Linéaire",Meilleur_Parcours_2),("Polynomiale",Meilleur_Parcours_3)]):
    for essai in range(4):
        seed(500+10*num+essai)
        debut=perf_counter()
        P,D=fonction(VILLES,25000,100)
        t=perf_counter()-debut
        print(nom,"essai",essai+1,":",round(D,2),"km en",round(t,2),"s")
        if D<D_final:
            P_final=P[:]
            D_final=D
            methode_finale=nom
            t_final=t
debut=perf_counter()
plt.figure()
P_echange,D_echange=OptimisationEchange(VILLES,P_final)
t_echange=perf_counter()-debut
D_echange=DistanceParcours(VILLES,P_echange)
print("Après optimisation par échange :",round(D_echange,2),"km en",round(t_echange,2),"s")
if D_echange<D_final:
    P_final=P_echange[:] 
    D_final=D_echange
    methode_finale=methode_finale+" + échange"
    t_final=t_final+t_echange
print("Meilleur parcours :",P_final+[P_final[0]])
print("Distance :",round(D_final,2),"km")
print("Méthode :",methode_finale)
print("Temps de calcul de cet essai :",round(t_final,3),"s")
plt.figure()
AfficheParcours(VILLES,P_final)
# Ce parcours est le meilleur de mes essais, mais il n'est pas forcément optimal.
# Pour le prouver, il faudrait comparer tous les parcours, ce qui est trop long pour 58 villes.
# On pourrait faire plus d'essais et ajouter d'autres améliorations du parcours.
