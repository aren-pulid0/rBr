import time
from threading import Thread
from tkinter import Tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Frame

############################################################
############################## GAME
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
############################## SHURIKEN
##############################	
########### INITIAL X and Y
SHURIKEN_INITIAL_X = 270
SHURIKEN_INITIAL_Y = 710
########### MOVEMENT
SHURIKEN_MOV_Y = 5
SHURIKEN_MOV_X = 20
########### DIMENSIONS
			# radio: 10
			# color: red
###
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
############################## EVENTS
############################## 
########### SHURIKEN
SHURIKEN_EVENT = None
############################################################


class Shuriken():
	""" Shuriken is the main object of the game """

	def __init__(self):
		self.x = SHURIKEN_INITIAL_X
		self.y = SHURIKEN_INITIAL_Y
		self.xdirection = 0
		self.ydirection = 0
		self.movement = 'UPWARDS'

	def move(self,x,y):
		"""Recieves the amount of pixels to move in absolute value"""
		self.x += (x * self.xdirection)
		self.y += (y * self.ydirection)
	
	def __str__(self):
		return 'SHURIKEN : X: {}, Y: {}, DIRECTION X: {}, DIRECTION Y {}, MOVEMENT {}'.format(self.x, self.y, self.xdirection, self.ydirection, self.movement)

class Obstacle():
	""" If shuriken collides with one of this you lose """

	def __init__(self):
		self.x = OBSTACLE_INITIAL_X
		self.y = OBSTACLE_INITIAL_Y
		self.xdirection = 0
		self.ydirection = 1
		self.movement = None

	def move(self,y):
		"""Recieves the amount of pixels to move in absolute value"""
		self.y += (y * self.ydirection)
	
	def __str__(self):
		return 'OBSTACLE nº1: X: {}, Y: {}, DireccionY: {}, Movement: {}'.format(self.x,self.y,self.ydirection, self.movement)

class Drawer():

	def __init__(self,canvas):
		"""Holds the canvas to make the drawings in the game loop"""
		self.gameMap = canvas
		self.image = PhotoImage(file='/home/pulid0/100CodingChallenge/RunBladeRun/shuriken.gif')
	
	def move(self,drawing, tag, x, y):
		""" Draws the corresponding move then updates the canvas. Recieves a tag to recognice the object to move """
		self.gameMap.move(tag, (x * drawing.xdirection), (y * drawing.ydirection))
		self.gameMap.update()

	def drawWalls(self):
		self.gameMap.create_rectangle(BORDER_LEFT, BORDER_BOTTOM, WALL_LEFT, WALL_TOP, fill="black", tag="leftWall")
		self.gameMap.create_rectangle(WALL_RIGHT, WALL_BOTTOM, BORDER_RIGHT, BORDER_TOP, fill="black", tag='rightWall')
		self.gameMap.update()
	
	def drawShuriken(self):
		self.gameMap.create_image(SHURIKEN_INITIAL_X,SHURIKEN_INITIAL_Y, image=self.image, tag='shuriken')
		self.gameMap.update()
	
	def drawObstacle(self):
		self.gameMap.create_rectangle(OBSTACLE_INITIAL_X-5, OBSTACLE_INITIAL_Y-20, OBSTACLE_INITIAL_X+5, OBSTACLE_INITIAL_Y+20, fill="blue", tag="obstacle")

class EventListener(Thread):

	def __init__(self):
		Thread.__init__(self)
		self.event = None

	def run(self):
		global SHURIKEN_EVENT
		while True:
			if self.event == 'left':
				SHURIKEN_EVENT = 'move_left'

			if self.event == 'right':
				SHURIKEN_EVENT = 'move_right'

			time.sleep(100/1000)
		
			
def eventHandler(eventListener,event):
	print('Event recieved is {}'.format(event))
	if event == 'left':
		eventListener.event = 'left'

		### DEBUG
		#print('Event on EventListener is {}'.format(eventListener.event))
		#print('GLOBAL VARIABLE SHURIKEN EVENT: {}'.format(SHURIKEN_EVENT))
		### DEBUG
	if event == 'right':
		eventListener.event = 'right'

def setupGame(game_map):
	# Init objects required for the game
	shuriken = Shuriken()
	obstacle = Obstacle()
	drawer = Drawer(game_map)

	drawer.drawWalls()
	drawer.drawShuriken()
	drawer.drawObstacle()

	game_loop = Thread(target=GAME_LOOP, args=(shuriken, obstacle, drawer), name='GameLoopThread')
	game_loop.start()

def GAME_LOOP(shuriken, obstacle, drawer, pause=False ):
	# This is the main game loop:
	# 1-Checks for events
	# 2-Moves corresponding objects -> Also checks collisions
	# 3-Draws them.
	
	while not pause:

		#SHURIKEN
		if SHURIKEN_EVENT == 'move_left' and (shuriken.x - SHURIKEN_MOV_X + 10) != WALL_LEFT:
			if shuriken.movement == 'DOWNWARDS':
				moveShuriken_left(shuriken, xdirection=-1, ydirection=1)
				drawer.move(shuriken,'shuriken',SHURIKEN_MOV_X, SHURIKEN_MOV_Y)

			if shuriken.movement == 'UPWARDS':
				moveShuriken_left(shuriken)
				drawer.move(shuriken,'shuriken',SHURIKEN_MOV_X, SHURIKEN_MOV_Y)

			# check collision
			if (checkCollision(shuriken,obstacle)):
				print("COLISION")
				break

			### DEBUG
			#print(shuriken)
			### DEBUG

		if SHURIKEN_EVENT == 'move_right' and (shuriken.x + SHURIKEN_MOV_X - 10) != WALL_RIGHT:
			if shuriken.movement == 'DOWNWARDS':
				moveShuriken_right(shuriken, xdirection=1, ydirection=1)
				drawer.move(shuriken,'shuriken',SHURIKEN_MOV_X, SHURIKEN_MOV_Y)
			
			if shuriken.movement == 'UPWARDS':
				moveShuriken_right(shuriken)
				drawer.move(shuriken,'shuriken',SHURIKEN_MOV_X, SHURIKEN_MOV_Y)

			if (checkCollision(shuriken,obstacle)):
				print("COLISION")
				break


			### DEBUG
			#print(shuriken)
			### DEBUG
		
		#OBSTACLES

		moveObstacle(obstacle)
		drawer.move(obstacle,'obstacle',OBSTACLE_MOV_X, OBSTACLE_MOV_Y)

		###DEBUG
		print(obstacle)
		###DEBUG

		time.sleep(50/1000)

def checkCollision(shuriken, obstacle):
	colisionX = False
	colisionY = False

	for x in range(-5,5):
	# Checking square area of obstacle

		if (shuriken.x + 5 == obstacle.x + x) or (shuriken.x - 5 == obstacle.x + x):
			colisionX = True
		
			###DEBUG
			#print ("Colision X Value")
			###DEBUG
	
		for y in range(-20,20):

			if (shuriken.y + 5 == obstacle.y + y) or (shuriken.y + -5 == obstacle.y + y):
				colisionY = True

				###DEBUG
				#print ("Colision Y Value")
				###DEBUG
	
	if colisionX == True and colisionY == True:
		return True

def moveShuriken_left(shuriken, xdirection=-1, ydirection=-1):
	shuriken.xdirection = xdirection
	shuriken.ydirection = ydirection

	if shuriken.y == WALL_TOP:
		shuriken.movement = 'DOWNWARDS'
	
	if shuriken.y == WALL_BOTTOM:
		shuriken.movement = 'UPWARDS'

	shuriken.move(SHURIKEN_MOV_X, SHURIKEN_MOV_Y)


def moveShuriken_right(shuriken, xdirection=1, ydirection=-1):
	shuriken.xdirection = xdirection
	shuriken.ydirection = ydirection

	if shuriken.y == WALL_TOP:
		shuriken.movement = 'DOWNWARDS'
	
	if shuriken.y == WALL_BOTTOM:
		shuriken.movement = 'UPWARDS'
		
	shuriken.move(SHURIKEN_MOV_X, SHURIKEN_MOV_Y)
	
def moveObstacle(obstacle):

	if obstacle.y ==  WALL_TOP:
		obstacle.movement = 'DOWNWARDS'
		obstacle.ydirection = 1

	if obstacle.y + 20 == WALL_BOTTOM:
		obstacle.movement = 'UPWARDS'
		obstacle.ydirection = -1

	obstacle.move(OBSTACLE_MOV_Y)
	


class RunBladeRun(Frame):

	def __init__(self, master=None):

		Frame.__init__(self, master)
		self.pack()

		self.shuriken = Shuriken()
		self.obstacle = Obstacle()

		self.canvas = Canvas(self, width=WIDTH, height=HEIGHT,  background="white")
		self.eventListener = EventListener()
		self.eventListener.start()
		self.bind("<Left>", lambda e: eventHandler(self.eventListener,'left'))
		self.bind("<Right>", lambda e: eventHandler(self.eventListener,'right'))
		
		self.canvas.pack()
		self.focus()

		setupGame(self.canvas)

if __name__ == '__main__':
	app = RunBladeRun()
	app.mainloop()
