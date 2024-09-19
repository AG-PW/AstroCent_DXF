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
outers_xy = {(0,0)}

def hexagon(cx0,cy0,distance,index,color):
    plt.text((cx0), (cy0), f'{index}', ha='center', va='center', color=color)
    print(f'Hex: {index} at x:{cx0} | cy:{cy0} creates:')
    for i in range(6):
        cx = Decimal(cx0) + Decimal(math.cos(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
        cy = Decimal(cy0) + Decimal(math.sin(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
        centers_xy.add((Decimal(cx), Decimal(cy)))
        outers_xy.add((Decimal(cx), Decimal(cy)))
        plt.text((cx), (cy), f'{index}:{i}', ha='center', va='center', color=color)
        print(f'SubHex: {i} at x:{cx} | cy:{cy} creates:')
    print('New hex incoming...')
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'pink']
hexagon(0,0,distance,0,'black')
outers_xy.remove((0,0))

prev_outers_xy = outers_xy
print(prev_outers_xy)
for j in range(len(list(prev_outers_xy))):
     cx0, cy0 = list(prev_outers_xy)[j]
     print(f'cx0:{cx0} | cy0:{cy0}')
     for i in range(6):
         cx = Decimal(cx0) + Decimal(math.cos(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
         cy = Decimal(cy0) + Decimal(math.sin(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
         plt.text((cx), (cy), f'{j}:{i}', ha='center', va='center', color='red')








plt.show()
doc.saveas('circle.dxf')