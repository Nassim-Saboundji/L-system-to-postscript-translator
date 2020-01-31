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


# will return an operator table that will be used
# to create the code for each one of them.

#symbol parameter is None when we want the axiom code
#otherwise we can provide the symbol for any other we want the rules for.
def create_axiom_code(symbol):
    axiom = get_data_dico("axiom")
    
    

    if symbol != None :
        rules = get_data_dico("rules")[symbol]
        operator_axiom = "/" + symbol
    else:
        rules = get_data_dico("rules")[axiom]
        operator_axiom = "/" + axiom
    #print(rules)

    if len(rules) > 1 :
        #will contain the different rules for the same axiom.
        operator_table = []
        length = len(rules)

        for i in range(length):
            string = operator_axiom + str(i+1) 
            operator_table.append(string)
        print(operator_table)    
        
        
        operator_options = " ".join(operator_table)
        #print(operator_options)

        #code is generated here with formatting.
        body = operator_axiom + "\n" + """{\n \tdup\n \t0 eq\n\t{\n\t\tL:d T:draw
        pop\n\t}\n\t{\n\t\t1 sub\n\t\t"""+ "[" + operator_options + "]"+ """ L:rnd\n\t}ifelse
        \n}def\n"""
        #code is written in the already made .eps file
        append_eps_with(body)
        return operator_table
    else:
        if symbol != None:
            create_rule_code(symbol, 0, True, None)
        else:
            create_rule_code(axiom, 0, True, None)    
       
        return -1



# TODO!
# create code for other rules that have multiple versions
# will likely call creator_operator_code
# will be similar to create_axiom_code except that 
# it will be with any rule that isn't the axiom and has
# multiple versions.
#def create_expansion_code():


#take a symbol of type string
# from the actions and returns the associated
# postscript code for this action.
def action_detector(action_symbol):
    #will get the action associated to a symbol
    #i.e: "]" => "pop" action = "pop"
    action = get_data_dico("actions")[action_symbol]
    
    switcher = {
        "draw" : "dup " + action_symbol,
        "turnL" : "L:a neg T:turn",
        "turnR" : "L:a T:turn",
        "push": "gsave",
        "pop": "grestore"
    }
    return switcher.get(action, "nothing") 


#creates postscript code for a given rule.
#specificing the version which is an index when multiple rules
#exists for a given symbol. 0 1 2 --> 3 versions of the expansion exists
# at index 0 1 and 2

# the only_one? argument is a boolean that tells the function
# if or if not there exist only one version of the expansion of the rule_symbol provided.

# title_number specifiy which version of the rule if there is more than one rule
# otherwise you can put None
def create_rule_code(rule_symbol, version, only_one, title_number):
    
    # the rule is given back as a string ex: "FF-[-F+F+F]+[+F-F-F]"
    rule = get_data_dico("rules")[rule_symbol][version]
    
    code_table = []
    
    if only_one == False: #this rule has multiple extension possible
        for i,symbol in enumerate(rule):
            if rule.rfind(rule_symbol) == i: #rfind finds the index of the last occurence
                code_table.append(symbol)    #of the rule_symbol in the string "rule".
            else:
                code_table.append(action_detector(symbol))

        #generates the postscript code.
        append_eps_with("/" + rule_symbol + str(title_number) + "\n")
        append_eps_with("{\n")
        for code in code_table:
            append_eps_with("\t" + code + "\n")
        append_eps_with("\n}def\n")        
                
    else: #this rule only has one expansion possible.

        for i,symbol in enumerate(rule):
            if rule.rfind(rule_symbol) == i: #rfind finds the index of the last occurence
                code_table.append(symbol)    #of the rule_symbol in the string "rule".
            else:
                code_table.append(action_detector(symbol))

        append_eps_with("/" + rule_symbol + "\n")
        append_eps_with("{\n")
        append_eps_with("\tdup 0 eq \n")
        append_eps_with("\tpop\n")
        append_eps_with("\t{\n")
        append_eps_with("\t L:d T:draw \n")
        append_eps_with("\t}{\n")
        for code in code_table:
            append_eps_with("\t\t" + code + "\n")
        append_eps_with("\t}ifelse \n")
        append_eps_with("}def\n")

    return code_table
        


# creates the code for every different expansion version of a rule 
# operators is a list containing string names for each the versions of a rule.
# symbol is the symbol of the left side of a rule example: F -> F-F 
def create_operator_code(operators, symbol):
    nb_operators = len(operators)
    
    for i in range(nb_operators):
        create_rule_code(symbol, i, False, i+1)
    



#contains tests for now
def main():

    create_eps_with(template)
    create_Ld_code()
    create_La_code()

    # checks for each rule in our rules
    for rule in get_data_dico("rules"):
        if rule == get_data_dico("axiom"):
            #we generate generate code for the axiom
            #None propriety is telling us that
            operator_table = create_axiom_code(None) #contains a list of operators we 
            # need to write code for or -1 if not.
            if operator_table != -1: #we have operators therefore 
                #we create code for each operator.
                create_operator_code(operator_table, get_data_dico("axiom")) 
        else:
            # if it's not the axiom we generate code for our rule.                       
            operator_table = create_axiom_code(rule)
            if operator_table != -1: #we have operators therefore...
                create_operator_code(operator_table, rule)

    
    #checks if we have operators we need to create the code
    #for. #creates the axiom code and returns a list if 
    #there is multiple versions possible. if not
    # operator_table = -1
    #operator_table = create_axiom_code(None) 
    #if operator_table != -1:
    #    print("we have operators")
    #    create_operator_code(operator_table, get_data_dico("axiom"))

    #if len(get_data_dico("rules")) > 1:
    #    print("there is something else we need to generate code for")
    #    for rule in get_data_dico("rules"):
    #        print(rule)
    #        if rule == get_data_dico("axiom"):
    #            print("skip it")
    #        else:
    #            print("create rule for it")
    #            create_axiom_code(rule)

    #print(create_rule_code("F", 0, False))
    #print(create_rule_code("F", 0, True))
    #print(action_detector("F"))
    #append_eps_with(example_1)
    #create_eps_with(original_lindenmayer)
    #print(get_data_dico("axiom"))
    #print(get_data_dico("rules"))
    #print(get_data_dico("rules")["F"])



# allows to read the main function first when the program is executed.
if __name__ == '__main__':
    main()