from sys import argv ## pour permettre la lecture en ligne de commande
import json


# gets a dictionnary from the json file provided in 
# the command line and returns it. Provide the key
# in string associated to that dictionnary. 
# run the python file like this: python3 name.py name.json
def get_data_dico(string):
    with open(argv[1]) as my_json:
        data = json.load(my_json)
    return data[string]

print(get_data_dico("axiom"))
print(get_data_dico("rules"))
print(get_data_dico("rules")["F"]) 