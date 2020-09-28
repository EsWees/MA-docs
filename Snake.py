#!/usr/bin/env python3

# Import pygame main lib
import pygame

# For using randint, choice, randrange
from random import randint, choice, randrange

# For sleep function
from time import sleep

import argparse

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

parser = argparse.ArgumentParser(description='The Python Snake game')
parser.add_argument('-a', '--auto', action='store_const', const=True, help='Try to play in auto mode')

args = parser.parse_args()

print(f'{args=}')

# Define screen size
FIELD_WIDTH = FIELD_HEIGHT = 80
SCREEN_WIDTH = SCREEN_HEIGHT = 800

FIELD_ITEM_WIDTH = int(SCREEN_WIDTH / FIELD_WIDTH)
FIELD_ITEM_HEIGHT = int(SCREEN_HEIGHT / FIELD_HEIGHT)

# Make empty bitmap
# for j in range(FIELD_HEIGHT):
#     for i in range(FIELD_WIDTH):
#         SCREEN_MAP[i][j] = 0
SCREEN_MAP = [[0 for i in range(0, FIELD_WIDTH, 1)] for j in range(0, FIELD_HEIGHT, 1)]

# Set the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Should be a Class or magic function
SPEED = 0.05


# Define a Snake object as a sprite
class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, length=5):
        super(Snake, self).__init__()

        self.surf = pygame.Surface((
            FIELD_ITEM_WIDTH,
            FIELD_ITEM_HEIGHT
        ))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()

        self.length = length
        SCREEN_MAP[x][y] = self.length
        self.x, self.y = x, y
        self.movements = [self.move_right, self.move_left, self.move_up, self.move_down]
        self.move = choice(self.movements)

    def step(self):
        SCREEN_MAP[self.x][self.y] = self.length - 1
        if args.auto:
            try:
                self.move()
            except Exception as error:
                print(f"Oops! {error.__class__.__name__}. {error=}")
                self.auto_move()
                pass
        else:
            self.move()

    def get_position(self):
        return self.x * FIELD_ITEM_WIDTH, self.y * FIELD_ITEM_HEIGHT

    def move_up(self) -> tuple:
        self.move = self.move_up
        if 0 < self.y and SCREEN_MAP[self.x][self.y - 1] < 1:
            self.y -= 1
        elif SCREEN_MAP[self.x][self.y - 1] > 1:
            raise EOFError
        else:
            raise IndexError
        return self.x, self.y

    def move_down(self) -> tuple:
        self.move = self.move_down
        if self.y < FIELD_WIDTH - 1 and SCREEN_MAP[self.x][self.y + 1] < 1:
            self.y += 1
        elif SCREEN_MAP[self.x][self.y + 1] > 1:
            raise EOFError
        else:
            raise IndexError
        return self.x, self.y

    def move_left(self) -> tuple:
        self.move = self.move_left
        if 0 < self.x and SCREEN_MAP[self.x - 1][self.y] < 1:
            self.x -= 1
        elif SCREEN_MAP[self.x - 1][self.y] > 1:
            raise EOFError
        else:
            raise IndexError
        return self.x, self.y

    def move_right(self) -> tuple:
        self.move = self.move_right
        if self.x < FIELD_HEIGHT - 1 and SCREEN_MAP[self.x + 1][self.y] < 1:
            self.x += 1
        elif SCREEN_MAP[self.x + 1][self.y] > 1:
            raise EOFError
        else:         
            raise IndexError
        return self.x, self.y

    def auto_move(self) -> tuple:
        if self.x < FIELD_HEIGHT and SCREEN_MAP[self.x + 1][self.y] < 1:
            self.x += 1
        elif 0 < self.x and SCREEN_MAP[self.x - 1][self.y] > 1:
            self.x -= 1
        elif self.y < FIELD_WIDTH and SCREEN_MAP[self.x][self.y + 1] > 1:
            self.y += 1
        elif 0 < self.y and SCREEN_MAP[self.x][self.y - 1] < 1:
            self.y -= 1
        return self.x, self.y


# Define a Dot object as a sprite
class Dot(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        # I do not know what is the "super" object
        super(Dot, self).__init__()

        self.surf = pygame.Surface((
            FIELD_ITEM_WIDTH,
            FIELD_ITEM_HEIGHT
        ))

        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.surf.set_alpha(255)

        if x is not None is not y:
            SCREEN_MAP[x][y] = -1
        else:
            x, y = randint(0, FIELD_WIDTH - 1), randint(0, FIELD_HEIGHT - 1)
            SCREEN_MAP[x][y] = -1

        self.position = [FIELD_ITEM_WIDTH * x, FIELD_ITEM_HEIGHT * y]


# Event handler
def event_processing():
    # process events
    for event in pygame.event.get():
        # if key pressed
        if event.type == KEYDOWN:
            # ESC event
            if event.key == K_ESCAPE:
                return False
            # UP event
            elif event.key == K_UP:
                snake.move = snake.move_up
            # DOWN event
            elif event.key == K_DOWN:
                snake.move = snake.move_down
            # LEFT event
            elif event.key == K_LEFT:
                snake.move = snake.move_left
            # RIGHT event
            elif event.key == K_RIGHT:
                snake.move = snake.move_right
        # if got quit event
        elif event.type == QUIT:
            return False
    return True


# Setup Snake
snake = Snake(FIELD_WIDTH // 2, FIELD_HEIGHT // 2)


def main():
    """
    the main function. The Snake game
    """
    # Init pygame module
    pygame.init()

    point = pygame.Surface((
        FIELD_ITEM_WIDTH,
        FIELD_ITEM_HEIGHT
    ))

    # Setup Target
    target = Dot()

    # main loop
    while event_processing():
        snake.step()

        # Screen filling
        screen.fill((255, 255, 255))

        for i in range(FIELD_WIDTH):
            for j in range(FIELD_HEIGHT):
                # Background
                point.fill((0, randint(99, 100), randint(0, 20)))
                screen.blit(point, [FIELD_ITEM_WIDTH * i, FIELD_ITEM_HEIGHT * j])

                # Draw the dot target
                if SCREEN_MAP[i][j] == -1:
                    screen.blit(target.surf, target.position)

                # Draw the snake
                if SCREEN_MAP[i][j] == snake.length - 1:
                    snake.surf.fill((0, 200, 255))
                    screen.blit(snake.surf, snake.get_position())

                # Snake tail control
                if SCREEN_MAP[i][j] > 0:
                    point.fill((100, 255, 200))
                    screen.blit(point, [FIELD_ITEM_WIDTH * i, FIELD_ITEM_HEIGHT * j])
                    SCREEN_MAP[i][j] -= 1

        # Show the bitmap
        pygame.display.flip()

        # Speed controller
        sleep(SPEED)

    # Exit from the app with regular exit code
    pygame.quit()


if __name__ == "__main__":
    main()
