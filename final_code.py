import random
import pytest


#This class and functions were created by Melvin Nava
class Tile(object):
   value = 0 #this is the blank spot property
   chosen = False #Assigns a property of chosen that remains false
   bomb = False #assigns a bomb property that remains false


   def __init__(self):
       self.chosen = False #each tile becomes not chosen as the board gets built


   def __str__(self):
       return str(Tile.value)


   def isbomb(self): #see if a tile is a bomb, if -1 set to true
       if Tile.value == -1:
           return True
       else:
           return False


#This class was created by Jose Aguirre and Melvin Nava. The creator of specific functions will be stated in the first function they created to reduce clutter
class gameboard(object):


   #Functions hitbomb, gamewon, __init__, __str__. and addbomb and the overall structure of the class gameboard was created by Jose Aguirre
   def hitbomb(self, x, y): #should return false if the user-inputted coordinates are not on a bomb (-1)
       return self.board[x][y].value == -1


   def gamewon(self):  #when there are no more tiles that can be uncovered
       return self.options == 0


   def __init__(self, boardSize, numbombs):
       """boardSize begins at 0 and begins to cycle through 0-4 for 5 total values in both length and witdth, at
       the end, boardSize has a value of 5"""
       self.board = [[Tile() for i in range(0, boardSize)] for j in range(0, boardSize)]  # creates a 2
       # dimensional list for the board. it iterates the amount specified, then does it again
       self.boardSize = boardSize
       self.numbombs = numbombs
       self.options = boardSize * boardSize - numbombs #keeps a count for how many turns you get,
       # subtracts by bomb number so that game ends when out of non-bomb tiles
       i = 0
       while i < numbombs:
           x = random.randint(0, self.boardSize-1) #random x location for bomb
           y = random.randint(0, self.boardSize-1) #random y location for bomb, minus one necessary
           if self.board[x][y].bomb == False: #scans to see if a bomb is already present, if not
               self.addbomb(x, y) #add bomb
               i += 1
           else:
               i -= 1


   def __str__(self):
       """Creates a string reprensentation of the object. Essentially formats the board we will see in the console"""
       strOut = "H" #blank space
       divider = "\n***" #the lines in between the rows


       for i in range(0, self.boardSize):
           strOut += " | " + str(i)
           divider += "****"
       divider += "\n"
       strOut += divider


       for y in range(0, self.boardSize):
           strOut += str(y)
           for x in range(0, self.boardSize):
               """scans tiles to see if they have been chosen. If the have not been chosen keep hidden with
               the 'else' statement. should be updating the grid over every iteration until you reach the board size"""
               if self.board[x][y].bomb and self.board[x][y].chosen: #revealstile
                   strOut += " | " + str(self.board[x][y].value)
               elif self.board[x][y].chosen: #reveals tile
                   strOut += " | " + str(self.board[x][y].value)
               else:
                   strOut += " |  "
           strOut += " | " #should execute once the iterations are over
           strOut += divider
       return strOut


   def addbomb(self, x, y):
       """takes the random x and y that was generated from the string function and turns the tile into a bomb"""
       self.board[x][y].value = -1 #assigns the tile to -1, so unleashing a bomb is "-1"
       self.board[x][y].bomb = True #'activates' bomb on tile
       for i in range(x-1, x+2):
           if 0 <= i < self.boardSize: #This if conditional should take care of the corners of the
               try:# adjacent tiles where the bomb is
                   if self.board[i][y-1].bomb == False:
                       self.board[i][y-1].value += 1
                       """Simpler terms: if there is not a bomb on the coordinate
                        of [i][y-1] then the tile of list{i}, item in list y-1 recieves a value of +1 after visualization
                        it seems that this takes care of everything to the left of the bomb postion"""
                   if  self.board[i][y+1].bomb ==False:
                       self.board[i][y+1].value += 1
                       """Simpler terms: if there is not a bomb on the coordinate
                                            of [i][y+1] then the tile of list{i}, item in list y+1 recieves a value of +1.
                                            This takes care of everything to the right of the bomb"""
               except IndexError:
                   main()
       try:
           if self.board[x-1][y].bomb == False:
               self.board[x-1][y].value += 1
               """This should be anything above the bomb """
           if self.board[x+1][y].bomb == False:
               self.board[x+1][y].value += 1
               """Below the bomb"""
       except IndexError:
           main()


   #This function was created by Melvin Nava
   def userinp(self, x, y):
       try:
           self.board[x][y].chosen = True
       except IndexError:
           print("please enter a number within the range of the labels")
           main()#"""This should be main() not sure what to put in place though"""
       self.options -= 1
       if self.board[x][y].value == -1: #checks to see if chosen tile is a bomb (-1)
           return False
       else:
           return True
   """attempt to use BFS to obtain the 'ripple effect' of searching through the array """
  # def Breadthfirstsearch(self, queue = None):
       #current_index = queue.get()
      # self.board[x+1][y] = current_index[0], current_index [1]
      # element = matrix[self.board[x+1][y].bomb]
      # if element == 1 or 2:
      #     return self.board[x+1][y].bomb
      # for i in range (self.board[x+1][y].bomb -1,self.board[x+1][y] +2):
      #     for k in range(self.board[x+1][y].bomb -1,self.board[x+1][y] +2):
       #        if self.board[x+1][y]


#This function was created by Mahedre
#play game
def main():
   boardSize = int(5)
   numbombs = int(2)
   gameOver = False #declares the game does not end until this is true
   winner = False #declares winner as false for as long as the game is in session
   Board = gameboard(boardSize, numbombs)
   while gameOver == False:
       print(Board)
       try:
           x = int(input("x: "))
           y = int(input("y: "))
       except:
           print("invalid input, please enter a number")
           continue
       Board.userinp(x, y) #executes the make move function with user x and y
       gameOver = Board.hitbomb(x, y)
       if Board.gamewon() and gameOver == False:
           gameOver = True
           winner = True


   print(Board)
   if winner:
       print("Congratulations, You Win!")
   else:
       print("You hit a bomb, Game Over!")
       print(Board)
main()


#For further instructions, please see the readme provided
#class TestClass:
 #def test_one(self):  #For me only one test works at a time I couldnt get it to run the tests in the class
   #Board = gameboard(5, 2)
   #assert Board.userinp(a, 2) == True #if letter


 #def test_two(self):
 #  Board = gameboard(5, 2)
 #  assert Board.userinp(3, 2) == True #correct input


 #def test_three(self):
 #  Board = gameboard(5, 2)
 #  assert Board.userinp(12, 2) == True #if out of range