class Circle:

    def area(self):
        radius = float(input("Enter radius of circle: "))
        area = 3.14 * radius * radius
        print("Area of Circle =", area)


class Rectangle:

    def area(self):
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print("Area of Rectangle =", area)


# Creating objects
c = Circle()
r = Rectangle()

# Calling methods
c.area()

print()

r.area()
