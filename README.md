# README

## Projet : Checker de Logique

Ce projet est un checker de logique propositionnelle qui permet aux utilisateurs de vérifier la satisfiabilité de formules propositionnelles.

## Fonctionnalités
- **Vérification de Satisfiabilité:** Détermine si une formule est satisfiable ou non.

## Installation

1. Assurez-vous d'avoir Python 3 installé sur votre système.

2. (Optionnel) Si vous préférez travailler dans un environnement virtuel, vous pouvez le créer en utilisant les étapes suivantes :
    ```
    python -m venv venv
    source venv/bin/activate  # Pour Linux/macOS
    .\venv\Scripts\activate   # Pour Windows
    ```

3. Installez les dépendances nécessaires en exécutant la commande suivante :
    ```
    pip install -r requirements.txt
    ```

## Utilisation

1. Exécutez le script principal en utilisant Python :
  ```
  python main.py #Python
  python3 main.py #Python3
  ```
2. Suivez les instructions à l'écran pour saisir votre formule logique.
3. Consultez le tableau des connecteurs logiques pour connaître les symboles utilisés par la bibliothèque sympy.
4. Pour quitter le programme, entrez simplement 'q' lorsque vous êtes invité à entrer une nouvelle formule.

## Exemple de Formule

```
(P | Q) >> (R & ~Q)
```

## Structure du Projet

- `checker.py` : Le script principal qui gère l'interaction avec l'utilisateur et l'évaluation des formules.

## Bibliothèque
Sympy : https://github.com/sympy/sympy