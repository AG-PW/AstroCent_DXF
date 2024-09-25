import ezdxf
import math
from decimal import Decimal, ROUND_DOWN
import matplotlib.pyplot as plt


# Plot to see what's happening
size = 30
fig,ax = plt.subplots(figsize=(size, size))
plt.title('Circle Pattern')
plt.xlim(-size, size)
plt.ylim(-size, size)
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))

# Add minor ticks
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.5))

# Customize grid appearance
ax.grid(which='major', linestyle='-', linewidth='0.5', color='k')
ax.grid(which='minor', linestyle='--', linewidth='0.25', color='k')

# Create doc object
doc = ezdxf.new('R2010',units=ezdxf.units.MM)

# Create model space
msp = doc.modelspace()
# Add a new layer
layer_pattern = "Pattern"
doc.layers.add(layer_pattern)
layer_shape = "Shape"
doc.layers.add(layer_shape)
layer_hole = "Hole"
doc.layers.add(layer_hole)

# Parameter of the overall shape
square_side = 50
active_area = 35

# Parameter of the pattern
diameter_pattern = 2
distance = 4

# Hole parameters
hole = 3.5
offset = 3.5

circles = []
def hexagon(cx0,cy0,distance):
    #plt.text((cx0), (cy0), f'O', ha='center', va='center', color='red')
    outers_xy = set()
    for i in range(6):
        cx = Decimal(cx0) + Decimal(math.cos(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
        cy = Decimal(cy0) + Decimal(math.sin(math.pi / 3 * i) * distance).quantize(Decimal('.00001'))
        outers_xy.add((Decimal(cx), Decimal(cy)))
    return outers_xy


def outside(side, area, hole, offset):
    corner = side/2
    plt.gca().add_artist(plt.Line2D([-corner,-corner],[corner,-corner],linestyle='-',color='green'))
    plt.gca().add_artist(plt.Line2D([corner, -corner], [corner, corner], linestyle='-', color='green'))
    plt.gca().add_artist(plt.Line2D([corner, corner], [-corner, corner], linestyle='-', color='green'))
    plt.gca().add_artist(plt.Line2D([-corner, corner], [-corner, -corner], linestyle='-', color='green'))
    points = [(-corner, -corner), (corner, -corner), (corner, corner),(-corner,corner),(-corner,-corner)]
    msp.add_lwpolyline(points, dxfattribs={"layer": layer_shape})


    plt.gca().add_artist(plt.Circle((-corner+offset, -corner+offset), radius=hole / 2, fill=False, linewidth=1, edgecolor='magenta'))
    plt.gca().add_artist(plt.Circle((corner-offset, -corner+offset), radius=hole / 2, fill=False, linewidth=1, edgecolor='magenta'))
    plt.gca().add_artist(plt.Circle((corner - offset, corner - offset), radius=hole / 2, fill=False, linewidth=1, edgecolor='magenta'))
    plt.gca().add_artist(plt.Circle((-corner + offset, corner - offset), radius=hole / 2, fill=False, linewidth=1, edgecolor='magenta'))
    msp.add_circle((-corner+offset, -corner+offset), hole / 2, dxfattribs={"layer": layer_hole})
    msp.add_circle((corner-offset, -corner+offset), hole / 2, dxfattribs={"layer": layer_hole})
    msp.add_circle((corner - offset, corner - offset), hole / 2, dxfattribs={"layer": layer_hole})
    msp.add_circle((-corner + offset, corner - offset), hole / 2, dxfattribs={"layer": layer_hole})


    corner = active_area / 2
    plt.gca().add_artist(plt.Line2D([-corner, -corner], [corner, -corner], linestyle='-', color='cyan'))
    plt.gca().add_artist(plt.Line2D([corner, -corner], [corner, corner], linestyle='-', color='cyan'))
    plt.gca().add_artist(plt.Line2D([corner, corner], [-corner, corner], linestyle='-', color='cyan'))
    plt.gca().add_artist(plt.Line2D([-corner, corner], [-corner, -corner], linestyle='-', color='cyan'))

all_centers = set()
centers = set()
centers.update(hexagon(0, 0, distance))
all_centers.update(centers)
new_centers = set()
iteration_centers = centers


for j in range(5):

    for center in iteration_centers:
        cx0,cy0 = list(center)
        new_centers.update(hexagon(cx0, cy0, distance))
        all_centers.update(new_centers)
    iteration_centers = new_centers - centers


print(len(all_centers))
for center in range(len(all_centers)):
    cx0,cy0 = list(all_centers)[center]
    print(f'cx:{cx0} | cy:{cy0}')
    #plt.text((cx0), (cy0), 'O', ha='center', va='center', color='red')
    print(type(cx0))
    if( (cx0+Decimal(diameter_pattern/2)>active_area/2) or (cx0-Decimal(diameter_pattern/2)<-active_area/2) or (cy0+Decimal(diameter_pattern/2)>active_area/2) or (cy0-Decimal(diameter_pattern/2)<-active_area/2)):
        continue
    else:
        plt.gca().add_artist(plt.Circle((cx0,cy0), radius=diameter_pattern/2, fill=False, linewidth=1, edgecolor='red'))
        msp.add_circle((cx0, cy0), diameter_pattern / 2,dxfattribs={"layer": layer_pattern})




outside(square_side, active_area, hole,offset)
plt.show()
doc.saveas('Astrocent_Square.dxf')