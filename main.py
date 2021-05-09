from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

class Pathmaker:
	def __init__(self, x1=0, y1=0, x2=1, y2=1, segments=2):
		self.point1 = Point(x1, y1)
		self.point2 = Point(x2, y2)
		self.segments = segments-1

	def findIncrement(self):
		rawX, rawY = self.point1.x - self.point2.x, self.point1.y - self.point2.y
		self.incremntX = abs(rawX/self.segments)
		self.incremntY = abs(rawY/self.segments)
	
	def findPoints(self):
		x, y, = tuple(self.point1)
		self.points = []
		self.points.append(self.point1)
		for _ in range(self.segments):
			x += int(self.incremntX)
			y += int(self.incremntY)
			self.points.append(Point(x, y))



run = Pathmaker(0, 0, 10, 10, 10)
run.findIncrement()
run.findPoints()
print(run.points)