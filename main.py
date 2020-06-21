from PIL import Image
import numpy

img = Image.open("tiny.png")
array = numpy.array(img).tolist()
for x, y in enumerate(array):
    for i, h in enumerate(y):
        if h == 0:
            array[x][i] = (0, 0, 0)
        else:
            array[x][i] = (255, 255, 255)
for i, h in enumerate(array):
    for x, y in enumerate(h):
        #line above, line below, pixel to the right, pixel to the left. If > 2, then turn green
        counter=0
        if array[i][x] == (255, 255, 255):
            if x+1 < len(array[i]):
                if array[i][x+1] != (0, 0, 0):
                    print("triggered 1")
                    counter +=1
            if x-1 != -1:
                if array[i][x-1] != (0, 0, 0):
                    print("triggered 2")
                    counter +=1
            if i+1 < len(array):
                if array[i+1][x] != (0, 0, 0):
                    print("triggered 3")
                    counter+=1
            if i-1 != -1:
                if array[i-1][x] != (0, 0, 0):
                    print("triggered 4")
                    counter+=1
            if counter == 1:
                array[i][x] = (0, 0, 255)
            elif counter > 2:
                array[i][x] = (0, 255, 0)

array = numpy.array(array).astype(numpy.uint8)
newImg = Image.fromarray(array).show()
