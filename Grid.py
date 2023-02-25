from typing import List, Tuple
from copy import deepcopy

class Grid:

    """A Python class that represent the grid of a 2048 game

    Attributes:

        matrix(list) : A list of integer representing the grid
        size(int) : The size of the grid
    Methods:
        __init__(self, size: int) : Initializes the grid
        Optimizer_score(self) : Returns the grid's score

        Maximizer moves :
            -notBlockedUp/notBlockedDown/NotBlockedLeft/NotBlockedRight(self) :
                Returns whether the grid can move up/down/left/right
            -moveUp/moveDown/moveLeft/moveRight :
                Returns : The grid after being moved in the chosen direction

        Minimizer's moves :
            -addRandom(self) : Find a random place that is empty and adds a 2 or a 4

    Comment : Please refer to the code with left/up/right/down = 0, 1, 2, 3

    """
    def __init__(self, board):
        self.size = len(board)
        self.matrix = board

    def Intro(self):
        for i in range(self.size):
            print(self.matrix[i])

    def getEmptyCells(self):
        """
        This method counts the number of the empty cells on the grid
        Returns:
            An int counting the number of empty cells on the grid
        """

        EmptyCells = 0

        for row in range(self.size):
            for col in range(self.size):
                if self.matrix[row][col] == 0:
                    EmptyCells += 1
        
        return EmptyCells
    
    def getUniformity(self):
        """
        This method returns the uniformity of the grid
        Returns:
            An int representing the uniformity of the grid
        """
        uniformity = 0
        for row in range(self.size):
            for col in range(self.size):
                if row + 1 <= self.size:
                    uniformity += (self.matrix[row][col] == self.matrix[row + 1][col])
                if col + 1 <= self.size:
                    uniformity += (self.matrix[row][col] == self.matrix[row][col + 1])
        
        return uniformity

    def Optimizer_score(self):
        score = 0
        for i in range(self.size):
            for j in range(self.size):
                score += self.matrix[i][j]

        return score
    def getMaxTile(self):
        """
        This method returns the maximum tile value on the grid
        """
        max_tile = 0
        for i in range(self.size):
            for j in range(self.size):
                max_tile = max(max_tile, self.matrix[i][j])
        return max_tile
    def notBlockedUp(self):
        # Loop through the column, and track if that column could be moved up or not
        # Method for moving one column up : 
        # There is an empty cell above a valued cell/There are two cells could be merged together

        #Search for the first value in the column
        for col in range(self.size):

            FirstNonEmptyRow = -1

            for row in range(self.size - 1 , -1 , -1):
                if self.matrix[row][col] != 0:
                    FirstNonEmptyRow = row
                    break
            if FirstNonEmptyRow == -1:
                continue
            else:
                for row in range(FirstNonEmptyRow , -1 , -1):
                    if self.matrix[row][col] == 0:
                        return True
                    elif row != 0 and self.matrix[row][col] == self.matrix[row - 1][col]:
                        return True

        return False

    def notBlockedDown(self):
        """

        This method checks if the grid could be moved down
        The technique is searching for the bottom-most non-empty cell, and then check if this specific cell could be moved down
        
        Returns : 1 if the grid could be moved down, 0 otherwise
        
        """
        for col in range(self.size):
            
            FirstNonEmptyRow = -1

            for row in range(self.size):
                if self.matrix[row][col] != 0:
                    FirstNonEmptyRow = row
                    break
            if FirstNonEmptyRow == -1:
                continue
            else:
                for row in range(FirstNonEmptyRow , self.size):
                    if self.matrix[row][col] == 0:
                        return True
                    elif row != self.size - 1 and self.matrix[row][col] == self.matrix[row + 1][col]:
                        return True

        return False

    def notBlockedLeft(self):

        # Loop through the row and search for the first left-most value

        for row in range(self.size):

            First_nonempty_col = -1 

            for col in range(self.size - 1, -1 , -1):
                if self.matrix[row][col] != 0:
                    First_nonempty_col = col
                    break
            if First_nonempty_col == -1:
                continue
            else:
                for col in range(First_nonempty_col , -1 , -1):
                    if self.matrix[row][col] == 0:
                        return True
                    elif col != 0 and self.matrix[row][col] == self.matrix[row][col - 1]:
                        return True

        return False  

    def notBlockedRight(self):

        """
        This method checks if the grid could be moved right
        The technique is searching for the left-most non-empty cell, and then check if the cell could be moved right
        
        Returns : 1 if the grid could be moved right, 0 otherwise

        """

        for row in range(self.size):

            FirstNonEmptyCol = -1 

            for col in range(self.size):
                if self.matrix[row][col] != 0:
                    FirstNonEmptyCol = col
                    break
            if FirstNonEmptyCol == -1:
                continue
            else:
                for col in range(FirstNonEmptyCol , self.size):
                    if self.matrix[row][col] == 0:
                        return True
                    elif col != self.size - 1 and self.matrix[row][col] == self.matrix[row][col + 1]:
                        return True

        return False

    def moveUp(self):
        """
        This method moves the grid up
        Returns:
            Another grid that is the result after moving the self grid up
        """

        Upgraded = deepcopy(self)

        for col in range(Upgraded.size):

            LastNonEmptyRow = -1
            FirstEmptyRow = -1
            matched = False 

            for row in range(Upgraded.size):

                current_value = Upgraded.matrix[row][col]

                # Update the first empty row in this column

                if current_value == 0 and FirstEmptyRow == -1:
                    FirstEmptyRow = row
                
                elif current_value != 0:
                    #move it up
                    if FirstEmptyRow == -1:
                        LastNonEmptyRow = row 
                    if FirstEmptyRow != -1:
                        Upgraded.matrix[FirstEmptyRow][col] = current_value
                        Upgraded.matrix[row][col] = 0
                        LastNonEmptyRow = FirstEmptyRow
                        FirstEmptyRow = FirstEmptyRow + 1

                    if LastNonEmptyRow != 0:
                        if matched == False and Upgraded.matrix[LastNonEmptyRow -1][col] == current_value:
                            Upgraded.matrix[LastNonEmptyRow - 1][col] = current_value * 2
                            Upgraded.matrix[LastNonEmptyRow][col] = 0
                            LastNonEmptyRow = LastNonEmptyRow - 1
                            FirstEmptyRow = LastNonEmptyRow + 1
                            matched = True
                        else:
                            matched = False

        return Upgraded
    
    def moveDown(self):
        """
        This method moves the grid down
        Returns:
            Another grid that is the result after moving the self grid down
        """

        Downgraded = deepcopy(self)

        for col in range(Downgraded.size):

            LastNonEmptyRow = -1
            FirstEmptyRow = -1
            matched = False 

            for row in range(Downgraded.size - 1, -1, -1):

                current_value = Downgraded.matrix[row][col]

                # Update the first empty row in this column

                if current_value == 0 and FirstEmptyRow == -1:
                    FirstEmptyRow = row
                
                elif current_value != 0:
                    #move it down
                    if FirstEmptyRow == -1:
                        LastNonEmptyRow = row 
                    if FirstEmptyRow != -1:
                        Downgraded.matrix[FirstEmptyRow][col] = current_value
                        Downgraded.matrix[row][col] = 0
                        LastNonEmptyRow = FirstEmptyRow
                        FirstEmptyRow = FirstEmptyRow - 1

                    if LastNonEmptyRow != Downgraded.size - 1:
                        if matched == False and Downgraded.matrix[LastNonEmptyRow + 1][col] == current_value:
                            Downgraded.matrix[LastNonEmptyRow + 1][col] = current_value * 2
                            Downgraded.matrix[LastNonEmptyRow][col] = 0
                            LastNonEmptyRow = LastNonEmptyRow + 1
                            FirstEmptyRow = LastNonEmptyRow - 1
                            matched = True
                        else:
                            matched = False

        return Downgraded
    def moveLeft(self):
        """
        This method moves the grid left
        Returns:
            Another grid that is the result after moving the self grid left
        """

        Leftgraded = deepcopy(self)

        for row in range(Leftgraded.size):

            LastNonEmptyCol = -1
            FirstEmptyCol = -1
            matched = False 

            for col in range(Leftgraded.size):
                
                current_value = Leftgraded.matrix[row][col]

                # Update the left-most empty column in this row

                if current_value == 0 and FirstEmptyCol == -1:
                    FirstEmptyCol = col
                
                elif current_value != 0:
                    #Determine if it can't be moved left
                    if FirstEmptyCol == -1:
                        LastNonEmptyCol = col 
                    #elif it can be moved left
                    if FirstEmptyCol != -1:
                        Leftgraded.matrix[row][FirstEmptyCol] = current_value
                        Leftgraded.matrix[row][col] = 0
                        LastNonEmptyCol = FirstEmptyCol
                        FirstEmptyCol = FirstEmptyCol + 1
                    
                    if LastNonEmptyCol != 0:
                        if matched == False and Leftgraded.matrix[row][LastNonEmptyCol - 1] == current_value:
                            Leftgraded.matrix[row][LastNonEmptyCol - 1] = current_value * 2
                            Leftgraded.matrix[row][LastNonEmptyCol] = 0
                            LastNonEmptyCol = LastNonEmptyCol - 1
                            FirstEmptyCol = LastNonEmptyCol + 1
                            matched = True
                        else:
                            matched = False
        
        return Leftgraded
    def moveRight(self):

        """
        This method moves the grid right
        Returns:
            Another grid that is the result after moving the self grid right
        """

        Rightgraded = deepcopy(self)

        for row in range(Rightgraded.size):

            LastNonEmptyCol = -1
            FirstEmptyCol = -1
            matched = False 

            for col in range(Rightgraded.size - 1, -1, -1):
                
                current_value = Rightgraded.matrix[row][col]

                # Update the left-most empty column in this row

                if current_value == 0 and FirstEmptyCol == -1:
                    FirstEmptyCol = col
                
                elif current_value != 0:
                    #Determine if it can't be moved right
                    if FirstEmptyCol == -1:
                        LastNonEmptyCol = col 
                    #elif it can be moved right
                    if FirstEmptyCol != -1:
                        Rightgraded.matrix[row][FirstEmptyCol] = current_value
                        Rightgraded.matrix[row][col] = 0
                        LastNonEmptyCol = FirstEmptyCol
                        FirstEmptyCol = FirstEmptyCol - 1
                    
                    if LastNonEmptyCol != Rightgraded.size - 1:
                        if matched == False and Rightgraded.matrix[row][LastNonEmptyCol + 1] == current_value:
                            Rightgraded.matrix[row][LastNonEmptyCol + 1] = current_value * 2
                            Rightgraded.matrix[row][LastNonEmptyCol] = 0
                            LastNonEmptyCol = LastNonEmptyCol + 1
                            FirstEmptyCol = LastNonEmptyCol - 1
                            matched = True
                        else:
                            matched = False
        
        return Rightgraded
    
        
    def getPossibleMaximizerMoves(self):
        """
        This method returns a list of all the possible moves that can be made on the grid
        Returns:
            A list of all the possible moves that can be made on the grid in the tuple (Move , Grid_after_moved)
        """

        Possible_grid = []

        if self.notBlockedLeft():
            Possible_grid.append([2, self.moveLeft()])
        if self.notBlockedUp():
            Possible_grid.append([0 , self.moveUp()])
        if self.notBlockedRight():
            Possible_grid.append([3 , self.moveRight()])
        if self.notBlockedDown():
            Possible_grid.append([1 , self.moveDown()])
        
        return Possible_grid
    
    def addRandomcell(self):
        """ 
        This method adds a random 2 or 4 cell on to the grid
        Returns : A list of grids after being added a random cell
        """

        Possible_grid = []

        for row in range(self.size):
            for col in range(self.size):
                if self.matrix[row][col] == 0:

                    Temp1 = deepcopy(self)
                    Temp2 = deepcopy(self)
                    Temp1.matrix[row][col] = 2
                    Possible_grid.append(Temp1)

                    Temp2.matrix[row][col] = 4
                    Possible_grid.append(Temp2)
        
        return Possible_grid
