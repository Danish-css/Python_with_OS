import math
def triangle(base,height):
	return base*height/2

def rectangle(length,breadth):
	return length*breadth

def circle(radius):
	return math.pi*(radius**2)
def donut(outer_radius, inner_radius):
	return circle(outer_radius) - circle(inner_radius)
