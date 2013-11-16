class Coordinates(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def relativeTo(self, direction):
        if direction == 'up':
            return Coordinate(self.x, self.y+1)
        if direction == 'right':
            return Coordinate(self.x+1, self.y)
        if direction == 'left':
            return Coordinate(self.x-1, self.y)
        if direction == 'down':
            return Coordinate(self.x, self.y-1)
        return False

class Possibilities(object):

    def __init__(self, up, right, left, down):
        self.up = up
        self.right = right
        self.left = left
        self.down = down
    
    def nextPossibility(self):
        if self.up:
            self.up = False
            return 'up'
        if self.right:
            self.right = False
            return 'right'
        if self.left:
            self.left = False
            return 'left'
        if self.down:
            self.down = False
            return 'down'
        return False

class Position(object):

    def __init__(self, x, y, possibilities):
        self.x = x
	self.y = y
        self.possibilities = possibilities
