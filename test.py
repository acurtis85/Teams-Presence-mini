from unicornhatmini import UnicornHATMini
import threading
from time import sleep
from random import randint
width = 7
height = 17
blinkThread = None
after_work = False
globalRed = 0
globalGreen = 0
globalBlue = 0
token=''
points = []
fullname = ''
brightness_led = 0.5
sleepValue = 5 # seconds
unicorn = UnicornHATMini()

def setColor(r, g, b, brightness, speed) :
	global crntColors, globalBlue, globalGreen, globalRed
	globalRed = r
	globalGreen = g
	globalBlue = b
	if brightness == '' :
		unicorn.set_brightness(brightness_led)
	for x in range(width):
		for y in range(height):
			unicorn.set_pixel(x, y, r, g, b)
			unicorn.show()
			
def setColor2(r, g, b) :
	for x in range(width):
		for y in range(height):
			unicorn.set_pixel(x, y, r, g, b)
			unicorn.show()

def pulse():
	for b in range(0, 7):
		blockPrint()
		unicorn.set_brightness(b/10)
		enablePrint()
		for y in range(height):
			for x in range(width):
				unicorn.set_pixel(x, y, 102, 255, 255)
				unicorn.show()
		sleep(0.05)
	sleep(1)
	for b in range(6, 0, -1):
		blockPrint()
		unicorn.set_brightness(b/10)
		enablePrint()
		for y in range(height):
			for x in range(width):
				unicorn.set_pixel(x, y, 102, 255, 255)
				unicorn.show()
		sleep(0.05)

def switchBlue() :
	red = 0
	green = 0
	blue = 250
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()

def switchRed() :
	red = 250
	green = 0
	blue = 0
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()

def switchGreen() :
	red = 0
	green = 250
	blue = 0
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()

def switchPink() :
	red = 255
	green = 108
	blue = 180
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()

def switchYellow() :
	red = 255
	green = 191
	blue = 0
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()

def switchOff() :
	global blinkThread, globalBlue, globalGreen, globalRed
	globalRed = 0
	globalGreen = 0
	globalBlue = 0
	if blinkThread != None :
		blinkThread.do_run = False
	unicorn.clear()
	unicorn.show()

class LightPoint:

	def __init__(self):
		self.direction = randint(1, 4)
		if self.direction == 1:
			self.x = randint(0, width - 1)
			self.y = 0
		elif self.direction == 2:
			self.x = 0
			self.y = randint(0, height - 1)
		elif self.direction == 3:
			self.x = randint(0, width - 1)
			self.y = height - 1
		else:
			self.x = width - 1
			self.y = randint(0, height - 1)

		self.colour = []
		for i in range(0, 3):
			self.colour.append(randint(100, 255))


def update_positions():

	for point in points:
		if point.direction == 1:
			point.y += 1
			if point.y > height - 1:
				points.remove(point)
		elif point.direction == 2:
			point.x += 1
			if point.x > width - 1:
				points.remove(point)
		elif point.direction == 3:
			point.y -= 1
			if point.y < 0:
				points.remove(point)
		else:
			point.x -= 1
			if point.x < 0:
				points.remove(point)


def plot_points():

	unicorn.clear()
	for point in points:
		unicorn.set_pixel(point.x, point.y, point.colour[0], point.colour[1], point.colour[2])
	unicorn.show()

def blinkRandom():
	#t = threading.currentThread()
	#while getattr(t, "do_run", True):
	if len(points) < 10 and randint(0, 5) > 1:
		points.append(LightPoint())
		plot_points()
		update_positions()
		sleep(0.03)

# Setup Unicorn light
	setColor(50, 50, 50, 1, 1)
#unicorn.set_layout(unicorn.AUTO)
	unicorn.set_brightness(0.8)

# Get the width and height of the hardware
	width, height = unicorn.get_shape()

		
blinkRandom()
