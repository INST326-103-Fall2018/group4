Hello, welcome to Minesweeper!


This game was created by Jose Aguirre, Melvin Nava and Mahedre Samson.


Below are instructions on certain aspects of Minesweeper, as we could not program the game using pygame and other modules, but only using a random module. 


Goal


The goal of the game is to place as many “player-placed” blocks onto the grid as possible. 


Once the player places a block onto the grid, a number will appear in its place. This number will let the player know how many bombs are in the adjacent spaces. 


The player must place as many blocks onto the grid before they hit a bomb. Once the player hits a bomb, it is game over. 


Instructions


To begin, simply choose an X and a Y coordinate that will be used to place a number on the board. The player can choose to enter values which can be equal to or between 0 and 4 or equal to or between -1 and -5. If a player enters values that are not equal to the ones stated above, the game will tell the player to enter numbers that fall within those numbers. 


For example, if a player enters “X: -5 and “Y: 1”, then the coordinates will fall onto “X:0” and “Y:1”


Testing

To test this program, the user must first delete the hashtags so that the code becomes code, and no longer comments. 


To test this program, the user must change the name of the py file to “test_nameoffile”


Next, open up the command line and make sure your computer has python and pip installed


Next, in your command line, type “pip install pytest”


After py test finishes installing, locate where the py file is in your computer and find the file location. Copy the file location and type it in your command line as “cd *your file location here*”. 


Finally, run py test