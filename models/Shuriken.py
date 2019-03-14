from GameModel import gameModel

############################## SHURIKEN
##############################	
########### INITIAL X and Y
#SHURIKEN_INITIAL_X = 270
#SHURIKEN_INITIAL_Y = 710


class Shuriken(gameModel):

    radius = 10
    MOV_Y = 10
    MOV_X = 20

    def __init__(self):
        super().__init__()
        self.tag = 'Shuriken'
        self.direction = None # Direction is a debug/state attribute just to make things clearer instead of xdir and ydir
    
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

        # Here I change the direction
        def moveLeft(self):
            self.xdirection = -1

            if self.ydirection == 1:
                self.direction = 'DOWN-LEFT'
            else:
                self.direction = 'UP-LEFT'
        
        def moveRight(self):
            self.xdirection = 1

            if self.ydirection == 1:
                self.direction = 'DOWN-RIGHT'
            else:
                self.direction = 'UP-RIGHT'

        def moveUp(self):
            self.ydirection = -1

            if self.xdirection == -1:
                self.direction = 'UP-LEFT'
            else:
                self.direction = 'UP-RIGHT'
        
        def moveDown(self):
            self.ydirection = 1

            if self.xdirection == -1:
                self.direction = 'DOWN-LEFT'
            else:
                self.direction = 'DOWN-RIGHT'

    
    