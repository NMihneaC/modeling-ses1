import random

class Point:
    """
    class modeling a real life 2D point
    """
    def __init__(self,x,y):
        """
        Initialize the point instance
        :param x: the x-axis coordinate value
        :param y: the y-axis coordinate value
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        defines how a point is printed
        """
        return f"<{self.x},{self.y}>"

    def __repr__(self):
        return self.__str__()

    def dist_orig(self):
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self,other):
        """
        called when you do self > other
        :return: True/False
        """
        return self.dist_orig() > other.dist_orig()

    def __eq__(self, other):
        return self.dist_orig() == other.dist_orig()

p1 = Point(1,2) #create new instance
p2 = Point(3,4)
print(p1.x,p2.y)#access attributes

points = []
for i in range(5):
    #create a random point
    p = Point(
        random.randint(-100,100),
        random.randint(-100, 100)
    )
    #append it to the list
    points.append(p)

for point in points:
    print(points)

p = Point(12,5)
print(p.dist_orig())

print(p1 < p2)

points.sort()
print(points)

found_equal = 0
count = 0
while True:
    if found_equal == 10:
        break
    p1 = Point(
        random.randint(-100,100),
        random.randint(-100, 100)
    )
    p2 = Point(
        random.randint(-100,100),
        random.randint(-100,100)
    )
    count += 1
    if p1 == p2:
        #print(p1, p2)
        found_equal +=1

print(f"probability is 1 in {count/found_equal}")