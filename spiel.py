# 1. Spielbrett

def spielbrett():
    brett = []
    
    for i in range(3):              # range() beschreibt eine Zählsequenz bis zum angegebenm Argument
        zeile = [" ", " ", " "]
        brett.append(zeile)

    return brett


# 2. Spielbrett anzeigen

def spielbrett_anzeigen(brett):
    
    for zeile in brett:
        print("|".join(zeile))
        print("------")


# 3. Zug machen

def mache_zug(brett, spieler, zeile, spalte):
    if brett[zeile][spalte] == " ":
        brett[zeile][spalte] = spieler
        return True
    else:
        return False


# 4. Gewinnen überprüfen

def gewinnen(brett, spieler):
    for zeile in range(3):
        if brett[zeile][0] == brett[zeile][1] == brett[zeile][2] == spieler:
            return True

    for spalte in range(3):
        if brett[0][spalte] == brett[1][spalte] == brett[2][spalte] == spieler:
            return True
        
    if brett[0][0] == brett[1][1] == brett[2][2] == spieler or \
       brett[0][2] == brett[1][1] == brett[2][0] == spieler:
        return True


# 5. Unentschieden Prüfen
def unentschieden(brett):
    for zeile in brett:
        if " " in zeile:
            return False
    return True


# 6. Hauptprogramm
def spiele_tic_tac_toe():
    brett = spielbrett()
    aktueller_spieler = "X"

    while True:
        spielbrett_anzeigen(brett)
        zeile = int(input(f"Spieler {aktueller_spieler}, wähle deine Zeile. (0 - 2)"))
        spalte = int(input(f"Spieler {aktueller_spieler}, wähle deine Zeile. (0 - 2)"))

        if not mache_zug(brett, aktueller_spieler, zeile, spalte):
            print("Versuch es nochmal")
            continue

        if gewinnen(brett, aktueller_spieler):#
           spielbrett_anzeigen(brett)
           print(f"{aktueller_spieler} Du hast gewonnen.")
           break
        
        elif unentschieden(brett):
            spielbrett_anzeigen(brett)
            print("Unentschieden.")
            break
        aktueller_spieler = "O" if aktueller_spieler == "X" else "X"
spiele_tic_tac_toe()