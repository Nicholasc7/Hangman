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





    def draw_stand(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        pygame.draw.line(screen, BLACK, (WIDTH - 200 ,HEIGHT/2), (WIDTH - 200 + SLANT, HEIGHT/2 - SLANT), 7)
        pygame.draw.line(screen, BLACK, ((WIDTH - 200) + (SLANT*2),HEIGHT/2), ((WIDTH - 200) + (SLANT*2) - SLANT, HEIGHT/2 - SLANT), 7)
        pygame.draw.line(screen, BLACK, ((WIDTH - 200) + (SLANT*2) - SLANT, HEIGHT/2 - SLANT),    ((WIDTH - 200) + (SLANT*2) - SLANT, HEIGHT/2 - 250), 5)
        pygame.draw.line(screen, BLACK, ((WIDTH - 200) + (SLANT*2) - SLANT, HEIGHT/2 - 250),  ((WIDTH - 275) + (SLANT*2) - SLANT, HEIGHT/2 - 250), 4)
        pygame.draw.line(screen, BLACK, ((WIDTH - 275) + (SLANT*2) - SLANT, HEIGHT/2 - 250),  ((WIDTH - 275) + (SLANT*2) - SLANT, HEIGHT/2 - 230), 2)

    def draw_head(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        pygame.draw.circle(screen, BLACK, ((WIDTH - 274) + (SLANT*2) - SLANT, HEIGHT/2 - 210), 20, 2)

    def draw_torso(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        pygame.draw.line(screen, BLACK, (WIDTH - 224, HEIGHT/2 - 190), (WIDTH - 224, HEIGHT/2 - 130), 2)

    def draw_leftarm(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        pygame.draw.line(screen, BLACK, (WIDTH - 224, HEIGHT/2 - 180), (WIDTH - 249, HEIGHT/2 - 155), 2)

    def draw_rightarm(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        pygame.draw.line(screen, BLACK, (WIDTH - 224, HEIGHT/2 - 180), (WIDTH - 199, HEIGHT/2 - 155), 2)

    def draw_leftleg(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        pygame.draw.line(screen, BLACK, (WIDTH - 224, HEIGHT/2 - 130), (WIDTH - 249, HEIGHT/2 - 105), 2)

    def draw_rightleg(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        pygame.draw.line(screen, BLACK, (WIDTH - 224, HEIGHT/2 - 130), (WIDTH - 199, HEIGHT/2 - 105), 2)

    def draw_lefteye(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        EYE_LEN = 6
        pygame.draw.circle(screen, BLACK, ((WIDTH - 274) + (SLANT*2) - SLANT - EYE_LEN -1, HEIGHT/2 - 210 - EYE_LEN), EYE_LEN, 2)

    def draw_righteye(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        EYE_LEN = 6
        pygame.draw.circle(screen, BLACK, ((WIDTH - 274) + (SLANT*2) - SLANT + EYE_LEN + 1, HEIGHT/2 - 210 - EYE_LEN), EYE_LEN, 2)

    def draw_mouth(self, screen):
        BLACK = (0,0,0)
        HEIGHT = 800
        WIDTH = 800
        SLANT = 50
        EYE_LEN = 6
        pygame.draw.circle(screen, BLACK, ((WIDTH - 274) + (SLANT*2) - SLANT, HEIGHT/2 - 203), 4, 2)
