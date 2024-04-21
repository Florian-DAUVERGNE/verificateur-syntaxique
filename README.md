# Projet : Vérificateur de Propositions Logiques

Ce projet est un vérificateur de propositions logiques basé sur la syntaxe de logique sémantique qui permet aux utilisateurs de vérifier la satisfiabilité de formules propositionnelles.

## Installation

1. Assurez-vous d'avoir Python 3 installé sur votre système.

2. Clonez ce dépôt

    ```
    git clone git@github.com:Florian-DAUVERGNE/evaluateur_de_propositions.git
    ```

 ou téléchargez les fichiers source.

![alt text]( https://bpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/b/3044/files/2021/05/github.png)

3. (Optionnel) Si vous préférez travailler dans un environnement virtuel, vous pouvez le créer en utilisant les étapes suivantes :
    ```
    python -m venv venv
    source venv/bin/activate  # Pour Linux/macOS
    .\venv\Scripts\activate   # Pour Windows
    ```

4. Installez les dépendances nécessaires en exécutant la commande suivante :
    ```
    pip install -r requirements.txt
    ```

## Utilisation

1. Exécutez le script principal en utilisant Python :
  ```
  python VerificateurSyntaxique.py #Python
  python3 VerificateurSyntaxique.py #Python3
  ```
2. Suivez les instructions à l'écran pour saisir votre formule logique.
3. Pour quitter le programme, entrez simplement 'q' lorsque vous êtes invité à entrer une nouvelle formule.

## Exemple de Formule

```
(P | Q) >> (~r = (Q & P))
```

## Structure du Projet

- `VerificateurSyntaxique.py` : Le script principal qui gère l'interaction avec l'utilisateur et l'évaluation des formules.

## Bibliothèque
Sympy : https://github.com/sympy/sympy

terminaltables : https://pypi.org/project/terminaltables/

re : https://docs.python.org/fr/3/library/re.html