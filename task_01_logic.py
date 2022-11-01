from task_01 import Rectangle


class Logic:

    def calculate_total_square(rectangles):
        if isinstance(rectangles, (list, tuple)):
            total = 0
            for rect in rectangles:
                if isinstance(rect, Rectangle):
                    total += rect.calculate_square()

            return total

    def calculate_total_perimenter(rectangles):
        if isinstance(rectangles, (list, tuple)):
            total = 0
            for rect in rectangles:
                if isinstance(rect, Rectangle):
                    total += rect.calculate_perimeter()

            return total
