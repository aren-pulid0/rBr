class gameModel():

    def __init__(self):
        self.x = None
        self.y = None
        self.xdirection = None
        self.ydirection = None
    
    def move(self, x, y):

        self.x = self.x + (x * self.xdirection)
        self.y = self.y + (y * self.ydirection)
    
