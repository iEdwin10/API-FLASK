from flask import Flask
import requests

app = Flask(__name__)

@app.route("/bonjour/")
def hello_world():
    print("<p>Hello, World!</p>")
    return "ok"

@app.route("/goodbye/")
def goodbye():
    return "Goodbye"

# @app.route("/pokemon/<name>")
# def pokemon(name):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         pokemon_name = pokemon_data['name']
#         return f"C'est le pokemon : {pokemon_name}"
#     elif response.status_code == 404:
#         return "Le Pokemon n'exsite pas"

# @app.route("/pokemon/<name>")
# def pokemon(name):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
#     try:
#         pokemon_data = response.json()
#         pokemon_name = pokemon_data['name']
#         return f"C'est le pokemon : {pokemon_name}"
#     catch:
#         return "Le Pokemon n'exsite pas"


# @app.route("/pokemon/<name1>/<name2>")
# def peser(name1,name2):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name1}/name{pokemon_name2}")
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         pokemon_name1 = pokemon_data['name']
#         pokemon_name2 = pokemon_data['name']
#         pokemon_weight1 = pokemon_data['weight']
#         pokemon_weight2 = pokemon_data['weight']
#         if pokemon_weight1 > pokemon_weight2 : 
#             return f"{pokemon_name1} est plus lourd"
#         elif pokemon_weight1 < pokemon_weight2:
#             return f"{pokemon_name2} est plus lourd"
#         else :
#             return f"{pokemon_name1} et {pokemon_name2} ont le meme poids."
        
#     elif response.status_code == 404:
#         return "Le(s) Pokemon(s) n'exsite pas"

@app.route("/find/<univers>/<name>")
def pokemon(univers, name):
    if univers == "sw":
        response = requests.get(f"https://swapi.dev/api/people/{name}/")
        data = response.json()
        sw_name = data['name']
        return sw_name
    elif univers =="pk":
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        data = response.json()
        pk_name = data['name']
        return pk_name
    else:
        return "Univers not found"




app.run()



