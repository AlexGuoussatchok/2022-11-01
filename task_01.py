class Rectangle:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def calculate_square(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return (self.a + self.b) * 2

    def get_info(self):
        return f"Rectangle: a = {self.a}, b = {self.b}"

    def calculate_square(self, side_1, side_2):
        square = side_1 * side_2
        return square


# rect_1 = Rectangle(10, 15)
# rect_2 = Rectangle(20, 10)
# rect_3 = Rectangle(20)
# rect_4 = Rectangle()
# rect_5 = Rectangle()
# rect_6 = Rectangle()
# rect_7 = Rectangle()
# rect_8 = Rectangle()
# rect_9 = Rectangle()
# rect_10 = Rectangle()
#
# print(rect_1.get_info())
# print(rect_2.get_info())
# print(rect_3.get_info())
# print(rect_4.get_info())
# print(rect_5.get_info())
