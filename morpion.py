plateau_jeu = {
    "case1": "_",
    "case2": "_",
    "case3": "_",
    "case4": "_",
    "case5": "_",
    "case6": "_",
    "case7": "_",
    "case8": "_",
    "case9": "_"
}

def affichage(plateau):
    print(f"{plateau['case1']} | {plateau['case2']} | {plateau['case3']}")
    print(f"{plateau['case4']} | {plateau['case5']} | {plateau['case6']}")
    print(f"{plateau['case7']} | {plateau['case8']} | {plateau['case9']}")

def verifVictoire(player,plateau):
    if ((plateau["case1"] == player and plateau["case2"] == player and plateau["case3"] == player) or
        (plateau["case4"] == player and plateau["case5"] == player and plateau["case6"] == player) or
        (plateau["case7"] == player and plateau["case8"] == player and plateau["case9"] == player) or
        (plateau["case1"] == player and plateau["case4"] == player and plateau["case7"] == player) or
        (plateau["case2"] == player and plateau["case5"] == player and plateau["case8"] == player) or
        (plateau["case3"] == player and plateau["case6"] == player and plateau["case9"] == player) or
        (plateau["case1"] == player and plateau["case5"] == player and plateau["case9"] == player) or
        (plateau["case3"] == player and plateau["case5"] == player and plateau["case7"] == player)):
        return player
    else:
        return None

def initGame():
    joueur1 = "X"
    joueur2 = "O"
    gagnant = None
    plateau = plateau_jeu.copy()
    affichage(plateau)
    i = 0
    while gagnant == None:
        player = joueur2 if i % 2 else joueur1
        coup = input(f"joueur {player}, choisissez une case : ")
        try:
            if plateau[f"case{coup}"] == "_":
                plateau[f"case{coup}"] = player
                i += 1
                print(i)
            else:
                print("Cette case à déjà été choisi par votre adversaire")
            affichage(plateau)
            gagnant = verifVictoire(player,plateau)
            if gagnant == None and i == 9 :
                break
        except:
            print("Veuillez entrer un numéro entre 1 et 9 pour sélectionner la case voulu")
    return "Pas de gagnant aujourd'hui! Retentez votre chance!" if gagnant == None else f"Victoire du joueur {player}, félicitations!"

print(initGame())