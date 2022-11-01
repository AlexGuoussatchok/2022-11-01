import random
from task_01 import Rectangle


class RectangleCreator:
    FIRST_SIDE_RANGE = 10
    SECOND_SIDE_RANGE = 10

    def get_rectangle(size):
        rectangles = []
        for _ in range(size):
            rect = Rectangle()
            rect.a = random.randint(1, RectangleCreator.FIRST_SIDE_RANGE)
            rect.b = random.randint(1, RectangleCreator.SECOND_SIDE_RANGE)
            rectangles.append(rect)

        return rectangles
