#!/usr/bin/env python3

import pygame
from random import randint, choice
from time import sleep

# setup bind keyboard
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


DEBUG = True

SPEED = 1
LENGTH = 2


class GameOBJ(pygame.sprite.Sprite):
    """Базовый класс для всех объектов игры"""
    def __init__(self, size_h=0, size_w=0):
        self.size_h = size_h
        self.size_w = size_w
        super().__init__()
        self.surf = pygame.Surface((
            size_w,
            size_h
        ))
        self.rect = self.surf.get_rect()


class Cell(GameOBJ):
    """Описание одной ячейки"""
    __number__ = 0
    __value__ = 0

    def __init__(self, x=0, y=0, size_h=0, size_w=0):
        Cell.__number__ += 1
        self.__color__ = (0, 100, 255)
        super().__init__(size_h=size_h, size_w=size_w)
        self.surf.fill(self.__color__)
        self.__x__ = x
        self.__y__ = y
        self.size_h = size_h
        self.size_w = size_w

    def __repr__(self):
        return f"Represent from cell #{self.__number__}"

    def __str__(self):
        return f"I'm cell #{self.__number__} and value {self.value}"

    def get_position(self):
        return self.x * self.size_h, self.y * self.size_w

    def change_color(self, color):
        self.surf.fill(color)

    @property
    def value(self):
        return self.__value__

    @value.setter
    def value(self, v):
        if v >= -1:
            self.__value__ = v
        else:
            self.__value__ = 0

    @property
    def x(self):
        return self.__x__

    @x.setter
    def x(self, x):
        if x >= 0:
            self.__x__ = x
        else:
            raise ValueError

    @property
    def y(self):
        return self.__y__

    @y.setter
    def y(self, y):
        if y >= 0:
            self.__y__ = y
        else:
            raise ValueError


class Field:
    """Содержит поле из ячеек"""
    def __init__(self, w=8, h=8):
        self.__cells__ = []
        self.__width__ = w  # ширина
        self.__height__ = h  # высота

        pxl_wight = int(MainWindow.__SCREEN_WIGHT__ / w)
        pxl_height = int(MainWindow.__SCREEN_HEIGHT__ / h)

        for j in range(w):  # Y
            for i in range(h):  # X
                self.__cells__.append(Cell(i, j, size_w=pxl_wight, size_h=pxl_height))

    @property
    def cells(self) -> list:
        return self.__cells__

    def get_cell_by_number(self, number):
        return self.cells[number]

    def set_value_by_cell_number(self, value, number):
        self.cells[number].value = value

    def get_coordinates_from_cell_number(self, number) -> tuple:
        tmp = 0
        for j in range(self.__width__):  # Y
            for i in range(self.__height__):  # X
                tmp += 1
                if tmp == number:
                    return i, j
        return -1, -1

    def get_cell_number_from_coordinates(self, x, y) -> int:
        # TODO: Needs to optimize this part of code. Maybe named dict and move to __init__
        for c in self.cells:
            if c.x == x and c.y == y:
                return c.__number__ -1


class Apple:
    """Описание яблока"""
    def __init__(self, field, cell_num=None):
        if cell_num is None:
            cell_num = randint(0, Cell.__number__)
        self.value = -1
        self.color = (255, 0, 0)
        self.__number__ = cell_num
        field.set_value_by_cell_number(self.value, cell_num)
        self.cell = field.get_cell_by_number(cell_num)
        self.surf = self.cell.surf
        self.cell.change_color(self.color)

    def get_position(self):
        return self.cell.get_position()

    def __repr__(self):
        return f"Represent from the Apple #{self.__number__} cell"

    def __str__(self):
        return f"Apple in the cell #{self.__number__}"


class Snake:
    """Змейка"""
    __length__ = LENGTH
    __speed__ = SPEED
    color = (0, 255, 0)

    def __init__(self, field, cell_num=None):
        # Check the cell number and set LENGTH as value
        if cell_num is None:
            cell_num = randint(0, Cell.__number__ - 1)
        self.__head_in_cell__ = cell_num
        field.set_value_by_cell_number(self.length, cell_num)
        self.__movements__ = [self.move_right, self.move_left, self.move_up, self.move_down]
        self.move = choice(self.__movements__)
        self.x, self.y = field.get_coordinates_from_cell_number(cell_num)
        self.color = Snake.color
        self.cell = field.get_cell_by_number(cell_num)
        self.surf = self.cell.surf
        self.cell.change_color(self.color)

    def get_position(self):
        return self.cell.get_position()

    def move_right(self, field):
        if self.x < field.__height__ - 1 and \
                field.cells[field.get_cell_number_from_coordinates(self.x + 1, self.y)].value < 1:
            cell_num = field.get_cell_number_from_coordinates(self.x + 1, self.y)
            self.__head_in_cell__ = cell_num
            field.set_value_by_cell_number(self.length, self.__head_in_cell__)
            self.x += 1
        else:
            raise IndexError

    def move_left(self, field):
        if self.x > 0 and \
                field.cells[field.get_cell_number_from_coordinates(self.x - 1, self.y)].value < 1:
            cell_num = field.get_cell_number_from_coordinates(self.x - 1, self.y)
            self.__head_in_cell__ = cell_num
            field.set_value_by_cell_number(self.length, self.__head_in_cell__)
            self.x -= 1
        else:
            raise IndexError

    def move_up(self, field):
        print(f"field.cells[{field.get_cell_number_from_coordinates(self.x, self.y - 1)}].value")
        if self.y > 0 and \
                field.cells[field.get_cell_number_from_coordinates(self.x, self.y - 1)].value < 1:
            cell_num = field.get_cell_number_from_coordinates(self.x, self.y - 1)
            self.__head_in_cell__ = cell_num
            field.set_value_by_cell_number(self.length, self.__head_in_cell__)
            self.y -= 1
        else:
            raise IndexError

    def move_down(self, field):
        if self.y < field.__width__ - 1 and \
                field.cells[field.get_cell_number_from_coordinates(self.x, self.y + 1)].value < 1:
            cell_num = field.get_cell_number_from_coordinates(self.x, self.y + 1)
            self.__head_in_cell__ = cell_num
            field.set_value_by_cell_number(self.length, self.__head_in_cell__)
            self.y += 1
        else:
            raise IndexError

    def step(self, field):
        self.move(field)

    # Speed
    @property
    def speed(self):
        return self.__speed__

    @speed.setter
    def speed(self, speed):
        self.__speed__ = speed

    # Length
    @property
    def length(self):
        return self.__length__

    @length.setter
    def length(self, value):
        self.__length__ += value

    def __repr__(self):
        return f"(REPR) Snake = {self.__speed__} {self.__length__} {self.__head_in_cell__}"

    def __str__(self):
        return f"(STR) Snake = {self.__speed__} {self.__length__} {self.__head_in_cell__}"


class MainWindow:
    __SCREEN_WIGHT__ = 800
    __SCREEN_HEIGHT__ = 800

    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((self.__SCREEN_WIGHT__, self.__SCREEN_HEIGHT__))
        pygame.display.set_caption("Snake game")

        # Screen filling
        self.screen.fill((0, 100, 0))

        self._field = Field()
        self._snake = Snake(self._field, 15)
        self._apple = Apple(self._field, 40)
        self.game = True
        self.__score__ = 0

    def draw(self, target):
        self.screen.blit(target.surf, target.get_position())

    def flip(self):
        pygame.display.flip()

    def start(self):
        game = True
        print(f"{self._snake.__doc__}")
        while game:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game = False
                        continue
                    elif event.key == K_UP:
                        if DEBUG: print(f"{event.key=}")
                        self.m = self._snake.move_up
                    elif event.key == K_DOWN:
                        if DEBUG: print(f"{event.key=}")
                        self.m = self._snake.move_down
                    elif event.key == K_LEFT:
                        if DEBUG: print(f"{event.key=}")
                        self.m = self._snake.move_left
                    elif event.key == K_RIGHT:
                        if DEBUG: print(f"{event.key=}")
                        self.m = self._snake.move_right
                elif event.type == QUIT:
                    game = False
            self._snake.step(self._field)
            self.draw(self._apple)
            self.draw(self._snake)
            self.flip()
            sleep(self._snake.speed)

    @property
    def score(self):
        return self.__score__

    @score.setter
    def score(self, value):
        self.__score__ += 1


def main():
    game = MainWindow()
    game.start()


if __name__ == "__main__":
    main()
