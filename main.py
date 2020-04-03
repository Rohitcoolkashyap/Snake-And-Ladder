import random
import time

import pygame

# 1920,1080 made by Rohit Kashyap
# initialize pygame
pygame.init()
# window object
screen = pygame.display.set_mode((1920, 1080))
# game title
pygame.display.set_caption('Snake And Ladder')
# icon image
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# font object
font = pygame.font.SysFont('comicsans', 40)
# current mouse position
mouse_pos = (999, 999)
# global back_button
back_button = font.render("Back", 1, (255, 255, 0))
slide = 0
click_pos = pygame.mouse.get_pressed()

check = 0
r = 0
font1 = pygame.font.SysFont("comicsans", 50, True)
message = font1.render("Player Win", 1, (255, 255, 255))
message2 = font1.render("Computer Win", 1, (255, 255, 255))

messag3 = font1.render("Player Turn", 1, (255, 255, 255))

messag4 = font1.render("Computer Turn", 1, (255, 255, 255))

time1 = pygame.time.get_ticks()


# starting menu screen
class Menu:
    def __init__(self):
        self.bg_img = pygame.image.load('girl.jpg')
        self.text1 = font.render("Start", 1, (255, 255, 0))
        self.text2 = font.render("Exit", 1, (255, 255, 0))
        self.start = False
        self.pos = (999, 999)
        self.exit_button = True
        self.start_button = True

    def show_menu(self):
        screen.blit(self.bg_img, (300, 150))  # blit() used to draw
        self.show_buttons()

    def show_buttons(self):
        global check
        mouse1 = pygame.mouse.get_pos()  # get current mouse position

        if 450 + 150 >= mouse1[0] >= 450 and 450 + 50 >= mouse1[1] >= 450:  # for hover
            pygame.draw.rect(screen, (172, 115, 57), (450, 450, 150, 50))
        else:
            pygame.draw.rect(screen, (96, 64, 31), (450, 450, 150, 50))

        if 450 + 150 >= mouse1[0] >= 450 and 600 + 50 >= mouse1[1] >= 600:
            pygame.draw.rect(screen, (172, 115, 57), (450, 600, 150, 50))
        else:
            pygame.draw.rect(screen, (96, 64, 31), (450, 600, 150, 50))

        screen.blit(self.text1, (493, 460))  # display text on screen

        screen.blit(self.text2, (493, 610))

        if 450 + 150 >= mouse_pos[0] >= 450 and 450 + 50 >= mouse_pos[1] >= 450:
            check = 1
        if 450 + 150 >= mouse_pos[0] >= 450 and 600 + 50 >= mouse_pos[1] >= 600:
            pygame.quit()
            quit()


# snake ladder board
class Board:
    def __init__(self):
        self.board_img = pygame.image.load('board.jpg')
        self.dice_img = [pygame.image.load('dice1.png'),
                         pygame.image.load('dice2.png'),
                         pygame.image.load('dice3.png'),
                         pygame.image.load('dice4.png'),
                         pygame.image.load('dice5.png'),
                         pygame.image.load('dice6.png'), ]
        self.blue = pygame.image.load('bluegoti.png')
        self.red = pygame.image.load('red.png')
        self.start = False
        self.text5 = font.render("Player1", 1, (255, 255, 0))
        self.text6 = font.render("Computer", 1, (255, 255, 0))
        self.player1_dice = 0
        self.t2 = 1
        self.player_turn = False
        self.open = False
        self.count = 0
        self.now = False
        self.add = 145
        self.f1 = 325
        self.rule1 = 0
        self.c1 = 0
        self.c1 = 0
        self.ret = False
        self.start1 = False
        self.computer_dice = 0
        self.start2 = False
        self.dice_no = 0

        self.player1_active = True
        self.computer_active = True
        self.player2_active = False
        self.player3_active = False

        self.count1 = 0
        self.count2 = 0
        self.show2 = False
        self.finish1 = False
        self.finish2 = False

        self.show1 = False
        self.goti_pos = [[325, 820], [470, 820], [600, 820], [730, 820], [870, 820], [990, 820], [1126, 820],  # 6
                         [1250, 820], [1380, 820], [1516, 820], [1515, 745], [1390, 745], [1200, 745], [1100, 745],
                         [1000, 745], [870, 745], [730, 745], [600, 745], [480, 745], [340, 745], [340, 670],
                         [470, 670], [600, 670], [724, 670], [870, 670], [996, 670], [1126, 670], [1257, 670],
                         [1389, 670], [1502, 670], [1510, 600], [1389, 600], [1247, 600], [1114, 600], [987, 600],
                         [859, 600], [728, 600], [599, 600], [458, 600], [331, 600], [339, 535], [472, 535], [602, 535],
                         [728, 535], [860, 535], [992, 535], [1123, 535], [1252, 535], [1384, 535], [1505, 535],
                         [1511, 460], [1381, 460], [1241, 460], [1116, 460], [987, 460], [858, 460], [729, 460],
                         [593, 460], [466, 460], [334, 460], [337, 380], [470, 380], [597, 380], [729, 380], [859, 380],
                         [976, 380], [1112, 380], [1240, 380], [1370, 380], [1502, 380], [1512, 300], [1383, 300],
                         [1236, 300], [1116, 300], [981, 300], [854, 300], [731, 300], [599, 300], [475, 300],
                         [333, 300], [339, 240], [467, 240], [595, 240], [720, 240], [853, 240], [984, 240],
                         [1117, 240], [1246, 240], [1382, 240], [1508, 240], [1513, 160], [1374, 160], [1245, 160],
                         [1115, 160], [985, 160], [851, 160], [731, 160], [594, 160], [467, 160], [331, 160],
                         [1750, 500], [1750, 600]]
        self.red_pos = [self.goti_pos[0][0], self.goti_pos[0][0]]

    def display_board(self):
        screen.blit(self.board_img, (300, 150))
        self.show_buttons()

    def show_buttons(self):
        global check
        mouse2 = pygame.mouse.get_pos()  # get current mouse position
        screen.blit(self.dice_img[0], (1700, 300))

        if 1700 + 180 >= mouse2[0] >= 1700 and 800 + 50 >= mouse2[1] >= 800:  # player
            pygame.draw.rect(screen, (255, 0, 0), (1700, 800, 180, 50))
        else:
            pygame.draw.rect(screen, (204, 0, 0), (1700, 800, 180, 50))

        if 1700 + 180 >= mouse2[0] >= 1700 and 900 + 50 >= mouse2[1] >= 900:  # computer
            pygame.draw.rect(screen, (26, 26, 255), (1700, 900, 180, 50))
        else:
            pygame.draw.rect(screen, (0, 0, 153), (1700, 900, 180, 50))

        screen.blit(self.text5, (1725, 810))

        screen.blit(self.text6, (1725, 910))

        if self.start2:
            screen.blit(self.blue, (self.goti_pos[self.count2]))
        else:
            screen.blit(self.blue, (1750, 500))
        if self.start1:
            screen.blit(self.red, (self.goti_pos[self.count1]))
        else:
            screen.blit(self.red, (1750, 600))

        self.main_game()

    def check1(self):
        self.dice_no = random.randint(0, 5)
        if self.dice_no == 5:
            self.start1 = True
            self.player_turn = False

    def check2(self):
        self.player1_dice = random.randint(0, 5)
        if self.player1_dice == 5:
            self.start2 = True
            self.player_turn = False

    def dice(self):
        self.player1_dice = random.randint(0, 5)

    def dice2(self):
        self.computer_dice = random.randint(0, 5)

    def ladder(self):
        if self.count2 == 4:
            self.count2 = 57
        if self.count2 == 13:
            self.count2 = 48
        if self.count2 == 52:
            self.count2 = 71
        if self.count2 == 63:
            self.count2 = 82

        if self.count1 == 4:
            self.count1 = 57
        if self.count1 == 13:
            self.count1 = 48
        if self.count1 == 52:
            self.count1 = 71
        if self.count1 == 63:
            self.count1 = 82

    def snake(self):
        if self.count2 == 37:
            self.count2 = 19
        if self.count2 == 50:
            self.count2 = 9
        if self.count2 == 75:
            self.count2 = 53
        if self.count2 == 96:
            self.count2 = 60

        if self.count2 == 90:
            self.count2 = 72

        if self.count1 == 37:
            self.count1 = 19
        if self.count1 == 50:
            self.count1 = 9
        if self.count1 == 75:
            self.count1 = 53
        if self.count1 == 96:
            self.count1 = 60

        if self.count1 == 90:
            self.count1 = 72

    def main_game(self):

        if not self.start1 or not self.start2:
            if self.player_turn:
                if not self.start2:
                    print('player turn')
                    self.check2()
                if not self.start1:
                    print('computer turn')
                    self.check1()

        if self.player_turn:

            if self.start2:
                print('player turn')

                self.dice()
                self.count2 += self.player1_dice + 1
                self.ladder()
                self.snake()

                if self.count2 < 100:

                    if self.count2 == 99:
                        self.start2 = False
                        self.finish2 = True
                        print('Player win')

                        for i in range(3):
                            screen.blit(message, (500, 100))

                            time.sleep(2)
                            pygame.display.update()

                        pygame.quit()
                        quit()
                else:
                    self.count2 -= self.player1_dice + 1

        if self.start1:
            if self.player_turn:

                print('computer turn')

                self.dice2()
                self.count1 += self.computer_dice + 1
                self.ladder()
                self.snake()
                if self.count1 < 100:

                    if self.count1 == 99:
                        self.start1 = False
                        self.finish1 = True
                        print('Computer Win ')

                        for i in range(3):
                            screen.blit(message2, (500, 100))

                            time.sleep(2)
                            pygame.display.update()
                        pygame.quit()
                        quit()
                else:
                    self.count1 -= self.computer_dice + 1

        screen.blit(self.dice_img[self.player1_dice], (1700, 300))
        self.player_turn = False


# select player mode
class Player:
    def __init__(self):
        self.text3 = font.render("Single Player", 1, (255, 255, 0))
        self.text4 = font.render("2 - Player", 1, (255, 255, 0))
        self.text5 = font.render("Back", 1, (255, 255, 0))

        self.bg_img = pygame.image.load('girl.jpg')

    def select_player(self):

        screen.blit(self.bg_img, (300, 150))
        self.show_buttons()

    def show_buttons(self):
        global check, click_pos
        mouse3 = pygame.mouse.get_pos()

        if 450 + 240 >= mouse3[0] >= 445 and 450 + 50 >= mouse3[1] >= 450:  # for hover
            pygame.draw.rect(screen, (172, 115, 57), (450, 450, 240, 50))
            click_pos = pygame.mouse.get_pressed()
        else:
            pygame.draw.rect(screen, (96, 64, 31), (450, 450, 240, 50))

        if 450 + 240 >= mouse3[0] >= 450 and 600 + 50 >= mouse3[1] >= 600:
            pygame.draw.rect(screen, (172, 115, 57), (450, 600, 240, 50))
        else:
            pygame.draw.rect(screen, (96, 64, 31), (450, 600, 240, 50))

        if click_pos[0]:
            if 450 + 240 >= mouse_pos[0] >= 450 and 450 + 50 >= mouse_pos[1] >= 450:
                check = 2

        screen.blit(self.text3, (480, 460))
        screen.blit(self.text4, (493, 610))
        screen.blit(self.text5, (57, 29))


def back():
    global check
    mouse = pygame.mouse.get_pos()
    if 20 + 150 >= mouse[0] >= 20 and 20 + 50 >= mouse[1] >= 20:
        pygame.draw.rect(screen, (172, 115, 57), (20, 20, 150, 50))

    else:
        pygame.draw.rect(screen, (96, 64, 31), (20, 20, 150, 50))

    if 20 + 150 >= mouse_pos[0] >= 20 and 20 + 50 >= mouse_pos[1] >= 20:
        check = 0
    screen.blit(back_button, (57, 29))


def redrawGameWindow():
    # these conditions used to know which screen is to be displayed
    global t, slide, check

    if check == 1:
        win3.select_player()

    elif check == 2:
        win2.display_board()
    else:
        win1.show_menu()

    back()
    pygame.display.update()  # update game window


# objects
win1 = Menu()
win2 = Board()
win3 = Player()
running = True
while running:
    screen.fill((163, 163, 117))  # background color
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            win2.player_turn = True

    redrawGameWindow()
pygame.quit()
