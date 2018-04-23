from py2opencl import Py2OpenCL
import numpy
from numpy.random import randint

def next_it( x, y, dest, src ):
    """
      neighbor coordinates:

       0, 1, 2,
       3,    4,
       5, 6, 7

    """
    live_neighbors = ( src[ x-1, y-1 ] + src[ x, y-1 ] + src[ x+1, y-1 ]
                       + src[ x-1, y ] + src [ x+1, y ]
                       + src[ x-1, y+1 ] + src[ x, y+1 ] + src[ x+1, y+1 ] )
    if live_neighbors < 2:
        dest[x,y] = 0
    elif live_neighbors == 3:
        dest[x,y] = 1
    elif src[x,y] and live_neighbors == 2:
        dest[x,y] = 1
    elif live_neighbors > 3:
        dest[x,y] = 0
    else:
        dest[x,y] = 0

grid = randint( 0, 2, size=(40, 40) ).astype(numpy.dtype('uint8'))

iterate = Py2OpenCL( next_it )
iterate.bind( grid, return_type = numpy.dtype('uint8') )

print iterate.kernel

for i in range(int(1e6)):
    grid = iterate.apply( grid )
