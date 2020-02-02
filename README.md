![](https://i.ibb.co/sVqHrfB/202002021605511000.jpg){:height="50%" width="50%"}

# L-system-to-postscript-translator
A python program that takes an L-System and outputs a Postscript program that draws plants or other shapes.

An L-system is a set of rules and and axiom that is used to model the growth of plants. It's also used in various other applications. (Conway's game of life is familiar to the L-System concept) 

My program takes in json file that contains rules and an axiom and outputs a postscript file.
This postscript file when opened presents a drawing that was made following the rules of that L-System in the json file.

To run my program, simply type this command:

python3 traducteur.py your_file.json [a number from 1 to ... which represents the number of iterations.]

