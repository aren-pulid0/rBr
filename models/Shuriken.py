from GameModel import gameModel

############################## SHURIKEN
##############################	
########### INITIAL X and Y
SHURIKEN_INITIAL_X = 270
SHURIKEN_INITIAL_Y = 710
########### MOVEMENT
SHURIKEN_MOV_Y = 10
SHURIKEN_MOV_X = 20
########### DIMENSIONS
# radio: 10
# color: red
###

class Shuriken(gameModel):

    radius = 10


    def __init__(self):
        super().__init__()
        self.tag = 'Shuriken'
        self.direction = None
    
    def setShurikenPosition(self, x, y):
        self.x = x
        self.y = y
    
    def setShurikenDirection(self, movement):
        MOVES = {
            'LEFT': moveLeft(),
            'RIGHT': moveRight(),
            'UP': moveUp(),
            'DOWN': moveDown()
            }

        if movement not in MOVES.keys():
            print("Movement is not [ LEFT, RIGHT, UP , DOWN ]")
            raise NotImplementedError
        else:
            MOVES[movement]

        def moveLeft(self):
            self.xdirection = -1
        
        def moveRight(self):
            self.xdirection = 1

        def moveUp(self):
            self.ydirection = -1
        
        def moveDown(self):
            self.ydirection = 1

    
