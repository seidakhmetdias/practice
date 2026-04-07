import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)

# ВАЖНО: твоя папка называется "musik"
player = MusicPlayer("musik")

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.prev_track()

            elif event.key == pygame.K_q:
                running = False

    # отображение текста
    track_text = font.render(f"Track: {player.get_current_track()}", True, (255, 255, 255))
    controls_text = font.render("P-Play S-Stop N-Next B-Back Q-Quit", True, (200, 200, 200))

    screen.blit(track_text, (50, 150))
    screen.blit(controls_text, (50, 200))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
