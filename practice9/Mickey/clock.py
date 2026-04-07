import pygame
import datetime

class MickeyClock:
    def __init__(self, center, left_hand_img, right_hand_img):
        self.center = center
        self.left_hand = left_hand_img   # секунды
        self.right_hand = right_hand_img # минуты

    def get_time_angles(self):
        now = datetime.datetime.now()

        seconds = now.second
        minutes = now.minute

        # углы (по часовой стрелке)
        seconds_angle = -seconds * 6
        minutes_angle = -(minutes + seconds / 60) * 6  # плавное движение

        return seconds_angle, minutes_angle

    def draw(self, screen):
        sec_angle, min_angle = self.get_time_angles()

        # вращение
        sec_rotated = pygame.transform.rotate(self.left_hand, sec_angle)
        min_rotated = pygame.transform.rotate(self.right_hand, min_angle)

        # центрирование
        sec_rect = sec_rotated.get_rect(center=self.center)
        min_rect = min_rotated.get_rect(center=self.center)

        # рисуем
        screen.blit(sec_rotated, sec_rect)
        screen.blit(min_rotated, min_rect)