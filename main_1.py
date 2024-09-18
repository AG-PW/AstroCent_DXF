import ezdxf
import math
from decimal import Decimal, ROUND_DOWN
import matplotlib.pyplot as plt

size = 20
# Plot to see what's happening
plt.figure(figsize=(size, size))
plt.title('Circle Pattern')
plt.xlim(-size, size)
plt.ylim(-size, size)

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


def hexagon(cx0,cy0,distance,index,color):
    plt.text((cx0), (cy0), f'{index}', ha='center', va='center', color=color)
    for i in range(6):
        cx = Decimal(cx0) + Decimal(math.cos(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
        cy = Decimal(cy0) + Decimal(math.sin(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
        centers_xy.add((Decimal(cx), Decimal(cy)))
        plt.text((cx), (cy), f'{index}:{i}', ha='center', va='center', color=color)
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'pink']
for i in range(6):
    cx0,cy0 = list(centers_xy)[i]
    hexagon(cx0,cy0,distance,i,colors[i])
#hexagon(0,0,distance,0,'black')



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