# Given the Coordinates (x, y) of a Center of a Circle and Its Radius,
# Write Python Program to Determine Whether the Point Lies Inside the Circle,
# On the Circle or Outside the Circle

class Circle:
    def __init__(self, cx=0, cy=0, r=0, px=0, py=0):
        self.cx_coord = cx
        self.cy_coord = cy
        self.r = r
        self.px_coord = px
        self.py_coord = py
        self.status = ""

    def check_circle(self):
        check_result = (self.px_coord - self.cx_coord)**2 + (self.py_coord - self.cy_coord)**2
        if check_result < self.r**2:
            self.status = f"Points with coordinates ({self.px_coord, self.py_coord}) is INSIDE the circle"
        elif check_result > self.r**2:
            self.status = f"Points with coordinates ({self.px_coord, self.py_coord}) is OUTSIDE the circle"
        else:
            self.status = f"Points with coordinates ({self.px_coord, self.py_coord}) is ON the circle"

        return self


def main():
    point = Circle(10, 2, 3, 9, 9)
    returned_object = point.check_circle()
    print(returned_object.status)
    print(f"Is point an instance of Circle Class? {isinstance(point, Circle)}")
    print(f"Is returned_object an instance of Circle Class? {isinstance(returned_object, Circle)}")
    print(f"Identity of the location of the returned_object object is {id(returned_object)}")
    print(f"Identity of the location of a point object is {id(point)}")


if __name__ == "__main__":
    main()
