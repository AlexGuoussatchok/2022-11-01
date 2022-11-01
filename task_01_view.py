from task_01 import Rectangle


class View:
    def convert(rectangles):
        if isinstance(rectangles, (list, tuple)):
            result = ""
            for rect in rectangles:
                if isinstance(rect, Rectangle):
                    result += rect.get_info(ls) + "\n"

            return result