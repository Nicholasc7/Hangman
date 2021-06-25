import pygame

class Man:
    def __init__(self):
        pass

    def draw_hangman_menu(self, screen):
        bottom_line1 = pygame.draw.line(screen, (0,0,0), (40,780), (80,720), 4)
        bottom_line2 = pygame.draw.line(screen, (0,0,0), (80, 720), (120, 780), 4)
        vertical_line = pygame.draw.line(screen, (0,0,0), (80,720), (80, 600), 4)
        horizontal_line = pygame.draw.line(screen, (0,0,0), (80,600), (130, 600), 3)
        vertical_line_short = pygame.draw.line(screen, (0,0,0), (130,600), (130, 620), 2)

        head = pygame.draw.circle(screen, (0,0,0), (130, 635), 15, 2)
        torso = pygame.draw.line(screen, (0,0,0), (130, 650), (130, 690), 2)
        left_arm = pygame.draw.line(screen, (0,0,0), (130, 665-8), (115, 685-8), 2)
        right_arm = pygame.draw.line(screen, (0,0,0), (130, 665-8), (145, 685-8), 2)
        left_leg = pygame.draw.line(screen, (0,0,0), (130, 690), (115, 690+28), 2)
        right_leg = pygame.draw.line(screen, (0,0,0), (130, 690), (145, 690+28), 2)

        #left_eye1 = pygame.draw.line(screen, (0,0,0), (125,630), (120, 635),2)
        #left_eye2 = pygame.draw.line(screen, (0,0,0), (135,640), (130, 635),2)

    def draw_head(self, screen):
        head = pygame.Rect(250, 250, 50, 50)
        pygame.draw.rect(screen, (255, 0, 0), head)
