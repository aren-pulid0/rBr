from tkinter import Canvas
from tkinter import Tk
##############################
WIDTH = 540
HEIGHT = 720
##############################
########### BORDERS
###### X
BORDER_LEFT = 0
BORDER_RIGHT = 540
###### Y
BORDER_TOP = 0
BORDER_BOTTOM = 720
###### X
WALL_LEFT = 60
WALL_RIGHT = 480
###### Y
WALL_TOP = 0
WALL_BOTTOM = 720
###

class GameMap(Canvas):

    def __init__(self, master, width, height):
        super().__init__(master = master, width= width, height= height)


app = Tk()
gameMap = GameMap(app, WIDTH, HEIGHT)
gameMap.pack()

app.mainloop()