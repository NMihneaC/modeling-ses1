from point import Point

class ColourPoint(Point):
    def __init__(self, x , y, colour):
        """
        Defines a colour point x, y, colour
        """
        self.x = x
        self.y = y
        self.colour = colour

    def __str__(self):
        return f"<{self.x},{self.y}>({self.colour})"

colour_points = []
for _ in range(5):
    p = ColourPoint(random.randint(-100, 100),
                    random.randint(-100, 100),
                    random.choice(colours)
                    )
    colour_points.append(p)
print("random colour points: ")
print(colour_points)
colour_points.sort()
print("sorted colour points: ")
print(colour_points)