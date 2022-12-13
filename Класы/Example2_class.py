class Point(object):
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def point_coords(self):
        return (self.x, self.y)


class Rectangle(object):
    def __init__(self, left_bottom, top_right):
        self.left_bottom = left_bottom
        self.top_right = top_right
        self.top_left = (self.left_bottom[0], self.top_right[1])
        self.right_bottom = (self.top_right[0], self.left_bottom[1])
        self.height = ((self.top_left[1]-self.left_bottom[1])**2+(self.top_left[0]-self.left_bottom[0])**2)**0.5
        self.width = ((self.right_bottom[1]-self.left_bottom[1])**2+(self.right_bottom[0]-self.left_bottom[0])**2)**0.5

    def perimeter(self):
        return self.width*2+self.height*2

    def square(self):
        return self.width*self.height

    def contains(self, point):
        if (point[0] >= self.left_bottom[0] and point[0] <= self.right_bottom[0]) and (point[1] >= self.left_bottom[1] and point[1] <= self.top_left[1]):
            return True
        else:
            return False

p1 = Point(-3, 2).point_coords()
p2 = Point(6, 7).point_coords()
p3 = Point(4, 5).point_coords()
r = Rectangle(p1, p2)
print(r.height)
print(r.width)
print(r.perimeter())
print(r.square())
print(r.contains(p3))
