import requests # Import de la lib request

def peser(name1,name2) : # Création de la fonction peser
    pokemon1_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name1}").json() # Récuperer les information du code de l'API
    pokemon2_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name2}").json()
    weight1 = pokemon1_data["weight"] # Créer une variable qui contiendra la valeur du poid du 1er Pokemon
    weight2 = pokemon2_data["weight"] # Créer une variable qui contiendra la valeur du poid du 2eme Pokemon

    if weight1 > weight2 : 
        print(f"{name1} est plus lourd que {name2}.")
    elif weight1 < weight2 :
        print(f"{name2} est plus lourd que {name1}.")
    else :
        print(f"{name1} et {name2} font le meme poids")

print (peser("blaziken", "pikachu")) #Appel de la fonction en insérant 2 pokemons a comparer 

