import queue, numpy, time
from PIL import Image

def maze(mazename, start=True, end=True):
    f = 0
    q = queue.Queue()
    visited = []
    img = Image.open(mazename)
    array = numpy.array(img).tolist()
    for x, y in enumerate(array):
        for i, h in enumerate(y):
            if h == 0:
                array[x][i] = (0, 0, 0)
            else:
                array[x][i] = (255, 255, 255)
    if start and end:
        for x, y in enumerate(array[0]):
            if y == (255, 255, 255):
                start = [x+1, 1]
        for x, y in enumerate(array[-1]):
            if y == (255, 255, 255):
                end = [x+1, len(array)]
    start[0] = start[0]-1
    start[1] = start[1]-1
    end[0] = end[0]-1
    end[1] = end[1]-1
    start = tuple(start)
    q.put("")
    print("End", end)
    while True:
        f+=1
        #Checking for end
        parse = q.get()
        m = list(start)
        for i in parse:
            if i == "D":
                m[1] = m[1]+1
            if i == "U":
                m[1] = m[1]-1
            if i == "L":
                m[0] = m[0]-1
            if i == "R":
                m[0] = m[0]+1
        if m not in visited:
            visited.append(m)
            print(m, f)
            if m == end:
                m = list(start)
                array[m[1]][m[0]] = (255, 0, 0)
                for i in parse:
                    if i == "D":
                        m[1] = m[1]+1
                        array[m[1]][m[0]] = (255, 0, 0)
                    if i == "U":
                        m[1] = m[1]-1
                        array[m[1]][m[0]] = (255, 0, 0)
                    if i == "L":
                        m[0] = m[0]-1
                        array[m[1]][m[0]] = (255, 0, 0)
                    if i == "R":
                        m[0] = m[0]+1
                        array[m[1]][m[0]] = (255, 0, 0)
                return array
            #Find new trails
            directions = ["U", "D", "L", "R"]
            if m[0] == 0:
                directions.remove("L")
            elif array[m[1]][m[0]-1] == (0, 0, 0):
                directions.remove("L")
            if m[0]+1 == len(array[0]):
                directions.remove("R")
            elif array[m[1]][m[0]+1] == (0, 0, 0):
                directions.remove("R")
            if m[1] == 0:
                directions.remove('U')
            elif array[m[1]-1][m[0]] == (0, 0, 0):
                directions.remove('U')
            if m[1]+1 == len(array):
                directions.remove("D")
            elif array[m[1]+1][m[0]] == (0, 0, 0):
                directions.remove("D")
            for direction in directions:
                q.put(parse+direction)

t1 = time.time()
arr = maze(input("Enter maze file name: "))
print(time.time()-t1)
Image.fromarray(numpy.array(arr).astype(numpy.uint8)).show()
