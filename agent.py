from orientation import *

class Agent(object):

    def __init__(self, x, y, dungeon)
        self.x = x
        self.y = y
        self.dungeon = dungeon
        crd = Coordinates(x, y)
        self.position = Position(crd, findPossibilities(crd))

    def findPossibilities(self, crd)
        queue = [Coordinates(crd.x, crd.y+1),
                 Coordinates(crd.x+1, crd.y),
                 Coordinates(crd.x-1, crd.y),
                 Coordinates(crd.x, crd.y-1)]

        for i, item in enumerate(queue):
            if item.x < 0 || item.y < 0 || item.x > 24 || item.y > 24:
                queue[i]=False
            else
                if dungeon[item.y][item.x] == 1:
                    queue[i]=False
                else
                    if False: #Caminho foi percorrido
                        queue[i]=False
                    else
                        queue[i]=True

        return Possibilities(queue[0], queue[1], queue[2], queue[3])
