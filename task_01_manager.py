from task_01_2 import RectangleCreator
from task_01_logic import Logic
from task_01_view import View


def main():
    size = 5
    ls = RectangleCreator.get_rectangle(size)
    total_square = Logic.calculate_total_square(ls)
    total_perimeter = Logic.calculate_total_perimenter(ls)

    msg = (f"Total square = {total_square},\n total perimeter = {total_perimeter}")

    print(View.convert())
    print(msg)


if __name__ == "__main__":
    main()
