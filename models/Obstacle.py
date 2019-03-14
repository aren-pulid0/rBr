from GameModel import gameModel


############################## OBSTACLE
##############################
###########  INITIAL X and Y
OBSTACLE_INITIAL_X = 270
OBSTACLE_INITIAL_Y = 20
###########  MOVEMENT
OBSTACLE_MOV_X = 0
OBSTACLE_MOV_Y = 20
###########  DIMENSIONS
# x:10
# y:40
# color: blue
###

class Obstacle(gameModel):

    ObstacleNumber = None

    def __init__(self):
        """Initialices a new Obstacle and assigns Obstacle_i tag"""
        super().__init__()
        
        if ObstacleNumber == None:
            self.tag = 'Obstacle_1'
            ObstacleNumber = 1
        else:
            ObstacleNumber += 1
            self.tag = 'Obstacle_' + str(ObstacleNumber)
    
    def setObstaclePosition(self, x, y):
        self.x = x
        self.y = y
    
    def setObstacleDirection(self, xdirection=None, ydirection=1):
        self.xdirection = xdirection
        self.ydirection = ydirection
    
    def __str__(self):
        return '{}, X: {}, Y: {}, xDir: {}, yDir: {}'.format(self.tag, self.x, self.y, self.xdirection, self.ydirection)