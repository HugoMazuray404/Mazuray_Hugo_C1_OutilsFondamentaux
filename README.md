# Mazuray_Hugo_OutilsFondamentaux
# Le problème du voyageur de commerce

## Présentation du projet

Ce projet porte sur le **problème du voyageur de commerce**, un problème d'optimisation qui consiste à déterminer le plus court trajet permettant de visiter un ensemble de villes, en passant une seule fois par chacune d'elles, avant de revenir au point de départ.

Le projet s'appuie sur un sujet de départ consacré au voyageur de commerce, utilisant un ensemble de **58 villes françaises**.

Cependant, ce sujet initial ne permettait pas d'aborder suffisamment toutes les notions mathématiques étudiées en travaux pratiques. J'ai donc choisi de **conserver le sujet initial et d'y ajouter de nouvelles questions**, afin d'approfondir le problème et de mieux répondre aux attentes du projet personnel.

L'objectif n'est donc pas uniquement de trouver un parcours court, mais aussi de comprendre et de comparer les différentes méthodes mathématiques et informatiques utilisées pour résoudre ce problème.

## Arboréssance
├── Tp
│   ├── Tp1
│   ├── Tp2
│   ├── Tp3
│   ├── Tp4
│   ├── Tp5
│   └── Tp6
└── projet
    ├── Sujet_Voyageur_remanié.pdf
    ├── Villes.txt
    └── Algo_Voyageur_remanié.py

## Fonctionnement du projet

Il permet notamment, selon les parties :

- de charger les coordonnées géographiques des villes ;
- de représenter graphiquement un parcours ;
- de calculer la distance entre deux villes ainsi que la longueur totale d'un parcours ;
- de rechercher des parcours courts à l'aide de différentes méthodes ;
- d'étudier les performances de ces méthodes ;
- d'analyser l'influence des paramètres et de certaines approximations numériques sur les résultats.

Le problème présente une difficulté importante : le nombre de parcours possibles augmente très rapidement avec le nombre de villes.

Une recherche exhaustive devient donc rapidement irréalisable. Le projet explore ainsi des méthodes permettant de trouver de bons parcours sans nécessairement examiner toutes les possibilités.

## Lancement du programme

### Prérequis

Pour exécuter le programme, il faut disposer de :

- Python 3 ;
- des bibliothèques Python utilisées dans le code, notamment `numpy` et `matplotlib` ;
- du fichier contenant les coordonnées des villes (`Villes.txt`) (évidement présent sur le github).

### Exécution

1. Télécharger les fichiers du projet.
2. Placer le programme Python et le fichier `Villes.txt` dans le même dossier.
3. Exécuter le programme Python depuis ce dossier

Certaines parties du programme correspondent à des fonctions indépendantes. Leur exécution peut nécessiter de les appeler explicitement dans le code, avec les paramètres souhaités.

## Résultats et observations attendus

Ce projet doit permettre d'observer plusieurs phénomènes.

### 1. La difficulté du problème

Le nombre de parcours possibles augmente très rapidement lorsque le nombre de villes augmente.

On doit notamment constater que la recherche exhaustive peut fonctionner pour un petit ensemble de villes, mais qu'elle devient trop coûteuse pour un ensemble plus important.

### 2. L'efficacité des méthodes d'optimisation

Les différentes méthodes étudiées ne fournissent pas nécessairement les mêmes résultats.

Les expériences doivent permettre de comparer :

- les longueurs des parcours obtenus ;
- les temps de calcul ;
- la stabilité des résultats entre plusieurs exécutions ;
- l'influence des paramètres de chaque méthode.

L'objectif est de déterminer quelles méthodes offrent le meilleur compromis entre qualité du parcours et coût de calcul.

### 3. L'influence des méthodes mathématiques

Les questions supplémentaires doivent permettre d'étudier :

- les écarts entre différentes formules de calcul des distances ;
- les limites de l'approximation de la Terre par un plan ;
- l'intérêt d'une matrice des distances pour accélérer certains calculs ;
- l'utilisation de systèmes linéaires pour déterminer une fonction polynomiale ;
- la recherche numérique de racines ;
- l'influence d'une nouvelle loi de refroidissement sur les résultats des algorithmes ;
- l'utilisation de l'arithmétique modulaire pour construire des parcours.

Les résultats doivent être accompagnés, lorsque cela est pertinent, de tableaux, de graphiques et d'explications.

## Organisation du travail

Le sujet est organisé sous forme de questions progressives.

Les **questions Q1 à Q18** correspondent au sujet initial. Les questions suivantes ont été ajoutées afin de couvrir davantage de notions du cours et de développer une étude plus approfondie.

Les nouvelles questions peuvent réutiliser les fonctions, calculs et graphiques précédents, mais elles doivent apporter leurs propres fonctions ou méthodes lorsque cela est nécessaire.

Ce fonctionnement permet de conserver les différentes approches et de les comparer par la suite.

## Limites et perspectives du projet

Les questions Q15 à Q18, consacrées à des méthodes supplémentaires d'optimisation des parcours, n'ont pas toutes été réalisées par manque de temps.

J'ai choisi de donner la priorité à l'étude d'autres aspects mathématiques du problème du voyageur de commerce, notamment la précision des calculs, la géométrie, les matrices, les polynômes et la recherche de racines.

Ces questions constituent des pistes d'amélioration qui pourraient être étudiées dans une version ultérieure du projet.

Les méthodes d'optimisation utilisées ne garantissent pas nécessairement de trouver le parcours optimal. Les résultats obtenus doivent donc être interprétés comme des solutions approchées, sauf lorsqu'une recherche exhaustive permet de vérifier leur optimalité.

## Utilisation de l'intelligence artificielle

Une intelligence artificielle a été utilisée comme aide à la réflexion et à la rédaction pour identifier les notions mathématiques insuffisamment abordées dans le sujet initial, proposer des questions complémentaire. Elle a également été utilisée pour corriger du code ou clarifier des consignes incomprises.
