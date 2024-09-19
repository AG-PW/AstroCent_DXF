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

def hexagon(cx0,cy0,distance,index,color):
    plt.text((cx0), (cy0), f'{index}', ha='center', va='center', color=color)
    outers_xy = set()
    for i in range(6):
        cx = Decimal(cx0) + Decimal(math.cos(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
        cy = Decimal(cy0) + Decimal(math.sin(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
        outers_xy.add((Decimal(cx), Decimal(cy)))
        plt.text((cx), (cy), f'{index}:{i}', ha='center', va='center', color=color)
    return outers_xy
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'pink']


cx0,cy0 = 0,0
centers_set = hexagon(cx0, cy0, distance, 0, 'black')


centers_list = list(centers_set)
old_centers_set = centers_set
old_centers_list = list(old_centers_set)


test = set()
for i in range(len(old_centers_list)):
    print('-')
    print(len(old_centers_list))
    cx0,cy0 = old_centers_list[i]
    print(f'cx{cx0} : cy{cy0}')
    print(len(centers_set))
    print(len(old_centers_set))
    test.update(hexagon(cx0, cy0, distance, 0, colors[i]))



y = test - centers_set
test = set()
for i in range(len(list(y))):
    cx0, cy0 = list(y)[i]
    test.update(hexagon(cx0, cy0, distance, 0, 'black'))

y = test - centers_set
test = set()
for i in range(len(list(y))):
    cx0, cy0 = list(y)[i]
    test.update(hexagon(cx0, cy0, distance, 0, 'red'))

y = test - centers_set
test = set()
for i in range(len(list(y))):
    cx0, cy0 = list(y)[i]
    test.update(hexagon(cx0, cy0, distance, 0, 'red'))

plt.show()
#doc.saveas('circle.dxf')