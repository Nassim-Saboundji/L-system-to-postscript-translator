![](https://i.ibb.co/yPFQFtj/rsz-202002021605511000.jpg)

# L-system-to-postscript-translator
A python program that takes an L-System and outputs a Postscript program that draws plants or other shapes.

An L-system is a set of rules and and axiom that is used to model the growth of plants. It's also used in various other applications. (Conway's game of life is familiar to the L-System concept) If you want more details on the topic https://en.wikipedia.org/wiki/L-system


My program takes in json file that contains rules and an axiom and outputs a postscript file.
This postscript file when opened presents a drawing that was made following the rules of that L-System in the json file.

To run my program, simply type this command after having pointed your terminal to the location where translator.py is:

`python3 translator.py your_file.json [a number from 1 to ... which represents the number of iterations.]`

![](https://i.ibb.co/g9hF6jL/202002021605511001.jpg)
