# class Voiture:
#     def __init__(self, marque, modele, x, y):
#         self.marque = marque
#         self.modele = modele
#         self.x = x
#         self.y = y
    
#     def avancer(self):
#         self.x += 1
    
#     def reculer(self):
#         self.x -=1

#     def gauche(self):
#         self.y += 0.1
    
#     def droite(self):
#         self.y -= 0.1
    
#     def display(self):
#         print(f"Position actuelle de la voiture {self.marque}: ({self.x}, {self.y})")


# # Exemple d'utilisation
# ma_voiture = Voiture("Toyota", "Corolla", 0,0)
# ma_voiture.avancer()
# ma_voiture.reculer()
# ma_voiture.droite()
# ma_voiture.gauche()
# ma_voiture.display()

# AUTRE METHODE AVEC UNE FONCTION TOURNER PERSO ***********************************************

# Constructeur de la classe Voiture 
class Voiture: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

    def avancer(self): 
        self.x += 1 
        print(f"La voiture est à la position {self.x}, {self.y}") 
        return self.x, self.y 

    def reculer(self): 
        self.x -= 1 
        print(f"La voiture est à la position {self.x}, {self.y}") 
        return self.x, self.y 

    def tourner(self, direction): 
        if direction == "droite": 
            self.y -= 0.1 
            print(f"La voiture est à la position {self.x}, {self.y}") 
        if direction == "gauche": 
            self.y += 0.1 
            print(f"La voiture est à la position {self.x}, {self.y}") 
        else: 
            print(f"La voiture est à la position {self.x}, {self.y}") 
        return direction 
# Créer une instance de la classe Voiture 

voiture = Voiture(0, 0) 
voiture.avancer() 
voiture.tourner("gauche") 