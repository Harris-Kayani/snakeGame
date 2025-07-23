import pygame
import random
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

font = pygame.font.SysFont("comicsans", 30)
snake_block = 10
snake_speed = 15

head = pygame.image.load("add_your_own").convert_alpha()
head = pygame.transform.smoothscale(head, (50, 50))

food = pygame.image.load("add_your_own").convert_alpha()
food = pygame.transform.smoothscale(food, (50, 50))


clock = pygame.time.Clock()

snake = [(200, 300)]
direction = 'RIGHT'
game_over = False

food_x = random.randint(0, width - snake_block) // 10 * 10
food_y = random.randint(0, height - snake_block) // 10 * 10

def show_score(score):
    value = font.render("Score: " + str(score), True, white)
    screen.blit(value, [10, 10])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    x, y = snake[0]
    if direction == 'UP':
        y -= snake_block
    elif direction == 'DOWN':
        y += snake_block
    elif direction == 'LEFT':
        x -= snake_block
    elif direction == 'RIGHT':
        x += snake_block

    new_head = (x, y)
    snake.insert(0, new_head)

    if snake[0] == (food_x, food_y):
        food_x = random.randint(0, width - snake_block) // 10 * 10
        food_y = random.randint(0, height - snake_block) // 10 * 10
    else:
        snake.pop()
    if x < 0 or x >= width or y < 0 or y >= height:
        game_over = True

    if snake[0] in snake[1:]:
        game_over = True

    screen.fill(black)
    for pos in snake:
        screen.blit(head, pos)

        screen.blit(food, (food_x, food_y))

    show_score(len(snake) - 1)
    pygame.display.update()

    clock.tick(snake_speed)

screen.fill(black)
msg = font.render("Game Over! Press Q to leave.", True, red)
screen.blit(msg, [width // 4, height // 2])
pygame.display.update()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                waiting = False

pygame.quit()
