Below are the original directions for the assignment:


Make a new program called pokemon.py that has a "Pokemon" class. In this program, "Pokemon" (objects of the class) will battle until only one is victorious. It will work similar to the Tournament program you have already created, but will read in names and elements of each Pokemon object from a file.

Download the following data file: Pokemon.txtDownload Pokemon.txt

For pokemon.py you will read in the file to use the list of every Pokémon in the Pokédex, all 1025, each Pokémon is also paired with an Element.

Elements include Grass, Fire, and Water. Now if you look at the file given you will note that on each line there is a Pokémon with its Element. Here is the code to read and scan in the code:

file = open("Pokemon.txt","r")
for n in range(1025):
   Pokemon = file.readline()
   name, element = [str(i) for i in Pokemon.split()]

In your program, make it so that every Pokemon "object" has its own name and element, at least, but also any other traits you feel are important in deciding the outcome of a battle. The code above does not do this for you. For example, you should use the Pokémon's name instead of the random names you used for parts A and B. The pokemon's  name and element must be printed in the terminal.

Pokémon elements are stronger and weaker against other elements. When 2 Pokémon are in battle you will need to check if one element has an element advantage against the other. For example, from the chart below, a Pokemon with the Electric element cannot deal damage to a Pokemon with the Ground element. The chart explains what {0, 1/2, 2} means and how they are applied. You should make and fill a matrix within your code that determines element effectiveness; otherwise, you will have to use many, many if statements.
 
Screenshot 2023-07-27 at 6.14.57 PM.png
Another way you can write this chart is:
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],
[1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],
[1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1],
[1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],
[1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5],
[1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5],
[2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5],
[1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2],
[1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2],
[1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 0.5, 1],
[1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1],
[1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5],
[1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0],
[1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5],
[1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2],
[1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1]]
 
0     = Attacking causes no damage to defender. The defender automatically wins.
1/2 = Attacking cause half it's normal damage to defender. It is random who wins, with an advantage given to the defender unless both Pokémon are equally disadvantaged.
1 = Attacker causes normal amount of damage. No changes needed.
2 = Attack causes 2x more damage points to defender. The attacker automatically wins.
 
If neither Pokemon has an advantage or disadvantage, the winner is selected similar to the method described in Part A.

The best way to implement this is to create a matrix in your program that has the values of the table above. Then, instead of having dozens of if statements for all the element combinations, just have a lookup in the matrix (where row is the attacker's element and column is the defender's element) and give advantages or disadvantages accordingly.
 
Your output to the terminal might look like this:
 
Screenshot 2023-07-27 at 6.36.47 PM.png
