import pygame
import random
import time

pygame.init()

# --- НАСТРОЙКИ ---
WIDTH = 600
HEIGHT = 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Red Version")

clock = pygame.time.Clock()

# --- ФОН ---
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# --- ЦВЕТА ---
RED = (255, 0, 0)        # змейка
DARK_RED = (180, 0, 0)   # голова
BLACK = (0, 0, 0)

# --- ШРИФТ ---
font = pygame.font.SysFont(None, 30)

# --- ЗМЕЙКА ---
snake = [(100, 100), (80, 100), (60, 100)]
dx, dy = CELL, 0

# --- ГЕНЕРАЦИЯ ЕДЫ ---
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)

        if (x, y) not in snake:
            weight = random.choice([1, 2, 5])

            # цвет еды зависит от веса
            if weight == 1:
                color = (0, 200, 0)
            elif weight == 2:
                color = (255, 165, 0)
            else:
                color = (255, 0, 0)

            return {
                "pos": (x, y),
                "weight": weight,
                "color": color,
                "time": time.time()
            }

food = generate_food()

# --- ПАРАМЕТРЫ ---
score = 0
speed = 7
FOOD_LIFETIME = 5  # секунд

running = True
while running:

    # --- СОБЫТИЯ ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- УПРАВЛЕНИЕ ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL, 0

    # --- ДВИЖЕНИЕ ---
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    # --- СТОЛКНОВЕНИЕ СО СТЕНАМИ ---
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        print("GAME OVER")
        running = False

    # --- САМОСТОЛКНОВЕНИЕ ---
    if new_head in snake:
        print("GAME OVER")
        running = False

    snake.insert(0, new_head)

    # --- ПРОВЕРКА ЕДЫ ---
    if new_head == food["pos"]:
        score += food["weight"]
        food = generate_food()
    else:
        snake.pop()

    # --- ТАЙМЕР ЕДЫ ---
    if time.time() - food["time"] > FOOD_LIFETIME:
        food = generate_food()

    # --- ОТРИСОВКА ---
    screen.blit(background, (0, 0))

    # змейка (голова + тело)
    for i, segment in enumerate(snake):
        if i == 0:
            pygame.draw.rect(screen, DARK_RED, (segment[0], segment[1], CELL, CELL))
        else:
            pygame.draw.rect(screen, RED, (segment[0], segment[1], CELL, CELL))

    # еда
    pygame.draw.rect(screen, food["color"], (*food["pos"], CELL, CELL))

    # текст
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()