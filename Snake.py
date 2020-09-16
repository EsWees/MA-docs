#!/usr/bin/env python3.8

# Import libs
import os
import time
import random


def clear(func):
    """Detect OS. Set clear function"""
    def screen():
        if os.name == 'nt':
            clear = os.system('cls')
        else:
            clear = os.system('clear')
        func()
    return screen


def new_dot(x=None, y=None):
    """Makes new dot on the field"""
    if x and y:
        field[x][y] = -1
    else:
        field[random.randint(0, min(m, n) - 1)][random.randint(0, min(m, n) - 1)] = -1


@clear
def show_field():
    """show actual field with snake"""
    for j in range(n + 1):
        for i in range(m + 1):

            # Empty field
            if field[i][j] == 0:
                print(' ', end=' ')

            # Show the point
            elif field[i][j] == -1:
                print('\033[89m\033[1m0\033[0m', end=' ')

            # Show the Snake head
            elif field[i][j] == snake_length[0]:
                print('\033[91m*\033[0m', end=' ')

            # Show the Snake tail            
            elif field[i][j] == 1:
                print('\033[93m*\033[0m', end=' ')

            # Show the Snake body
            else:
                print('\033[92m*\033[0m', end=' ')

            # Show right corner of the field
            if i == m:
                print('|', end='')

            # Tail control
            if field[i][j] > 0:
                field[i][j] -= 1

        # New line
        print('')

    # Show buttom line
    print('_' * (n * 2 + 2), end="|\n")
    print(f'Score: {snake_dots[0]}')


def post(func):
    """
    Post move as a decorator
    :param: function
    :return: link to post_moving function
    """
    def post_moving(x, y):
        #print(f"{x=}, {y=}")
        x, y = func(x, y)
        if field[x][y] == -1:
            step[0] /= 2
            snake_length[0] += 2
            snake_dots[0] += 1
            new_dot()
        field[x][y] = snake_length[0]
        show_field()
        time.sleep(step[0])
        #clear()
        return x, y
    return post_moving
        
    
@post
def move_up(x:int, y:int) -> tuple:
    field[x][y] = snake_length[0] - 1
    if 0 < y and field[x][y - 1] < 1:
        y -= 1
    elif field[x][y - 1] > 1:
        raise EOFError
    else:
        raise IndexError
    return x, y


@post
def move_down(x:int, y:int) -> tuple:
    field[x][y] = snake_length[0] - 1
    if y < m - 1 and field[x][y + 1] < 1:
        y += 1
    elif field[x][y + 1] > 1:
        raise EOFError
    else:
        raise IndexError
    return x, y


@post
def move_left(x:int, y:int) -> tuple:
    field[x][y] = snake_length[0] - 1
    if 0 < x and field[x - 1][y] < 1:
        x -= 1
    elif field[x - 1][y] > 1:
        raise EOFError
    else:
        raise IndexError
    return x, y


@post
def move_right(x:int, y:int) -> tuple:
    field[x][y] = snake_length[0] - 1
    if x < n - 1 and field[x + 1][y] > 1:
        x += 1
    elif field[x + 1][y] < 1:
        raise EOFError
    else:
        raise IndexError
    return x, y


@post
def auto_move(x:int, y:int) -> tuple:
    if x < n and field[x + 1][y] < 1:
        x += 1
    elif 0 < x and field[x - 1][y] > 1:
        x -= 1
    elif y < m and field[x][y + 1] > 1:
        y += 1
    elif 0 < y and field[x][y - 1] < 1:
        y -= 1
    field[x][y] = snake_length[0] - 1
    return x, y


def pause(seconds:int=3) -> None:
    for i in range(seconds, 1, -1):
        print(f'New game in {i} second(s)', end='', flush=True)
        time.sleep(1)
        print(f'\b' * 500, end='', flush=True)


movements = [move_right, move_left, move_up, move_down]

auto_play = True

# Set Snake field
n = m = 20


while True:
    # start position it is center of the field
    x = int(n / 2)
    y = int(m / 2)

    # snake length by default
    snake_length = [5]

    # use step as a user level (seconds between step)
    step = [0.5]

    # Uses like a score
    snake_dots = [0]

    # field[n][m] = {0}
    field = [[0 for i in range(n + 1)] for j in range(m + 1)]
    new_dot()


    # Will be a new feature.
    # auto_move function will use this map to reach the -1 field
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
            if auto_play:
                func = random.choice(movements)
                for i in range(random.randrange(1, min(n, m))):
                    x, y = func(x, y)
            else:
                print("Sorry. User game is not implemented yet.")
                exit(1)
        except EOFError:
            if auto_play:
                x, y = auto_move(x, y)
            else:
                print(f'You was bitten by yourself')
                pause()
                break
        except IndexError:
            if auto_play:
                x, y = auto_move(x, y)
            else:
                print(f'Out Of Range')
                pause()
                break
        except KeyboardInterrupt as err:
            print("\nStop the Snake game\nPress one more time to finish the program")
            pause(10)
            break
        except Exception as error:
            print(f'Undefined behavior: {error.__class__.__name__}, error')
            break

    show_field()
    print(f'Game Over!')

