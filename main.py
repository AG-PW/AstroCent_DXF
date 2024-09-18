import ezdxf
import math

# Create doc object
doc = ezdxf.new('R2010')

# Create model space
msp = doc.modelspace()

# Parameter of the overall shape
diameter_overall = 50
msp.add_circle((0,0), diameter_overall/2)

# Parameter of the pattern
diameter_pattern = 1
distance = 2

circles = []



for j in range(0,6):

    cx = (math.cos(math.pi/3*j)*distance)
    cy = (math.sin(math.pi/3*j)*distance)
    circles.append({'center': (cx, cy), 'radius': diameter_pattern / 2})

    for i in range(0,6):
        cX = cx + (math.cos(math.pi/3*i)*distance)
        cY = cy + (math.sin(math.pi/3*i)*distance)
        circles.append({'center': (cX,cY), 'radius': diameter_pattern/2})


for circle in circles:
    msp.add_circle(circle['center'], circle['radius'])
doc.saveas('circle.dxf')