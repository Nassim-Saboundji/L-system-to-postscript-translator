from constants import *


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


def main():
    create_eps_with(template)
    append_eps_with(example_1)
    #create_eps_with(original_lindenmayer)


# allows to read the main function first when the program is executed.
if __name__ == '__main__':
    main()