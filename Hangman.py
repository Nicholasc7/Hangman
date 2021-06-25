import pygame
import random, time
from Man import Man
import sys
from pygame.locals import *

pygame.init()
pygame.font.init()


WIDTH, HEIGHT = 800, 800
WHITE = (255, 234, 210)
BLACK = (15, 14, 27)
BOX_PADDING = 10
WBOX_PADDING = 25
LETTER_BOX_PAD = 12
LETTER_BOX_SPACING = 65
LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT = 50, 50
SQUARE_UI_PAD = 75
INNER_SQUARE_PAD = 8


wordbank = [
["OCTOPUS", "BIRD", "WOLF", "PANDA", "LION", "TIGER", "DOG", "LIZARD", "EAGLE", "ZEBRA"],
["BURGER", "PANCAKE", "WAFFLE", "EGGS", "STEAK", "PIZZA", "BACON", "CHICKEN", "NOODLES"],
["AMERICA", "SPAIN", "FRANCE", "AFRICA", "NORWAY", "IRAN", "CHINA", "JAPAN"]
]


welcome_font = pygame.font.SysFont("", 50)
welcome_text = welcome_font.render("Welcome to Hangman!", True, WHITE)
welcome_box = pygame.Rect((WIDTH/2 - welcome_text.get_width()/2) - WBOX_PADDING, 50 - WBOX_PADDING, welcome_text.get_width() + WBOX_PADDING*2, welcome_text.get_height() + WBOX_PADDING*2)

category_fonts = pygame.font.SysFont("Ariel", 50)
category_text1 = category_fonts.render("Animals", True, BLACK)
category_text2 = category_fonts.render("Food", True, BLACK)
category_text3 = category_fonts.render("Geography", True, BLACK)
category_box1 = pygame.Rect((WIDTH/2 - category_text1.get_width()/2) - BOX_PADDING, 200 - BOX_PADDING, category_text1.get_width() + BOX_PADDING * 2, category_text1.get_height() + BOX_PADDING*2)
category_box2 = pygame.Rect((WIDTH/2 - category_text2.get_width()/2) - BOX_PADDING, 300 - BOX_PADDING, category_text2.get_width() + BOX_PADDING * 2, category_text2.get_height() + BOX_PADDING*2)
category_box3 = pygame.Rect((WIDTH/2 - category_text3.get_width()/2) - BOX_PADDING, 400 - BOX_PADDING, category_text3.get_width() + BOX_PADDING * 2, category_text3.get_height() + BOX_PADDING*2)

square_ui = pygame.Rect((WIDTH/2 - category_text3.get_width()/2) - SQUARE_UI_PAD, 200 - SQUARE_UI_PAD, (SQUARE_UI_PAD*2 + category_text3.get_width()), 300 + category_text3.get_height() + SQUARE_UI_PAD)
square_ui_inner = pygame.Rect((WIDTH/2 - category_text3.get_width()/2 + INNER_SQUARE_PAD) - SQUARE_UI_PAD, 200 - SQUARE_UI_PAD + INNER_SQUARE_PAD,\
 (SQUARE_UI_PAD*2 + category_text3.get_width() - INNER_SQUARE_PAD*2), 300 + category_text3.get_height() + SQUARE_UI_PAD - INNER_SQUARE_PAD*2)


# Create letters
letters = []
letter_font = pygame.font.SysFont("Ariel", 50)
letterbank = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(26):
    letter_text = letter_font.render(letterbank[i], True, WHITE)
    letters.append(letter_text)


# Create letter boxes
letter_box_index = []
letter_x, letter_y = 100, HEIGHT/2 + 100
# 1st row of boxes
for i in range(10):
    letter_box = pygame.Rect(letter_x - LETTER_BOX_PAD, letter_y - LETTER_BOX_PAD + 2, LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT)
    letter_x += LETTER_BOX_SPACING
    letter_box_index.append(letter_box)
letter_x = 100
letter_y += 100
# 2nd row of boxes
for i in range(10,20):
    letter_box = pygame.Rect(letter_x - LETTER_BOX_PAD, letter_y - LETTER_BOX_PAD + 2, LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT)
    letter_x += LETTER_BOX_SPACING
    letter_box_index.append(letter_box)
letter_x = 200
letter_y += 100
# 3rd row of boxes
for i in range(20,26):
    letter_box = pygame.Rect(letter_x - LETTER_BOX_PAD, letter_y - LETTER_BOX_PAD + 2, LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT)
    letter_x += LETTER_BOX_SPACING
    letter_box_index.append(letter_box)


# TODO: Create body part objects
#man = Man(head, torso, left_arm, right_arm, left_leg, right_leg, face)


def get_guess_word(wordbank, category):
    if category == 1:
        word = random.choice(wordbank[0])
        print(word)
        return word
    if category == 2:
        word = random.choice(wordbank[1])
        print(word)
        return word
    if category == 3:
        word = random.choice(wordbank[2])
        print(word)
        return word


def draw_dashes(guessword, screen):
    word_len = len(guessword)
    dash_x = 90
    dash_len = 50
    dash_spacing = 15
    for i in range(word_len):
        dash = pygame.Rect(dash_x, HEIGHT/2, dash_len, 5)
        pygame.draw.rect(screen, BLACK, dash)
        dash_x += dash_spacing + dash_len
    return True


def get_button_input(letters, letter_box_index, mouse_click, dashes_drawn):
    mouse_pos = pygame.mouse.get_pos()
    letter_x, letter_y = 100, HEIGHT/2 + 100
    if dashes_drawn:
        for i in range(10):
            if (mouse_pos[0] > letter_x - LETTER_BOX_PAD and mouse_pos[0] < letter_x - LETTER_BOX_PAD + LETTER_BOX_WIDTH) and (mouse_pos[1] > letter_y - LETTER_BOX_PAD and\
             mouse_pos[1] < letter_y - LETTER_BOX_PAD + LETTER_BOX_HEIGHT) and mouse_click == True:
                return letterbank[i]
            letter_x += LETTER_BOX_SPACING
        letter_y += 100
        letter_x = 100
        for i in range(10,20):
            if (mouse_pos[0] > letter_x - LETTER_BOX_PAD and mouse_pos[0] < letter_x - LETTER_BOX_PAD + LETTER_BOX_WIDTH) and (mouse_pos[1] > letter_y - LETTER_BOX_PAD and\
             mouse_pos[1] < letter_y - LETTER_BOX_PAD + LETTER_BOX_HEIGHT) and mouse_click == True:
                return letterbank[i]
            letter_x += LETTER_BOX_SPACING
        letter_y += 100
        letter_x = 200
        for i in range(20,26):
            if (mouse_pos[0] > letter_x - LETTER_BOX_PAD and mouse_pos[0] < letter_x - LETTER_BOX_PAD + LETTER_BOX_WIDTH) and (mouse_pos[1] > letter_y - LETTER_BOX_PAD and\
             mouse_pos[1] < letter_y - LETTER_BOX_PAD + LETTER_BOX_HEIGHT) and mouse_click == True:
                return letterbank[i]
            letter_x += LETTER_BOX_SPACING


def game_win(letters, letter_box_index, screen):
    letter_x, letter_y = 100, HEIGHT/2 + 100
    screen.fill((WHITE))

    # Draw letters and letter boxes
    for i in range(26):
        pygame.draw.rect(screen, BLACK, letter_box_index[i], 25, 15)

        # Align letter 'i'
        if i == 8:
            screen.blit(letters[i], (letter_x + 8, letter_y))
        else:
            screen.blit(letters[i], (letter_x, letter_y))

        letter_x += LETTER_BOX_SPACING
        if i == 9:
            letter_x = 100
            letter_y += 100
        if i == 19:
            letter_x = 200
            letter_y += 100


def menu(Man):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((WHITE))
    pygame.draw.rect(screen, BLACK, square_ui_inner,0,20)

    # Draw welcome box
    pygame.draw.rect(screen, BLACK, welcome_box, 0, 15)
    screen.blit(welcome_text, (WIDTH/2 - welcome_text.get_width()/2, 50))

    # Draw square ui
    pygame.draw.rect(screen, BLACK, square_ui, 3, 25)

    # Draw categories
    pygame.draw.rect(screen, WHITE, category_box1, 0, 20)
    screen.blit(category_text1, (WIDTH/2 - category_text1.get_width()/2, 200))
    pygame.draw.rect(screen, WHITE, category_box2, 0, 20)
    screen.blit(category_text2, (WIDTH/2 - category_text2.get_width()/2, 300))
    pygame.draw.rect(screen, WHITE, category_box3, 0, 20)
    screen.blit(category_text3, (WIDTH/2 - category_text3.get_width()/2, 400))

    # Draw hangman
    man = Man()
    man.draw_hangman_menu(screen)


    pygame.display.update()


def menu_box_click(text1, text2, text3, mouse_click):
    mouse_pos = pygame.mouse.get_pos()
    if (mouse_pos[0] > (WIDTH/2 - text1.get_width()/2 - BOX_PADDING) and mouse_pos[0] < (WIDTH/2 + text1.get_width()/2 + BOX_PADDING)) and\
    (mouse_pos[1] > 200 - BOX_PADDING and mouse_pos[1] < 200 + category_text1.get_height() + BOX_PADDING) and mouse_click == True:
        return 1
    if (mouse_pos[0] > (WIDTH/2 - text2.get_width()/2 - BOX_PADDING) and mouse_pos[0] < (WIDTH/2 + text2.get_width()/2 + BOX_PADDING)) and\
    (mouse_pos[1] > 300 - BOX_PADDING and mouse_pos[1] < 300 + category_text2.get_height() + BOX_PADDING) and mouse_click == True:
        return 2
    if (mouse_pos[0] > (WIDTH/2 - text3.get_width()/2 - BOX_PADDING) and mouse_pos[0] < (WIDTH/2 + text3.get_width()/2 + BOX_PADDING)) and\
    (mouse_pos[1] > 400 - BOX_PADDING and mouse_pos[1] < 400 + category_text3.get_height() + BOX_PADDING) and mouse_click == True:
        return 3


def is_letter_correct(letter_selected, word_dict, to_be_drawn, correct_guesses, wrong_guesses):
    guess_word = ""
    guess_word_index = []
    for letter in (range(len(word_dict))):
        guess_word = guess_word + word_dict[letter]
    for key in word_dict:
        guess_word_index.append(key)

    for letter in word_dict:
        if letter_selected == word_dict[letter]:
            if not correct_guesses.count(letter_selected) == guess_word.count(letter_selected):
                correct_guesses.append(letter)
                correct_guesses.append(word_dict[letter])
                del letter
                continue
        if letter_selected not in wrong_guesses and letter_selected not in guess_word:
            wrong_guesses.append(letter_selected)


def draw_correct_guesses(to_be_drawn, screen):
    letter_font = pygame.font.SysFont("Ariel", 70)
    HEIGHT = 800
    dash_x = 90
    dash_len = 50
    dash_spacing = 15
    space = dash_len + dash_spacing
    for index,i in enumerate(to_be_drawn):
        if isinstance(i, str):
            letter = letter_font.render(i, True, BLACK)
            screen.blit(letter, ((dash_x + dash_len/6) + space * to_be_drawn[index - 1], HEIGHT/2 - 40))



game_over = False
category = 0

# Log of letters that the user has selected
wrong_guesses = []

# Log of correct guesses
correct_guesses = []

# Guess word organized into a dictionary
word_dict = {}

# Letters and their index stored in here when guessed correctly
to_be_drawn = []

game_start = False

letter_selected = ""
while not game_over:

    dashes_drawn = False
    for event in pygame.event.get():
        mouse_click = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True
        if event.type == pygame.QUIT:
            sys.exit()


    # Waits at menu screen for user to pick a category
    if not category:
        menu(Man)
        category = menu_box_click(category_text1, category_text2, category_text3, mouse_click)
        guessword = get_guess_word(wordbank, category)


    # Adds the guess word to a dictionary ONE TIME because game start is false and a category is chosen. Then makes game_start True so the game win starts and this action isn't executed again.
    if not game_start and category:
        for index,letter in enumerate(guessword):
            word_dict[index] = letter
        game_start = True
        time.sleep(.1)


    # Game window start
    if game_start:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        game_win(letters, letter_box_index, screen)

        # Draw dashes to the screen
        dashes_drawn = draw_dashes(guessword, screen)

        # Returns the letter clicked and stores letter in 'letter_selected' variable
        letter_selected = get_button_input(letters, letter_box_index, mouse_click, dashes_drawn)

        # When there's 1 or more element in 'correct_guesses' list, start drawing said letters
        if correct_guesses:
            draw_correct_guesses(correct_guesses, screen)

        # If the user clicks on a letter
        if isinstance(letter_selected, str):

            # Checks if the letter is correct, if correct adds said letters to 'to_be_drawn' list and correct_guesses list, else added to wrong_guesses
            is_letter_correct(letter_selected, word_dict, to_be_drawn, correct_guesses, wrong_guesses)
            print(f"Correct guesses: {correct_guesses}")
            print(f"Wrong guesses: {wrong_guesses}")
            print(f"Guess word len: {len(guessword)}")
            print(word_dict)



        pygame.display.update()
