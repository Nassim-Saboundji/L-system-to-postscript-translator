from constants import *
import json
from sys import argv ## to retrieve command line arguments
import json


#This function create a x.eps file with the content we provide in the template
#argument. 
def create_eps_with(template):    	
	f = open("lindenmayer.eps", "w+")
	f.write(template)
	f.close()


#This function adds new content to an already existing lidenmayer.eps
#file.
def append_eps_with(content):
    f = open("lindenmayer.eps","a+")
    f.write(content)
    f.close()


# gets a dictionnary from the json file provided in 
# the command line and returns it.(You have to provide the key
# in string associated to that dictionnary.) 
# run the python file like this: python3 traducteur.py x.json
def get_data_dico(string):
    with open(argv[1]) as my_json:
        data = json.load(my_json)
    return data[string]


def create_Ld(step):
    code = "/L:d" + step_value
    


#contains tests for now
def main():
    create_eps_with(template)
    append_eps_with(example_1)
    #create_eps_with(original_lindenmayer)
    print(get_data_dico("axiom"))
    print(get_data_dico("rules"))
    print(get_data_dico("rules")["F"])


# allows to read the main function first when the program is executed.
if __name__ == '__main__':
    main()