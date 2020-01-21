"""
Radial Gradient. 

Draws a series of concentric circles to create a gradient 
from one color to another.
"""

class expanding_circle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0
    
    def grow(self, velocity):
        self.r = self.r + velocity
    
    def render(self):
        ellipse(self.x, self.y, self.r, self.r)
        
class expanding_ring(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0
        self.thickness = 30
        self.color = random(0, 360) 
    
    def grow(self, velocity):
        self.r = self.r + velocity
        self.color = (self.color + 4) % 360
    
    def render(self):
        fill(self.color, 90, 90)
        ellipse(self.x, self.y, self.r, self.r)
        fill(0, 0, 0)        
        inner_r = self.r - self.thickness
        ellipse(self.x, self.y, inner_r, inner_r)
        


circle_list = []

def setup():
    size(1080, 720)
    background(0)
    colorMode(HSB, 360, 100, 100)
    noStroke()
    ellipseMode(RADIUS)
    frameRate(30)
    
    x = width/2
    y = height/2
    velocity = 4

def draw():
    background(0)
    
    if mousePressed:
        circle = expanding_ring(mouseX, mouseY)
        circle_list.append(circle)
        
    for circle in circle_list:
        circle.grow(4)
        circle.render()
        if circle.r > width:
            circle_list.remove(circle)
    print(len(circle_list))

    
def drawGradient(x, y):
    radius = width / 4
    h = random(0, 360)
    for r in range(radius, 0, -1):
        fill(h, 90, 90)
        ellipse(x, y, r, r)
        h = (h + 1) % 360


    
