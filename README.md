# elementary-cellular-automaton
Used Tkinter and webbrowser libraries with Python in order to implement the simle elementary cellular automaton explained in the following sources:   
http://mathworld.wolfram.com/ElementaryCellularAutomaton.html
https://natureofcode.com/book/chapter-7-cellular-automata/

## About
Cellular automata are models used to simulate and study social self organization.  
Examples of self-organization include crystallization, how people live in a city,thermal convection of fluids, chemical oscillation, animal swarming, neural circuits, and artificial neural networks.   
A cellular automaton consists of a regular grid of cells, each in one of a finite number of states, such as on and off.  
The grid can be in any finite number of dimensions. For each cell, a set of cells called its neighborhood is defined relative to the specified cell. An initial state (time t = 0) is selected by assigning a state for each cell. A new generation is created (advancing t by 1), according to some fixed rule that determines the new state of each cell in terms of the current state of the cell and the states of the cells in its neighborhood.  
The simplest one is the elementary cellular automaton. 

## Version 1.0
- used Tkinter  to implement the GUI  

![gui example](https://github.com/mageirakos/elementary-cellular-automaton/blob/master/img/gui-example.png?raw=true)

- used webbrowser to learn the library and implement a couple of links to interesting sources  
- all 255 rules can are simulated correctly  
- made sure to not have any errors occur through the use of python exceptions  
- all 4 classes of cellular automata can be seen in the different rules of my implementation   

### Class 1 showing Uniformity  
![class 1](https://github.com/mageirakos/elementary-cellular-automaton/blob/master/img/rule%20222%20uniformity%20(%201%20category%20).png?raw=true)  
### Class 2 showing Repetition  
![class 2](https://github.com/mageirakos/elementary-cellular-automaton/blob/master/img/rule%20190%20repetition%20(%202nd%20category%20).png?raw=true)  
### Class 3 showing Instability  
![class 3](https://github.com/mageirakos/elementary-cellular-automaton/blob/master/img/rule%2030%20instability%20(%203rd%20category%20).png?raw=true)  
### Class 4 showing Complexity  
![class 4](https://github.com/mageirakos/elementary-cellular-automaton/blob/master/img/rule%20110%20repetition%20and%20complexity%20(4th%20category).png?raw=true)  
