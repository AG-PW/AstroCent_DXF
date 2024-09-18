import ezdxf
import math
from decimal import Decimal, ROUND_DOWN
import matplotlib.pyplot as plt


# Plot to see what's happening
plt.figure(figsize=(10, 10))
plt.title('Circle Pattern')
plt.xlim(-10, 10)
plt.ylim(-10, 10)

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

centers_xy = {(0,0)}
points_xy = {(0,0)}

center_x0, center_y0 = list(centers_xy)[0]

for i in range(6):
    px = Decimal(center_x0) + Decimal(math.cos(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
    py = Decimal(center_y0) + Decimal(math.sin(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
    centers_xy.add( ( Decimal(px), Decimal(py) ) )
    points_xy.add( ( Decimal(px), Decimal(py) ) )
    circle = plt.Circle((px/2, py/2), (diameter_pattern / 2)/2, fill=False, color='red', linewidth=1)
    # Add text inside the circle
    plt.text( (px/2), (py/2), str(i), ha='center', va='center')

print(len(centers_xy))

for i in range(len(centers_xy)):
    center_x0, center_y0 = list(centers_xy)[i]
    for j in range(6):
        px = Decimal(center_x0) + Decimal(math.cos(math.pi / 3 * j) * distance).quantize(Decimal('.00001'))
        py = Decimal(center_y0) + Decimal(math.sin(math.pi / 3 * j) * distance).quantize(Decimal('.00001'))
        centers_xy.add((Decimal(px), Decimal(py)))
        points_xy.add((Decimal(px), Decimal(py)))
        

print(len(centers_xy))

points_xy = list(points_xy)
circles = []

# for i in range(len(points_xy)):
#     px, py = points_xy[i]
#     circles.append({'center': (px, py), 'radius': diameter_pattern / 2})
#     circle = plt.Circle( (px/2, py/2), (diameter_pattern / 2)/2, fill=False, color='red', linewidth=1)
#     plt.gca().add_artist(circle)
#
# for circle in circles:
#     msp.add_circle(circle['center'], circle['radius'])



plt.show()
doc.saveas('circle.dxf')