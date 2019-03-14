from tkinter import Canvas
from tkinter import PhotoImage


class GameMap(Canvas):
    ##############################DEFAULT
    WIDTH = 540
    HEIGHT = 720
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

    def __init__(self, master, width, height):
        super().__init__(master = master, width= width, height= height, background= 'white')
        self.ShurikenImage = PhotoImage(file='/home/pulid0/100CodingChallenge/RunBladeRun/shuriken.gif')
        self.simpleObstacleImage = PhotoImage(file='/home/pulid0/100CodingChallenge/RunBladeRun/obstacle.gif')

    def addGameModel(self, gameModel):

        if gameModel.tag == 'shuriken':
            self.create_image(0,0, image= self.ShurikenImage, tag=gameModel.tag)
            self.update()
        
        if gameModel.tag[:-1] == 'Obstacle_':
            self.create_image(0,0, image= self.simpleObstacleImage, tag= gameModel.tag)
            self.update()

    def moveGameModel(self, gameModel,x , y):

        self.move(gameModel.tag, x, y)
        self.update()
    
    def drawWalls(self):
        self.create_rectangle(GameMap.BORDER_LEFT, GameMap.BORDER_BOTTOM, GameMap.WALL_LEFT, GameMap.WALL_TOP, fill="black", tag="leftWall")
        self.create_rectangle(GameMap.WALL_RIGHT, GameMap.WALL_BOTTOM, GameMap.BORDER_RIGHT, GameMap.BORDER_TOP, fill="black", tag='rightWall')
        self.update()
    
    def drawWireFrame(self):
        for y in range(0, GameMap.WALL_BOTTOM, 5):
            self.create_line(GameMap.WALL_LEFT, GameMap.BORDER_TOP+y, GameMap.WALL_RIGHT, GameMap.BORDER_TOP+y , fill='green')

        for x in range(0, GameMap.WALL_RIGHT-60, 5):
            self.create_line(GameMap.WALL_LEFT + x, GameMap.BORDER_TOP, GameMap.WALL_LEFT + x, GameMap.BORDER_BOTTOM, fill='green')

        self.update()
