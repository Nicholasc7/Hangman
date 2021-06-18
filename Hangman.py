import pygame
import random
from Man import Man
import sys
from pygame.locals import *

pygame.init()
pygame.font.init()


WIDTH, HEIGHT = 800, 800
WHITE = (255, 234, 210)
BLACK = (15, 14, 27)
BOX_PADDING = 15
LETTER_BOX_PAD = 12

wordbank = [
["octopus", "bird", "wolf", "panda", "lion", "tiger", "dog", "lizard", "eagle", "zebra"],
["burger", "pancake", "waffle", "eggs", "steak", "pizza", "bacon", "chicken", "noodles"],
["America", "Spain", "France", "Africa", "Norway", "Iran", "China", "Japan"]
]


welcome_font = pygame.font.SysFont("Muna Black", 75)
welcome_text = welcome_font.render("Welcome to Hangman!", True, WHITE)
welcome_box = pygame.Rect((WIDTH/2 - welcome_text.get_width()/2) - BOX_PADDING, (HEIGHT/9) - BOX_PADDING, welcome_text.get_width() + BOX_PADDING*2, welcome_text.get_height() + BOX_PADDING*2)

category_fonts = pygame.font.SysFont("Ariel", 50)
category_text1 = category_fonts.render("Animals", True, WHITE)
category_text2 = category_fonts.render("Food", True, WHITE)
category_text3 = category_fonts.render("Geography", True, WHITE)
category_box1 = pygame.Rect((WIDTH/2 - category_text1.get_width()/2) - BOX_PADDING, HEIGHT/5*2 - BOX_PADDING, category_text1.get_width() + BOX_PADDING * 2, category_text1.get_height() + BOX_PADDING*2)
category_box2 = pygame.Rect((WIDTH/2 - category_text2.get_width()/2) - BOX_PADDING, HEIGHT/5*3 - BOX_PADDING, category_text2.get_width() + BOX_PADDING * 2, category_text2.get_height() + BOX_PADDING*2)
category_box3 = pygame.Rect((WIDTH/2 - category_text3.get_width()/2) - BOX_PADDING, HEIGHT/5*4 - BOX_PADDING, category_text3.get_width() + BOX_PADDING * 2, category_text3.get_height() + BOX_PADDING*2)


# TODO: Create body part objects
#man = Man(head, torso, left_arm, right_arm, left_leg, right_leg, face)


def game_win(letters):
    letter_x, letter_y = 100, HEIGHT/2 + 100
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((WHITE))

    # 1st row of letters
    for i in range(10):
        letter_box = pygame.Rect(letter_x - LETTER_BOX_PAD, letter_y - LETTER_BOX_PAD + 2, 50, 50)
        pygame.draw.rect(screen, BLACK, letter_box, 25, 15)
        screen.blit(letters[i], (letter_x, letter_y))
        letter_x += 65
    letter_x = 100
    letter_y += 100
    # 2nd row of letters
    for i in range(10,20):
        letter_box = pygame.Rect(letter_x - LETTER_BOX_PAD, letter_y - LETTER_BOX_PAD + 2, 50, 50)
        pygame.draw.rect(screen, BLACK, letter_box, 25, 15)
        screen.blit(letters[i], (letter_x, letter_y))
        letter_x += 65
    letter_x = 200
    letter_y += 100
    # 3rd row of letters
    for i in range(20,26):
        letter_box = pygame.Rect(letter_x - LETTER_BOX_PAD, letter_y - LETTER_BOX_PAD + 2, 50, 50)
        pygame.draw.rect(screen, BLACK, letter_box, 25, 15)
        screen.blit(letters[i], (letter_x, letter_y))
        letter_x += 65


def menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((WHITE))

    pygame.draw.rect(screen, BLACK, welcome_box)
    screen.blit(welcome_text, (WIDTH/2 - welcome_text.get_width()/2, HEIGHT/9))

    pygame.draw.rect(screen, BLACK, category_box1, 32, 20)
    screen.blit(category_text1, (WIDTH/2 - category_text1.get_width()/2, HEIGHT/5*2))
    pygame.draw.rect(screen, BLACK, category_box2, 32, 20)
    screen.blit(category_text2, (WIDTH/2 - category_text2.get_width()/2, HEIGHT/5*3))
    pygame.draw.rect(screen, BLACK, category_box3, 33, 20)
    screen.blit(category_text3, (WIDTH/2 - category_text3.get_width()/2, HEIGHT/5*4))


def menu_box_click(text1, text2, text3, mouse_click):
    mouse_pos = pygame.mouse.get_pos()
    if (mouse_pos[0] > (WIDTH/2 - text1.get_width()/2 - BOX_PADDING) and mouse_pos[0] < (WIDTH/2 + text1.get_width()/2 + BOX_PADDING)) and\
    (mouse_pos[1] > HEIGHT/5*2 - BOX_PADDING and mouse_pos[1] < HEIGHT/5*2 + category_text1.get_height() + BOX_PADDING) and mouse_click == True:
        return 1
    if (mouse_pos[0] > (WIDTH/2 - text2.get_width()/2 - BOX_PADDING) and mouse_pos[0] < (WIDTH/2 + text2.get_width()/2 + BOX_PADDING)) and\
    (mouse_pos[1] > HEIGHT/5*3 - BOX_PADDING and mouse_pos[1] < HEIGHT/5*3 + category_text2.get_height() + BOX_PADDING) and mouse_click == True:
        return 2
    if (mouse_pos[0] > (WIDTH/2 - text3.get_width()/2 - BOX_PADDING) and mouse_pos[0] < (WIDTH/2 + text3.get_width()/2 + BOX_PADDING)) and\
    (mouse_pos[1] > HEIGHT/5*4 - BOX_PADDING and mouse_pos[1] < HEIGHT/5*4 + category_text3.get_height() + BOX_PADDING) and mouse_click == True:
        return 3



def create_guess_word(wordbank):
    pass


def is_corect_letter(guessword, userguess):
    pass


def hidden_word(guessword):
    pass


def display_man(man):
    pass


letters = []
letter_font = pygame.font.SysFont("Ariel", 50)
letterbank = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(26):
    letter_text = letter_font.render(letterbank[i], True, WHITE)
    letters.append(letter_text)


game_over = False
category = 0
while not game_over:

    for event in pygame.event.get():
        mouse_click = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True
        if event.type == pygame.QUIT:
            sys.exit()

    if not category:
        menu()
        category = menu_box_click(category_text1, category_text2, category_text3, mouse_click)
    else:
        game_win(letters)
    pygame.display.update()
