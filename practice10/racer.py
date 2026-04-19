import pygame
import random

pygame.init()

# --- НАСТРОЙКИ ---
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Final Full")

clock = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)

# --- ФОН ---
background = pygame.image.load("road.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
bg_y = 0

# --- МАШИНА ИГРОКА ---
player_img = pygame.image.load("car.png").convert_alpha()

# масштаб с сохранением пропорций
w, h = player_img.get_size()
scale = 80 / h
player_img = pygame.transform.scale(player_img, (int(w * scale), int(h * scale)))

player_x = WIDTH // 2 - player_img.get_width() // 2
player_y = HEIGHT - 120
player_speed = 5

# --- ВРАГ ---
enemy_img = pygame.image.load("enemy.png").convert_alpha()

w, h = enemy_img.get_size()
scale = 80 / h
enemy_img = pygame.transform.scale(enemy_img, (int(w * scale), int(h * scale)))

enemy_x = random.randint(0, WIDTH - enemy_img.get_width())
enemy_y = -100
enemy_speed = 5

# --- МОНЕТЫ ---
coins = []
coin_timer = 0

# --- СЧЁТ ---
score = 0
font = pygame.font.SysFont(None, 30)

# --- УСКОРЕНИЕ ---
N = 5  # каждые 5 очков

running = True
while running:

    # --- СОБЫТИЯ ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- УПРАВЛЕНИЕ ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_img.get_width():
        player_x += player_speed

    # --- ДВИЖЕНИЕ ФОНА ---
    bg_y += 5
    if bg_y >= HEIGHT:
        bg_y = 0

    screen.blit(background, (0, bg_y))
    screen.blit(background, (0, bg_y - HEIGHT))

    # --- ДВИЖЕНИЕ ВРАГА ---
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - enemy_img.get_width())

    # --- СПАВН МОНЕТ ---
    coin_timer += 1
    if coin_timer > 60:
        x = random.randint(0, WIDTH - 30)
        y = -30

        weight = random.choice([1, 2, 5])

        if weight == 1:
            color = (200, 200, 0)
        elif weight == 2:
            color = (255, 165, 0)
        else:
            color = (255, 215, 0)

        coins.append([x, y, weight, color])
        coin_timer = 0

    # --- ДВИЖЕНИЕ МОНЕТ ---
    for coin in coins:
        coin[1] += 4

    coins = [coin for coin in coins if coin[1] < HEIGHT]

    # --- COLLISION ---
    player_rect = pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height())
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_img.get_width(), enemy_img.get_height())

    for coin in coins[:]:
        coin_rect = pygame.Rect(coin[0], coin[1], 30, 30)
        if player_rect.colliderect(coin_rect):
            score += coin[2]
            coins.remove(coin)

            # ускорение врага
            if score % N == 0:
                enemy_speed += 1

    if player_rect.colliderect(enemy_rect):
        print("GAME OVER")
        running = False

    # --- ОТРИСОВКА ---
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))

    for coin in coins:
        pygame.draw.circle(screen, coin[3], (coin[0] + 15, coin[1] + 15), 15)

    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()