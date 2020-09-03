#!/usr/bin/env python3.8

# Import libs
import os
import time
import random

# Detect OS. Set clear function
if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

auto_play = True

# Clear the console screen
clear()

# Set Snake field
n = m = 20

def new_dot(x=None, y=None):
    """Makes new dot on the field"""
    if x and y:
        field[x][y] = -1
    else:
        field[random.randint(0, min(m, n) - 1)][random.randint(0, min(m, n) - 1)] = -1


def tail_field():
    """Snake tail control"""
    for j in range(n):
        for i in range(m):
            if field[i][j] > 0:
                field[i][j] -= 1


def show_field(field):
    """show actual field with snake"""
    for j in range(n + 1):
        for i in range(m + 1):
            if field[i][j] == 0:
                print(' ', end=' ')
            elif field[i][j] == -1:
                #print('\033[89m\033[1m0\033[0m', end=' ')
                print(field[i][j], end=' ')
            elif field[i][j] == snake_length[0]:
                #print('\033[91m*\033[0m', end=' ')
                print(field[i][j], end=' ')
            elif field[i][j] == 1:
                #print('\033[93m*\033[0m', end=' ')
                print(field[i][j], end=' ')
            else:
                #print('\033[92m*\033[0m', end=' ')
                print(field[i][j], end=' ')
            if i == m:
                print('|', end='')
        print('')
    tail_field()
    print('_' * n * 2)
    print(f'Score: {snake_dots[0]}')


def post_moving(x, y):
    if field[x][y] == -1:
        step[0] /= 2
        snake_length[0] += 2
        snake_dots[0] += 1
        new_dot()
    field[x][y] = snake_length[0]
    show_field()
    time.sleep(step[0])
    clear()
    return x, y


def move_up(x, y):
    field[x][y] = snake_length[0] - 1
    if 0 < y and field[x][y - 1] < 1:
        y -= 1
    elif field[x][y - 1] > 1:
        raise EOFError
    else:
        raise IndexError
    return post_moving(x, y)


def move_down(x, y):
    field[x][y] = snake_length[0] - 1
    if y < m - 1 and field[x][y + 1] < 1:
        y += 1
    elif field[x][y + 1] > 1:
        raise EOFError
    else:
        raise IndexError
    return post_moving(x, y)


def move_left(x, y):
    field[x][y] = snake_length[0] - 1
    if 0 < x and field[x - 1][y] < 1:
        x -= 1
    elif field[x - 1][y] > 1:
        raise EOFError
    else:
        raise IndexError
    return post_moving(x, y)


def move_right(x, y):
    field[x][y] = snake_length[0] - 1
    if x < n - 1 and field[x + 1][y] > 1:
        x += 1
    elif field[x + 1][y] < 1:
        raise EOFError
    else:
        raise IndexError
    return post_moving(x, y)


def auto_move(x, y):
    field[x][y] = snake_length[0] - 1
    if x < n - 1 and field[x + 1][y] < 1:
        x += 1
    elif 0 < x and field[x - 1][y] > 1:
        x -= 1
    elif y < m - 1 and field[x][y + 1] > 1:
        y += 1
    elif 0 < y and field[x][y - 1] < 1:
        y -= 1
    return post_moving(x, y)


movements = [move_right, move_left, move_up, move_down]

while True:
    # start position it is center of the field
    x = int(n / 2)
    y = int(m / 2)

    # snake length by default
    snake_length = [5]

    # use step as a user level (seconds between step)
    step = [0.1]

    # Uses like a score
    snake_dots = [0]

    # field[n][m] = {0}
    field = [[0 for i in range(n + 1)] for j in range(m + 1)]
    new_dot()

    score_field = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for j in range(n + 1):
        for i in range(m + 1):
            score = 0
            if i + 1 <= n:
                score += 1
            elif j + 1 <= m:
                score += 1
            elif i - 1 >= 0:
                score += 1
            elif j - 1 >= 0:
                score += 1
            score_field[i][j] = score

    while True:
        try:
            func = random.choice(movements)
            for i in range(random.randrange(1, min(n, m))):
                x, y = func(x, y)
        except EOFError:
            if auto_play:
                x, y = auto_move(x, y)
            else:
                print(f'You was bitten by yourself')
                break
        except IndexError:
            if auto_play:
                x, y = auto_move(x, y)
            else:
                print(f'Out Of Range')
                break
        except Exception as error:
            print(f'Undefined behavior: {error.__class__.__name__}, error')
            break

    show_field(field)
    print(f'Game Over!')

    if auto_play:
        for i in range(3, 1, -1):
            print(f'New game in {i} second(s)', end='', flush=True)
            time.sleep(1)
            print(f'\b' * 50, end='', flush=True)

    clear()
