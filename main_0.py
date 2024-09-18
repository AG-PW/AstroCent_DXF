import ezdxf
import math
from decimal import Decimal, ROUND_DOWN

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

cxy = {(0,0)}

for j in range(6):

    cx = Decimal(math.cos(math.pi/3*j)*j*distance).quantize(Decimal('.00001'))
    cy = Decimal(math.sin(math.pi/3*j)*j*distance).quantize(Decimal('.00001'))
    cxy.add((cx, cy))
    for i in range(6):
        cX = cx + Decimal(math.cos(math.pi/3*i)*distance).quantize(Decimal('.00001'))
        cY = cy + Decimal(math.sin(math.pi/3*i)*distance).quantize(Decimal('.00001'))
        cxy.add((cX, cY))

cxy = list(cxy)
circles = []

for i in range(len(cxy)):
    cx, cy = cxy[i]
    circles.append({'center': (cx, cy), 'radius': diameter_pattern / 2})

for circle in circles:
    msp.add_circle(circle['center'], circle['radius'])



doc.saveas('circle.dxf')