import pygame
from clock import MickeyClock

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# --- ЗАГРУЗКА ИЗОБРАЖЕНИЙ ---

bg = pygame.image.load("images/clock_bg.png").convert_alpha()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

left_hand = pygame.image.load("images/left_hand.png").convert_alpha()
right_hand = pygame.image.load("images/right_hand.png").convert_alpha()

# (если нужно — можно поменять размер)
# left_hand = pygame.transform.scale(left_hand, (300, 20))
# right_hand = pygame.transform.scale(right_hand, (300, 20))

center = (WIDTH // 2, HEIGHT // 2)

mickey_clock = MickeyClock(center, left_hand, right_hand)

# --- ОСНОВНОЙ ЦИКЛ ---

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # фон
    screen.blit(bg, (0, 0))

    # стрелки
    mickey_clock.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()