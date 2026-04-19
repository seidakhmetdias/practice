import pygame
import math

pygame.init()

# --- НАСТРОЙКИ ОКНА ---
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Paint")

clock = pygame.time.Clock()

# --- ЦВЕТА ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)

color = BLACK  # текущий цвет

# --- РЕЖИМЫ ---
mode = "brush"

# --- ПЕРЕМЕННЫЕ ---
drawing = False
start_pos = None

# фон
screen.fill(WHITE)

running = True
while running:

    # --- СОБЫТИЯ ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- НАЖАТИЕ МЫШИ ---
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # --- ОТПУСК МЫШИ ---
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            x1, y1 = start_pos
            x2, y2 = end_pos

            # --- ПРЯМОУГОЛЬНИК ---
            if mode == "rect":
                rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
                pygame.draw.rect(screen, color, rect, 2)

            # --- КРУГ ---
            elif mode == "circle":
                radius = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

            # --- КВАДРАТ ---
            elif mode == "square":
                side = max(abs(x2 - x1), abs(y2 - y1))
                rect = pygame.Rect(x1, y1, side, side)
                pygame.draw.rect(screen, color, rect, 2)

            # --- ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК ---
            elif mode == "triangle_right":
                points = [(x1, y1), (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, color, points, 2)

            # --- РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК ---
            elif mode == "triangle_eq":
                side = abs(x2 - x1)
                height = int(side * math.sqrt(3) / 2)

                points = [
                    (x1, y1),
                    (x1 + side, y1),
                    (x1 + side // 2, y1 - height)
                ]
                pygame.draw.polygon(screen, color, points, 2)

            # --- РОМБ ---
            elif mode == "rhombus":
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                points = [
                    (cx, y1),
                    (x2, cy),
                    (cx, y2),
                    (x1, cy)
                ]
                pygame.draw.polygon(screen, color, points, 2)

        # --- КЛАВИШИ ---
        if event.type == pygame.KEYDOWN:

            # --- РЕЖИМЫ (QWERTY) ---
            if event.key == pygame.K_q:
                mode = "brush"
            elif event.key == pygame.K_w:
                mode = "rect"
            elif event.key == pygame.K_e:
                mode = "circle"
            elif event.key == pygame.K_r:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "triangle_right"
            elif event.key == pygame.K_y:
                mode = "triangle_eq"
            elif event.key == pygame.K_u:
                mode = "rhombus"
            elif event.key == pygame.K_i:
                mode = "eraser"

            # --- ЦВЕТА ---
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

    # --- РИСОВАНИЕ КИСТЬЮ / ЛАСТИКОМ ---
    if drawing:
        mouse_pos = pygame.mouse.get_pos()

        # кисть
        if mode == "brush":
            pygame.draw.circle(screen, color, mouse_pos, 5)

        # ластик
        elif mode == "eraser":
            pygame.draw.circle(screen, WHITE, mouse_pos, 10)

    pygame.display.update()
    clock.tick(60)

pygame.quit()