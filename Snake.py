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

# Argument parser
parser = argparse.ArgumentParser(description='The Python Snake game')
parser.add_argument('-a', '--auto', action='store_const', const=True, help='Try to play in auto mode')
args = parser.parse_args()

# Define screen size
FIELD_WIDTH = FIELD_HEIGHT = 20
SCREEN_WIDTH = SCREEN_HEIGHT = 800

# Calculate one item of the game field
FIELD_ITEM_WIDTH = int(SCREEN_WIDTH / FIELD_WIDTH)
FIELD_ITEM_HEIGHT = int(SCREEN_HEIGHT / FIELD_HEIGHT)

# Make empty bitmap
# for j in range(FIELD_HEIGHT):
#     for i in range(FIELD_WIDTH):
#         SCREEN_MAP[i][j] = 0
SCREEN_MAP = [[0 for i in range(0, FIELD_WIDTH)] for j in range(0, FIELD_HEIGHT)]

# Set the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Snake speed movement
# Should be a Class or magic function
SPEED = 0.5


# Define an auto_move function
def auto_move(future_step) -> tuple:
    future_x, future_y = future_step
    if SCREEN_MAP[future_x][future_y] > 1:
        print(f"AM ==>> {SCREEN_MAP[future_x][future_y]=}")

        if future_x >= 0 and SCREEN_MAP[future_x - 1][future_y] == 0:
            print(f"LEFT")
            return future_x - 1, future_y

        if future_x < FIELD_WIDTH and SCREEN_MAP[future_x + 1][future_y] == 0:
            print(f"RIGHT")
            return future_x + 1, future_y

        if future_y + 1 < FIELD_HEIGHT and SCREEN_MAP[future_x][future_y + 1] == 0:
            print(f"UP")
            return future_x, future_y + 1

        if future_y - 1 >= 0 and SCREEN_MAP[future_x][future_y - 1] == 0:
            print(f"DOWN")
            return future_x, future_y - 1

        if SCREEN_MAP[future_x][future_y] == 0:
            print(f"What ? -_-")
            return future_x, future_y

    return future_x, future_y


class Snake(pygame.sprite.Sprite):
    """
    The Snake class shows all of Snake characteristics like as:
        color
        rectangle
        head position
        length
    """

    def __init__(self, x, y, length=5):
        super(Snake, self).__init__()

        self.surf = pygame.Surface((
            FIELD_ITEM_WIDTH,
            FIELD_ITEM_HEIGHT
        ))
        self.rect = self.surf.get_rect()
        self.color = (100, 255, 200)  # Light blue
        self.surf.fill(self.color)
        self.x, self.y = x, y
        self.position = x, y

        self.length = length
        self.movements = [self.move_right, self.move_left, self.move_up, self.move_down]
        self.move = choice(self.movements)

    def step(self):
        """ actually it's can be a wrapper """
        SCREEN_MAP[self.x][self.y] = self.length - 1
        self.move()
        self.position = self.x, self.y

    def get_position(self):
        return self.x * FIELD_ITEM_WIDTH, self.y * FIELD_ITEM_HEIGHT

    def move_up(self) -> tuple:
        if 0 < self.y and SCREEN_MAP[self.x][self.y - 1] < 1:
            self.y -= 1
        elif SCREEN_MAP[self.x][self.y - 1] > 1:
            raise EOFError
        else:
            raise IndexError
        return self.x, self.y

    def move_down(self) -> tuple:
        if self.y < FIELD_WIDTH - 1 and SCREEN_MAP[self.x][self.y + 1] < 1:
            self.y += 1
        elif SCREEN_MAP[self.x][self.y + 1] > 1:
            raise EOFError
        else:
            raise IndexError
        return self.x, self.y

    def move_left(self) -> tuple:
        if 0 < self.x and SCREEN_MAP[self.x - 1][self.y] < 1:
            self.x -= 1
        elif SCREEN_MAP[self.x - 1][self.y] > 1:
            raise EOFError
        else:
            raise IndexError
        return self.x, self.y

    def move_right(self) -> tuple:
        if self.x < FIELD_HEIGHT - 1 and SCREEN_MAP[self.x + 1][self.y] < 1:
            self.x += 1
        elif SCREEN_MAP[self.x + 1][self.y] > 1:
            raise EOFError
        else:
            raise IndexError
        return self.x, self.y


class Dot(pygame.sprite.Sprite):
    """ Dot object as a sprite """

    def __init__(self, x=None, y=None):
        super(Dot, self).__init__()

        self.surf = pygame.Surface((
            FIELD_ITEM_WIDTH,
            FIELD_ITEM_HEIGHT
        ))

        self.surf.fill((255, 0, 0))  # red
        self.rect = self.surf.get_rect()
        self.surf.set_alpha(255)  # clearly

        # If some position was defined as a argument for the Dot class
        if x is not None is not y:
            SCREEN_MAP[x][y] = -1
        else:
            x, y = randint(0, FIELD_WIDTH - 1), randint(0, FIELD_HEIGHT - 1)
            SCREEN_MAP[x][y] = -1

        self.x, self.y = x, y
        self.position = x, y

    def get_position(self):
        return self.x * FIELD_ITEM_WIDTH, self.y * FIELD_ITEM_HEIGHT


# Event handler
def event_processing(snake):
    # process keyboard events
    for event in pygame.event.get():
        # if key pressed
        if event.type == KEYDOWN and not args.auto:
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


def show_score(snake):
    font1 = pygame.font.Font(None, 50)
    text1 = font1.render(f"Score {int(snake.length / 5 - 1)}", 0, (255, 255, 255))
    text1.set_alpha(90)
    screen.blit(text1, (10, SCREEN_HEIGHT - 50))

def main():
    """
    the main function. The Snake game
    """
    # Init pygame module
    pygame.init()

    # Make one point on the Snake field
    point = pygame.Surface((
        FIELD_ITEM_WIDTH,
        FIELD_ITEM_HEIGHT
    ))

    # Setup Target
    target = Dot(7, 7)

    # Setup Snake
    snake = Snake(FIELD_WIDTH // 2, FIELD_HEIGHT // 2)

    def ai_move(tgt, snk) -> tuple:
        """
        Make a snake move to target
        :param tgt: Target position. For ex.: (15, 19)
        :param snk: Snake position. For ex.: (99, 40)
        :return: Next Snake position close to Target
        """
        tx, ty = tgt
        sx, sy = snk
        if tx > sx:
            return sx + 1, sy
        elif tx < sx:
            return sx - 1, sy
        elif ty > sy:
            return sx, sy + 1
        elif ty < sy:
            return sx, sy - 1

    # main loop
    while event_processing(snake):
        """ until event can be processed """
        if args.auto:
            """ auto play is enabled """
            SCREEN_MAP[snake.x][snake.y] = snake.length
            snake.x, snake.y = auto_move(ai_move(target.position, snake.position))
            snake.position = snake.x, snake.y
        else:
            snake.step()

        if target.position == snake.position:
            target = Dot()
            snake.length += 5
            global SPEED
            SPEED /= 1.1

        # Screen filling
        screen.fill((0, 100, 25))
        screen.blit(target.surf, target.get_position())

        for i in range(0, FIELD_WIDTH):
            for j in range(0, FIELD_HEIGHT):
                # Snake head
                if (i, j) == snake.position:
                    snake.surf.fill((255, 255, 0))  # Yellow
                    screen.blit(snake.surf, snake.get_position())

                # Snake tail control
                if SCREEN_MAP[i][j] >= 0:
                    SCREEN_MAP[i][j] -= 1
                    point.fill(snake.color)
                    screen.blit(point, [FIELD_ITEM_WIDTH * i, FIELD_ITEM_HEIGHT * j])

        show_score(snake)

        # Show the bitmap
        pygame.display.flip()

        # Speed controller
        sleep(SPEED)

    # Exit from the app with regular exit code
    pygame.quit()


if __name__ == "__main__":
    main()
