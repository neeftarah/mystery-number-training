# Apprendre à programmer par le jeu

L'objectif de cette série est d'apprendre les bases de la programmation dans divers langages autour d'un jeu simple.
Elle est destinées aux débutants en programmation ou aux développeurs souhaitant apprendre rapidement les bases d'un autre langage.

Les principes de programmation nécessaires seront expliqués dans ce document de manière générale, puis chaque dossier correspondant à un langage de programmation contiendra un ficher d'explications détaillée comme celui-ci pour le langage en question afin de présenter la syntaxe de chaque langages.


## Le jeu du nombre mystère
### Principe du jeu
Le jeu du nombre mystère également appeler jeu du Plus ou Moins est un grand classique de la programmation.
Il s'agit de trouver un nombre choisit aléatoirement en proposant successivement différents nombres.
Le programme nous renvoi alors un message nous indiquant si le nombre aléatoire est plus petit ou plus grand que le nombre saisi.

### Les besoins du jeu
Afin de réaliser notre jeu avec le maximum d'options, nous devront apprendre à utiliser :

1. les variables
2. Les conditions
3. les boucles
4. La génération de nombre aléatoire
5. L'affichage de texte à l'écran
6. La récupération de texte saisi
7. La vérification du type de donnée attendu
8. La gestion des erreurs
9. La gestion du temps
10. La lecture et l'écriture dans un fichier
11. La gestion de traductions multiples

### Fonctionnalités attendues
#### 1. Affichage d'un message de présentation
Tout d'abord, nous afficherons un message de présentation qui restera afficher 3s.

#### 2. Choix de la langue
Les différentes langues disponibles sont présentées au joueur qui devra choisir celle qu'il souhaite.
En fonction de sa saisie, le fichier de langue correspondant est chargé.

#### 3. Difficulté
Un 1er menu propose de choisir une difficulté :

1. De 1 à 100
2. De 1 à 1000
3. De 1 à 10 000
4. Personnalisé

#### 3. (bis) Difficulté personnalisée
Si la difficulté choisie est "4. Personnalisé", le programme invite le(s) joueur(s) à saisir le nombre maximum souhaité (inférieur à la taille d'un "_entier long non-signé_")

#### 4. Mode de jeu
Le jeu pourra être jouer à un ou deux joueurs.

1. **Le mode SOLO :** L'ordinateur choisit un nombre aléatoire et le joueur doit le trouver.
2. **Le mode MULTI :** Le joueur 2 commence par saisir un nombre que le joueur 1 doit trouver, puis le joueur 1 propose un nombre à son tour que le joueur 2 doit trouver. Le joueur ayant trouver le nombre mystère avec le moins de proposition gagne.

Un menu demandera quel mode de jeu utiliser.

#### 5. Pseudo du/des joueur(s)
Le programme demande le(s) nom(s) du/des joueur(s). et le(s) stock.

#### 6. Déroulement d'une partie
Le programme invite le joueur à saisir un nombre entre 0 et le maximum choisi par la difficulté.

Le joueur saisie un nombre :

* Si le joueur n'a pas saisie un nombre valide, le programme en informe le joueur et lui demande à nouveau de saisir un nombre.
* Si le nombre saisie est plus petit que le nombre mystère, le programme affiche "Le nombre mystère est plus grand !"
* Si le nombre saisie est plus grand que le nombre mystère, le programme affiche "Le nombre mystère est plus petit !"
* Si le nombre saisie est égal au nombre mystère, la partie est gagnée, le programme affiche "BRAVO ! Vous avez trouver le nombre mystère en X coups et Y secondes". Le score du joueur est afficher en dessous dans une liste des 10 meilleurs scores.

A chaque proposition d'un nombre valide, le compteur de coup (X) est incrémenté de 1.

Un chronomètre est démarré en début de partie (au 1er nombre saisie) et représente le temps de jeu (Y).


#### 7. Score
Une fois la partie terminé, le score est calculé comme suit et est afficher avec les 10 meilleurs scores.
Si le score du joueur est parmi les 10 meilleurs, son score, son pseudo, le nombre de coups, la difficulté, le temps mis et la date sont stockés dans un fichier texte au format CSV.

* Score = Nombre maximum - nombre de coup + Nombre maximum - temps écoulé en secondes.

#### 8. Nouvelle partie
S'il s'agit d'une partie MULTI, le joueur 2 joue sa partie et les scores des 2 joueurs sont comparés.

S'il s'agit d'une partie SOLO ou que le 2e joueur a déjà joué sa partie, le programme propose au(x) joueur(s) de faire une nouvelle partie (avec les même paramètres).
Un nouveau nombre aléatoire est alors choisit et la partie recommence.

Si le(s) joueur(s) ne souhaite(nt) pas rejouer, un message de remerciement s'affiche puis le programme se termine à l'appui de n'importe quelle touche.

## La programmation
### les variables

### Les conditions

### les boucles

### La génération de nombre aléatoire

### L'affichage de texte à l'écran

### La récupération de texte saisi

### La vérification du type de donnée attendu

### La gestion des erreurs

### La gestion du temps

### La lecture et l'écriture dans un fichier

### La gestion de traductions multiples

## Contribution
Toute contribution est la bienvenue !

L'objectif de ce programme est de découvrir et de faire découvrir de nouveaux langages de programmation.

Si vous souhaitez contribué, vous pouvez :

* **Proposer un nouveau langage de programmation** avec **les fichiers sources** du jeu dans ce langage et un **fichier README** détaillant la syntaxe et les particularités du langage
* **Proposer une nouvelle traduction** (des fichiers README et des traductions du jeu) **ou des corrections** d'orthographe ou de traduction.
* **Proposer des améliorations** sur les codes sources d'un ou plusieurs langages
* **En faisant connaître ce dépôt**.
