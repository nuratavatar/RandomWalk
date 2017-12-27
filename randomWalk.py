from graphics import *
import math
from random import *

def isBet(lower, var, upper):
	if(lower > upper): #This is a stupid proofing for myself because I'm stupid
		holder = upper
		upper = lower
		lower = holder
	if(var < upper and var > lower):
		return True
	else:
		return False

#window, starting point, angle, length
def drawLine(w, p0, theta, L, color):
	x1 = p0.getX() + L * math.cos(math.pi/180 * theta)
	y1 = p0.getY() + L * math.sin(math.pi/180 * theta)
	p1 = Point(x1, y1)
	line = Line(p0, p1); line.setOutline(color);line.draw(w)
	return p1
def main():
	colors = ['red', 'blue', 'green', 'purple', 'magenta', 'black']
	win = GraphWin('', 600, 600)
	win.setCoords(-400, -400, 400, 400)
	p = Point(0, 0)
	offCount = 0
	oC = Text(Point(0, -380), "Iterations off Screen: " + str(offCount));oC.draw(win)
	distance = 0
	d = Text(Point(0, 380), "Distance from Start: " + str(distance));d.draw(win)
	while(1):
		p = drawLine(win, p, randint(0, 360), 5, colors[randint(0, 5)]) #randint(0,5)
		if((not isBet(-400, p.getX(), 400)) or (not isBet(-400, p.getY(), 400))):
			oC.undraw()
			offCount += 1
			oC = Text(Point(0, -380), offCount); oC.setSize(10)
			oC.draw(win)
		distance = math.sqrt((p.getX())**2 + (p.getY())**2)
		d.undraw()
		d = Text(Point(0, 380), "Distance from Start: " + str(int(distance)));d.draw(win)

	win.getMouse()
main()
