import pygame,sys
from pygame.locals import *
from items_classes import *
from player_classes import *

#Colours    R...G...B
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)


pygame.init()
DISPLAYWIDTH = 1024
DISPLAYHEIGHT = 683
DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
FPS = 30
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Lost in the Forest!")

inventoryFont = pygame.font.Font(None, 32)
selectFont = pygame.font.Font(None, 32)
selectFont.set_underline(True)
charImgs = ('characters/guy0.png','characters/guy1.png','characters/guy2.png')
coinImg = 'items/coin0.png' 
mapImg = 'items/map.png'
coinSound = 'sounds/coin.wav'
player = Player(700,500,charImgs)#starting(x,y)coords
all_sprites = pygame.sprite.Group()


levelitems = pygame.sprite.Group()
coin = Item('c1',500,600,{'coin':1},coinImg,coinSound)
coin2 = Item('c2',220,530,{'coin':1},coinImg,coinSound)
mapitem = Item('themap',900,500,{'map':1},mapImg,coinSound)
levelitems.add(coin, coin2, mapitem)
levelwalls = pygame.sprite.Group()
wall = Wall('w1',0,450,1000,10)
wall1 = Wall('w2',0,683,1000,10)
wall3 = Wall('w3',1020,450,5,300)
levelwalls.add(wall, wall1, wall3)

all_sprites.add(levelwalls,levelitems)


def level():
    moveX,moveY=0,0
    player.set_location(level)
    background = pygame.image.load("backgrounds/forest.jpg").convert()
    while True:#Game Loop
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    moveX = -5
                if event.key==pygame.K_d:
                    moveX = 5
                if event.key==pygame.K_w:
                    moveY = -5
                if event.key==pygame.K_s:
                    moveY = 5
                if event.key==pygame.K_e:
                    moveX = 0
                    moveY = 0
                    inventoryMenu()
                if (event.key==K_ESCAPE):
                    moveX=0
                    moveY=0
                    pauseMenu()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_a:
                    moveX=0
                if event.key==pygame.K_d:
                    moveX=0
                if event.key==pygame.K_w:
                    moveY=0
                if event.key==pygame.K_s:
                    moveY=0
        if player.get_x() < 5:
            player.set_rect(DISPLAYWIDTH-100, player.get_y(),
                            player.get_width(), player.get_height())
            level2()
        DISPLAYSURF.blit(background, (0,0))
        player.update(moveX,moveY,levelitems,levelwalls)
        player.draw(DISPLAYSURF)
        levelitems.draw(DISPLAYSURF)
        FPSCLOCK.tick(FPS)
        pygame.display.update()


level2items = pygame.sprite.Group()
coin = Item('c3',350,575,{'coin':1},coinImg,coinSound)
level2items.add(coin)
level2walls = pygame.sprite.Group()
wall = Wall('w4',0,450,1000,10)
wall1 = Wall('w5',0,683,1000,10)
wall2 = Wall('w6',0,450,5,300)
level2walls.add(wall, wall1, wall2)

all_sprites.add(level2walls,level2items)

def level2():
    moveX,moveY=0,0
    player.set_location(level2)
    background = pygame.image.load("backgrounds/forestfront.jpg").convert()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    moveX = -5
                if event.key==pygame.K_d:
                    moveX = 5
                if event.key==pygame.K_w:
                    moveY = -5
                if event.key==pygame.K_s:
                    moveY = 5
                if event.key==pygame.K_e:
                    moveX = 0
                    moveY = 0
                    inventoryMenu()
                if (event.key==K_ESCAPE):
                    moveX=0
                    moveY=0
                    pauseMenu()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_a:
                    moveX=0
                if event.key==pygame.K_d:
                    moveX=0
                if event.key==pygame.K_w:
                    moveY=0
                if event.key==pygame.K_s:
                    moveY=0
        if player.get_x() > DISPLAYWIDTH-90:
            player.set_rect(10, player.get_y(), player.get_width(), player.get_height())
            level()
        DISPLAYSURF.blit(background, (0,0))
        player.update(moveX,moveY,level2items,level2walls)
        player.draw(DISPLAYSURF)
        level2items.draw(DISPLAYSURF)
        FPSCLOCK.tick(FPS)
        pygame.display.update()

#START LOCATION
player.set_location(level)
######START GAME
startMenu()
