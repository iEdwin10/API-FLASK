class Voiture:
    def __init__(self, marque, modele, x, y):
        self.marque = marque
        self.modele = modele
        self.x = x
        self.y = y
    
    def avancer(self):
        self.x += 1
    
    def reculer(self):
        self.x -=1

    def gauche(self):
        self.y += 0.1
    
    def droite(self):
        self.y -= 0.1
    
    def display(self):
        print(f"Position actuelle de la voiture {self.marque}: ({self.x}, {self.y})")


# Exemple d'utilisation
ma_voiture = Voiture("Toyota", "Corolla", 0,0)
ma_voiture.avancer()
ma_voiture.reculer()
ma_voiture.droite()
ma_voiture.gauche()
ma_voiture.display()