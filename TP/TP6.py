import math
import random
import matplotlib.pyplot as plt

def vecteur(A, B):
    return (B[0]-A[0], B[1]-A[1])

def produit_scalaire(u, v):
    return u[0]*v[0]+u[1]*v[1]

def norme(u):
    return math.sqrt(produit_scalaire(u,u))

def angle(u, v):
    c=produit_scalaire(u,v)/(norme(u)*norme(v))
    c=max(-1,min(1,c))
    return math.degrees(math.acos(c))

print(norme((3,4)))
print(produit_scalaire((1,2),(3,4)))
print(angle((1,0),(1,1)))
print(angle((1,0),(0,1)))

def determinant(u, v):
    return u[0]*v[1]-u[1]*v[0]

def distance_point_droite(P, A, B):
    AB=vecteur(A,B)
    AP=vecteur(A,P)
    return abs(determinant(AB,AP))/norme(AB)

print(distance_point_droite((0,0),(0,1),(1,0)))
print(distance_point_droite((3,4),(0,0),(1,0)))

def orientation(A, B, C):
    d=determinant(vecteur(A,B),vecteur(A,C))
    if d>0:
        return 1
    if d<0:
        return -1
    return 0

print(orientation((0,0),(1,0),(1,1)))
print(orientation((0,0),(1,0),(1,-1)))
print(orientation((0,0),(1,1),(2,2)))

def aire(polygone):
    s=0
    for i in range(len(polygone)):
        A=polygone[i]
        B=polygone[(i+1)%len(polygone)]
        s=s+determinant(A,B)
    return abs(s)/2

carre=[(0,0),(1,0),(1,1),(0,1)]
triangle=[(0,0),(4,0),(0,3)]
maison=[(0,0),(2,0),(2,1.5),(1,2.5),(0,1.5)]
print(aire(carre),aire(triangle),aire(maison))

def se_coupent(A, B, C, D):
    o1=orientation(A,B,C)
    o2=orientation(A,B,D)
    o3=orientation(C,D,A)
    o4=orientation(C,D,B)
    return o1*o2<0 and o3*o4<0

print(se_coupent((0,0),(1,1),(0,1),(1,0)))
print(se_coupent((0,0),(1,0),(0,1),(1,1)))
print(se_coupent((0,0),(1,1),(2,2),(3,3)))

def intersection(A, B, C, D):
    AB=vecteur(A,B)
    CD=vecteur(C,D)
    d=determinant(AB,CD)
    if d==0:
        return None
    AC=vecteur(A,C)
    t=determinant(AC,CD)/d
    u=determinant(AC,AB)/d
    if 0<=t<=1 and 0<=u<=1:
        return (A[0]+t*AB[0],A[1]+t*AB[1])
    return None

print(intersection((0,0),(2,2),(0,2),(2,0)))
print(intersection((0,0),(1,0),(0,1),(1,1)))

def dedans(P, polygone):
    x,y=P
    interieur=False
    for i in range(len(polygone)):
        x1,y1=polygone[i]
        x2,y2=polygone[(i+1)%len(polygone)]
        if (y1>y)!=(y2>y):
            xc=x1+(y-y1)*(x2-x1)/(y2-y1)
            if x<xc:
                interieur=not interieur
    return interieur

for P in [(1,1),(1,2.4),(3,1),(0.2,2.2)]:
    print(P,dedans(P,maison))

tirages=200000
touches=0
for i in range(tirages):
    P=(random.uniform(0,2),random.uniform(0,2.5))
    if dedans(P,maison):
        touches=touches+1
print(2*2.5*touches/tirages)

def tracer_polygone(polygone, points):
    x=[]
    y=[]
    for P in polygone:
        x.append(P[0])
        y.append(P[1])
    x.append(polygone[0][0])
    y.append(polygone[0][1])
    plt.figure()
    plt.plot(x,y)
    for P in points:
        if dedans(P,polygone):
            plt.scatter(P[0],P[1],color="green")
        else:
            plt.scatter(P[0],P[1],color="red")
    plt.axis("equal")
    plt.show()

nuage=[]
for i in range(60):
    nuage.append((random.uniform(-0.5,2.5),random.uniform(-0.5,3)))
tracer_polygone(maison,nuage)

L=[(0,0),(3,0),(3,1),(1,1),(1,3),(0,3)]
print(aire(L))
print(dedans((0.5,2),L))
print(dedans((2,2),L))
tracer_polygone(L,[(0.5,2),(2,2),(2,0.5)])

def zone_de(P, zones):
    for i in range(len(zones)):
        if dedans(P,zones[i]):
            return i
    return None

zones=[maison,[(3,0),(4,0),(4,1),(3,1)]]
print(zone_de((1,1),zones))
print(zone_de((3.5,0.5),zones))
print(zone_de((2.5,0.5),zones))
