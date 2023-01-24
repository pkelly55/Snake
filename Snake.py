"Snake Game to play in terminal" 
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# Initialize curses
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)
#Set up game for saving high score

# Snake and food
snake = [[4,10], [4,9], [4,8]]
food = [10,20]
burger = '🍔'
#use burger emoji for food
win.addch(food[0], food[1], burger)
# Game logic
score = 0
ESC = 27
key = KEY_RIGHT
while key != ESC:
    win.border(0)
    #create high score file
    with open('highscore.txt', 'w') as f:
        f.write(str(score))
    with open('highscore.txt', 'r') as f:
        highscore = int(f.read())
    # Print welcome message for amount of time of 1 second
    win.addstr(0, 43, 'High Score : ' + str(highscore) + ' ')
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    win.addstr(0, 27, ' SNAKE ')
    win.timeout(int(150 - (len(snake)/5 + len(snake)/10)%120))
    prevKey = key
    event = win.getch()

    
    key = key if event == -1 else event
    if key == ord(' '):
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, ESC]:
        key = prevKey
    # Calculate the new coordinates of the head of the snake.
    y = snake[0][0]
    x = snake[0][1]
    if key == KEY_DOWN:
        y += 1
    if key == KEY_UP:
        y -= 1
    if key == KEY_LEFT:
        x -= 1
    if key == KEY_RIGHT:
        x += 1
    snake.insert(0, [y, x])
    # If snake crosses the boundaries, make it enter from the other side
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1
    
    # If snake runs over itself
    if snake[0] in snake[1:]: 
        break
    if snake[0] == food:
        # Eat the food
        score += 1
        food = []
        while food == []:
            food = [randint(1, 18), randint(1, 58)]
            if food in snake:
                food = []
        win.addch(food[0], food[1], '*')
    else:
        # Move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')
curses.endwin()
print(f"Final score = {score}")
#When a round ends ask to play again
#Let play loop last forever until user quits


