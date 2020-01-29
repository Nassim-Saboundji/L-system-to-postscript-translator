from constants import *
import json
from sys import argv ## to retrieve command line arguments



#This function create a x.eps file with the content we provide in the template
#argument. 
def create_eps_with(template):    	
	f = open("resultat.eps", "w+")
	f.write(template)
	f.close()


#This function adds new content to an already existing lidenmayer.eps
#file.
def append_eps_with(content):
    f = open("resultat.eps","a+")
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


# creates the default movement code
# ex: /L:d (specific step value specified in the json) def 
# adds it to the postscript file
def create_Ld_code():
    step_value = get_data_dico("parameters")["step"]
    code = "/L:d " + str(step_value) + " def" + "\n"
    append_eps_with(code)


# creates the angle value code
# /L:a (specific angle value specified in the json) def
# # adds it to the postscript file    
def create_La_code():
    angle_value = get_data_dico("parameters")["angle"]
    code = "/L:a " + str(angle_value) + " def" + "\n"
    append_eps_with(code)


#creates the postscript code for the axiom
# if there are multiple rules the code generated allows for
# a random selection of the rule to follow.
# if there is only one rule the code for the rule is going
# to be written instead of the above.
def create_axiom_code():
    axiom = get_data_dico("axiom")
    
    operator_axiom = "/" + axiom

    rules = get_data_dico("rules")[axiom]
    print(rules)

    if len(rules) > 1 :
        #will contain the different rules for the same axiom.
        operator_table = []
        length = len(rules)

        for i in range(length):
            string = operator_axiom + str(i+1) 
            operator_table.append(string)
        print(operator_table)    
        
        operator_options = " ".join(operator_table)
        print(operator_options)

        #code is generated here with formatting.
        body = operator_axiom + "\n" + """{\n \tdup\n \t0 eq\n\t{\n\t\tL:d T:drawn
        pop\n\t}\n\t{\n\t\t1 sub\n\t\t"""+ "[" + operator_options + "]"+ """ L:rnd\n\t}ifelse
        \n}def """
        #code is written in the already made .eps file
        append_eps_with(body)
    else:
        print("Create the code directly TODO!")


#contains tests for now
def main():

    create_eps_with(template)
    create_Ld_code()
    create_La_code()
    create_axiom_code()
    #append_eps_with(example_1)
    #create_eps_with(original_lindenmayer)
    #print(get_data_dico("axiom"))
    #print(get_data_dico("rules"))
    #print(get_data_dico("rules")["F"])



# allows to read the main function first when the program is executed.
if __name__ == '__main__':
    main()
