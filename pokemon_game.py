from random import randint

class Pokemon:
    def __init__(self, nom, pv, level, attaque, defense):
        self.nom = nom
        self.pv = pv
        self.level = level
        self.attaque = attaque
        self.defense = defense

def target():
    if randint(0, 1) == 1:
        return True
    else:
        print("L'attaque a échoué !")
        return False

class Combat:
    def __init__(self, pkmn1, pkmn2):
        self.pkmn1 = pkmn1
        self.pkmn2 = pkmn2

    def verifVie(self):
        if self.pkmn1.pv <= 0:
            print(f"{self.pkmn1.nom} à 0 PV {self.pkmn2.nom} a gagné !")
            return True
        elif self.pkmn2.pv <= 0:
            print(f"{self.pkmn2.nom} à 0 PV {self.pkmn1.nom} a gagné !")
            return True
        else:
            return False

    def winner(self):
        if self.pkmn1.pv <= 0:
            return self.pkmn2.nom
        elif self.pkmn2.pv <= 0:
            return self.pkmn1.nom
        else:
            return None

    def calculAttaque(self):
        global multiplicateur
        attaquant = self.pkmn1 if randint(0, 1) == 0 else self.pkmn2
        defenseur = self.pkmn2 if attaquant == self.pkmn1 else self.pkmn1

        if isinstance(defenseur, Eau):
            type_defenseur = "eau"
        elif isinstance(defenseur, Feu):
            type_defenseur = "feu"
        elif isinstance(defenseur, Terre):
            type_defenseur = "terre"
        elif isinstance(defenseur, Normal):
            type_defenseur = "normal"
        else:
            raise ValueError("Pokemon inconnu.")

        puissance_attaque = attaquant.attaque

        if isinstance(attaquant, Eau):
            if type_defenseur == "eau":
                multiplicateur = 1
            elif type_defenseur == "feu":
                multiplicateur = 2
            elif type_defenseur == "terre":
                multiplicateur = 0.5
            elif type_defenseur == "normal":
                multiplicateur = 1
        elif isinstance(attaquant, Feu):
            if type_defenseur == "eau":
                multiplicateur = 0.5
            elif type_defenseur == "feu":
                multiplicateur = 1
            elif type_defenseur == "terre":
                multiplicateur = 2
            elif type_defenseur == "normal":
                multiplicateur = 1
        elif isinstance(attaquant, Terre):
            if type_defenseur == "eau":
                multiplicateur = 2
            elif type_defenseur == "feu":
                multiplicateur = 0.5
            elif type_defenseur == "terre":
                multiplicateur = 1
            elif type_defenseur == "normal":
                multiplicateur = 1
        elif isinstance(attaquant, Normal):
            if type_defenseur == "eau":
                multiplicateur = 0.75
            elif type_defenseur == "feu":
                multiplicateur = 0.75
            elif type_defenseur == "terre":
                multiplicateur = 0.75
            elif type_defenseur == "normal":
                multiplicateur = 1
        else:
            raise ValueError("Type de Pokemon non reconnu.")

        puissance_attaque *= multiplicateur
        return puissance_attaque

    def enlevePv(self, pkmn, pv):
        pkmn.pv -= pv
        print(f"{pkmn.nom} a perdu {int(pv)} points de vie.")

    def loozer(self):
        if self.verifVie():
            return self.winner()
        else:
            return None

    def attaque(self):
        attaquant = self.pkmn1 if randint(0, 1) == 0 else self.pkmn2
        defenseur = self.pkmn2 if attaquant == self.pkmn1 else self.pkmn1

        if target():
            puissance_attaque = self.calculAttaque()
            pv_enleves = puissance_attaque * (100 / (100 + defenseur.defense))
            self.enlevePv(defenseur, pv_enleves)

class Feu(Pokemon):
    def __init__(self, nom, pvmax, level, attaqueFeu, defense):
        super().__init__(nom, pvmax, level, attaqueFeu, defense)
        self.attaqueFeu = attaqueFeu

class Eau(Pokemon):
    def __init__(self, nom, pvmax, level, attaqueEau, defense):
        super().__init__(nom, pvmax, level, attaqueEau, defense)
        self.attaqueEau = attaqueEau
        self.pv = pvmax

class Terre(Pokemon):
    def __init__(self, nom, pvmax, level, attaqueTerre, defense):
        super().__init__(nom, pvmax, level, attaqueTerre, defense)
        self.attaqueTerre = attaqueTerre

class Normal(Pokemon):
    def __init__(self, nom, pvmax, level, attaqueNormal, defense):
        super().__init__(nom, pvmax, level, attaqueNormal, defense)
        self.attaqueNormal = attaqueNormal

Carapuce = Eau("Carapuce", 100, 1, 10, 0)
Salameche = Feu("Salameche", 100, 1, 10, 0)

combat1 = Combat(Carapuce, Salameche)
while combat1.loozer() == None:
    combat1.attaque()
