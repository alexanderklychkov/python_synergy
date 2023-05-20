class Turtle(object):
    __x = 0
    __y = 0
    __s = 1

    def __init__(self, s=1):
        self.__s = s

    def go_up(self):
        self.__y += self.__s

    def go_down(self):
        self.__y -= self.__s

    def go_left(self):
        self.__x -= self.__s

    def go_right(self):
        self.__x += self.__s

    def evolve(self):
        self.__s += 1

    def degrade(self):
        if self.__s - 1 <= 0:
            print('Скорость черепашки не может быть меньше 1')

        self.__s -= 1

    def count_moves(self, x2, y2):
        diff_x = abs(x2 - self.__x)
        diff_y = abs(y2 - self.__y)
        return diff_x // self.__s + diff_y // self.__s


turtle = Turtle()
turtle.evolve()
turtle.go_up()
turtle.go_down()
turtle.go_left()
turtle.go_right()
print(turtle.count_moves(10, 5))
