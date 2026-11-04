def lettre_vers_nombre(c):
    return ord(c)-ord("A")

def nombre_vers_lettre(n):
    return chr(n%26+ord("A"))

print(lettre_vers_nombre("C"),nombre_vers_lettre(2))

def nettoyer(texte):
    texte=texte.upper()
    accents="ÀÂÄÇÉÈÊËÎÏÔÖÙÛÜ"
    sans="AAACEEEEIIOOUUU"
    R=""
    for c in texte:
        for k in range (len(accents)):
            if c==accents[k]:
                c=sans[k]
        if c>="A" and c<="Z":
            R=R+c
    return R

print(nettoyer("Été, à Paris !"))

def chiffrer(texte,a,b):
    R=""
    for c in texte:
        x=lettre_vers_nombre(c)
        R=R+nombre_vers_lettre((a*x+b)%26)
    return R

message="ATTAQUEALAUBE"
print(chiffrer(message,5,8))

def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

valides=[]
for a in range (1,26):
    if pgcd(a,26)==1:
        valides.append(a)
print(valides)
print(len(valides),"valeurs possibles pour a")

def inverse_modulaire(a,n):
    a=a%n
    for c in range (1,n):
        if (a*c)%n==1:
            return c
    raise ValueError(str(a)+" n'est pas inversible modulo "+str(n))

print(inverse_modulaire(5,26))
print((5*21)%26)

try:
    inverse_modulaire(4,26)
except ValueError as erreur:
    print("erreur attendue :",erreur)

def dechiffrer(texte,a,b):
    ai=inverse_modulaire(a,26)
    R=""
    for c in texte:
        y=lettre_vers_nombre(c)
        R=R+nombre_vers_lettre(ai*(y-b)%26)
    return R

message=nettoyer("Attaque a l aube")
secret=chiffrer(message,5,8)
print(secret)
print(dechiffrer(secret,5,8))
print(dechiffrer(secret,5,8)==message)

try:
    dechiffrer(secret,4,7)
except ValueError as erreur:
    print("clé refusée :",erreur)

def toutes_les_clefs(secret):
    L=[]
    for a in valides:
        for b in range (26):
            L.append((a,b,dechiffrer(secret,a,b)))
    return L

essais=toutes_les_clefs(secret)
print(len(essais),"clefs essayées")
for e in essais:
    if e[2]==message:
        print("la bonne clef :",e[0],e[1])

texte_long=nettoyer("Le chiffrement affine est un chiffrement par substitution monoalphabetique. Chaque lettre du message est remplacee par une autre lettre, toujours la meme, ce qui laisse intactes les frequences relatives des lettres et permet de casser le code sans essayer toutes les clefs possibles.")
secret_long=chiffrer(texte_long,7,12)

comptes=[0]*26
for c in secret_long:
    comptes[lettre_vers_nombre(c)]=comptes[lettre_vers_nombre(c)]+1
imax=0
for k in range (26):
    if comptes[k]>comptes[imax]:
        imax=k
print("lettre la plus fréquente du chiffré :",nombre_vers_lettre(imax))

candidats=[]
for a in valides:
    b=(imax-4*a)%26
    candidats.append((a,b,dechiffrer(secret_long,a,b)))
print(len(candidats),"candidats au lieu de 312")
for e in candidats:
    if e[2][:13]=="LECHIFFREMENT":
        print("trouvé :",e[0],e[1])
        print(e[2][:60])
