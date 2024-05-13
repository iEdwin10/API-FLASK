import random

# eleve1 ={
#     "nom" : "Edwin",
#     "age" : 22,
#     "classe" : "devo23"
# }

# tab ={
#     "key1" : 5,
#     "key2" : 87,
#     "key3" : 6,
#     "key4" : 9,
#     "key5" : 14
# }

# print(eleve1["nom"])

# list = [1,6,8]
# for n in list : 
#     print (n)

# def somme(a,b,c):
#     return a+b+c

# sum = somme(1,5,2)
# print (sum)
    

# def randomsomme():
#     n1 = random.randint(0,200)
#     n2 = random.randint(0,100)
#     somme = n1+n2
#     return somme

# test = randomsomme()
# print(test)

# def randomsomme(maximum):
#     n1 = random.randint(0,maximum)
#     n2 = random.randint(0,maximum)
#     somme = n1+n2
#     return somme

# list = [4,8,67,29,3]

# def choicesomme():
#     nb1 = random.choice(list)
#     print(nb1)
#     nb2 = random.choice(list)
#     print(nb2)
#     result = nb1+nb2
#     return result

# test = choicesomme()
# print(test)


def aleatoire(choice_or_randint, list=[] ,min=0,max=0):
    if choice_or_randint == True:   
        return random.randint(min,max) 

    else: 
        return random.choice(list)
    
# Ici je tire un nombre aléatoire parmi la liste fourni en paramètre 
print(aleatoire(False, list = [9,0,20,8,7,22,100,199992])) 

# Ici je trie un élément aléatoire entre max et min 
print(aleatoire(True, min=999, max=1000)) 