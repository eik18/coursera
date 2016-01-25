"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
        Function that merges a single row or column in 2048.
    """ 
    temp_line=[] #declaration of new copy of line
    temp_line.extend(line) #transfer contents of line without impacting original
    table_width=len(line)
    index=0
    for dummy_variable in enumerate(range(table_width-1)):
        if temp_line[index]==0:
            #Current index is empty, slide past it 
            temp_line.pop(index)
            temp_line.append(0)
        elif temp_line[index+1]==0:
            #index to the right is empty, slide past it
            temp_line.pop(index+1)
            temp_line.append(0)
        elif temp_line[index+1]==temp_line[index]:
            #index to the right matches current index, merge!
            new_sum=temp_line[index]+temp_line[index+1]
            temp_line[index]=new_sum
            temp_line.pop(index+1)
            temp_line.append(0)
            index=index+1
        else:
            #index to the right doesn't match, move on
            index=index+1

    return temp_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height=grid_height
        self.grid_width=grid_width
        self.reset()
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.board=[]
        self.board=[[0 for dummy_col in range(self.grid_width)]for dummy_row in range(self.grid_height)]
            

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        tempresult=''
        for row in range(self.grid_height):
            tempresult=tempresult+str(self.board[row])+'\n'
        return tempresult
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
  
        index=[]
        motion=[]
        if direction==1:
            index=[self.grid_height-1,0]
            motion=OFFSETS['UP']
            iter_motion=OFFSETS['RIGHT']
            cellrange=self.grid_width
            iterrange=self.grid_height
        elif direction==2:
            index=[0,0]
            motion=OFFSETS['DOWN']
            cellrange=self.grid_width
            iterrange=self.grid_height
            iter_motion=OFFSETS['RIGHT']
                       
        elif direction==3:
            index=[0,self.grid_width-1]
            motion=OFFSETS['LEFT']
            cellrange=self.grid_height
            iterrange=self.grid_width
            iter_motion=OFFSETS['DOWN']
        elif direction==4:
            index=[0,0]
            motion=OFFSETS['RIGHT']
            cellrange=self.grid_height
            iterrange=self.grid_width
            iter_motion=OFFSETS['DOWN']
        
        for iteration in range(iterrange):
            output_result=[]
            for step in range(cellrange):
                row=index[0]+step*motion[0]+iter_motion*iteration
                col=index[1]+step*motion[1]+iter_motion*iteration
                output_result.append(self.get_tile(row, col))
            
    def get_line(self):        
                

        
            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        tile_list=self.empty_tile_avail()
        if tile_list:
            value_list=[4,2,2,2,2,2,2,2,2,2]
            new_value=random.choice(value_list)
            coordinates=random.choice(tile_list)
            self.set_tile(coordinates[0], coordinates[1], new_value)
        else:
            pass
        
    def empty_tile_avail(self):
        emptytiles=[]
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                    if self.board[row][col]==0:
                        emptytiles.append([row,col])
        return emptytiles
        
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.board[row][col]=value
        return 0

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.board[row][col]
    
