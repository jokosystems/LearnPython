# Given Three Points (x1, y1), (x2, y2) and (x3, y3), Write a Python
# Program to Check If they are Collinear (y3-y2)*(x2-x1) = (x3-x2)*(x2-x1)
class Collinear:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def check_collinear(self, p2, p3):
        # if (p3.y_coord - p2.y_coord) * (p2.x_coord - self.x_coord) ==
        # (p2.y_coord - self.y_coord) * (p3.x_coord - p2.x_coord):
        p32 = (p3.y_coord - p2.y_coord) * (p2.x_coord - self.x_coord)
        p321 = (p3.x_coord - p2.x_coord) * (p2.y_coord - self.y_coord)
        if p32 == p321:
            print("Points are Collinear")
        else:
            print("Points NOT Collinear")


def main():
    point_1 = Collinear(1, 4)
    point_2 = Collinear(4, 7)
    point_3 = Collinear(7, 10)
    point_1.check_collinear(point_2, point_3)


if __name__ == "__main__":
    main()
