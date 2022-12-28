import numpy
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.figure import Figure


def main():
    r = Rectangle("синего", 6, 3)
    c = Circle("зеленого", 8)
    s = Square("красного", 8)
    print(r)
    print(c)
    print(s)
    print(numpy.array((r, c, s), dtype=Figure))

if __name__ == "__main__":
    main()
