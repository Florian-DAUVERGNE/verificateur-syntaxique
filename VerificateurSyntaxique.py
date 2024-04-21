from sympy.logic.boolalg import to_cnf
from sympy.logic.inference import satisfiable
from terminaltables import AsciiTable
import re


def convertir_implication(expression):
    # Convertir l'équivalence (=) en formule avec des opérateurs logiques
    expression_convertie = re.sub(
        r'(\([^()]*\)|[A-Za-z])\s*=\s*(\([^()]*\)|[A-Za-z])', r'((\1 & \2) | (~\1 & ~\2))', expression)

    return expression_convertie


def est_satisfaisable(proposition):
    """Résoudre la satisfiabilité de la formule propositionnelle"""

    # Convertir l'équivalence (=) en formule avec des opérateurs logiques
    proposition = convertir_implication(proposition)

    # Convertir la formule pour qu'elle soit utilisée avec sympy
    proposition = to_cnf(proposition)

    # Résoudre la satisfiabilité de la formule
    return satisfiable(proposition)


# Définition du tableau des correspondances connecteur / symbole
correspondance = AsciiTable([
    ["Connecteur", "Symbole"],
    # Connecteur correspondant au symbole de négation
    ["Négation (¬)",    "~"],
    # Connecteur correspondant au symbole de conjonction
    ["Conjonction (∧)", "&"],
    # Connecteur correspondant au symbole de disjonction
    ["Disjonction (∨)", "|"],
    # Connecteur correspondant au symbole d'implication
    ["Implication (→)", ">>"],
    # Connecteur correspondant au symbole d'équivalence
    ["Équivalence (↔)", "="]
]).table

# Affichage du message d'aide
print("\n-----Taper votre formule (exemple : (P | Q) >> (~r = (Q & P))-----\n")
print("Tableau de correspondance :\n")
# Affichage de la table de correspondance
print(correspondance)


while True:
    # Demander à l'utilisateur de saisir la formule propositionnelle
    proposition = input(
        "\nEntrez la formule propositionnelle ou tapez 'q' pour quitter : ")

    # Terminer le programme si l'utilisateur tape 'q'
    if proposition.lower() == 'q':
        print("Programme terminé.")
        break

    # remplacer les majuscules par les minuscules
    proposition = proposition.lower()

    # Vérifier la satisfiabilité de la formule propositionnelle
    if est_satisfaisable(proposition):
        print("La formule est satisfiable.")
    else:
        print("La formule n'est pas satisfiable.")

    # Demander à l'utilisateur s'il souhaite entrer une nouvelle formule
    response = input("Voulez-vous entrer une nouvelle formule ? (Oui/Non) : ")
    if response.lower() != 'oui' and response.lower() != 'o':
        print("Programme terminé.")
        break
