import pygame
import time
import random

pygame.init()
quitcolor = (119,118,110)
black=(0,0,0)
display_width = 800
display_height = 600
gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("CarGameCaden")

clock = pygame.time.Clock()

carimg = pygame.image.load('Car1CSM.jpg')
backgroundpic = pygame.image.load('background-1_0.png')
IMAGE_SMALL = pygame.transform.scale(carimg, (80, 180))
car_width = 100


def obstacle(obs_startx, obs_starty, obs):   # define many car pictures
    if obs == 0:
        obs_pic = pygame.image.load("car1.jpg")
        obs_pic = pygame.transform.scale(obs_pic, (80, 180))
    elif obs == 1:
        obs_pic = pygame.image.load("car2.jpg")
        obs_pic = pygame.transform.scale(obs_pic, (80, 180))
    elif obs == 2:
        obs_pic = pygame.image.load("car3.jpg")
        obs_pic = pygame.transform.scale(obs_pic, (80, 180))
    elif obs == 3:
        obs_pic = pygame.image.load("car4.jpg")
        obs_pic = pygame.transform.scale(obs_pic, (80, 180))
    gamedisplay.blit(obs_pic,(obs_startx,obs_starty))


def car(x,y):
    gamedisplay.blit(IMAGE_SMALL,(x,y))


def text_objects(text,font):   # to define a function that could pass variables to be displayed
    textsurface = font.render(text,True,black)
    return textsurface,textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.SysFont("SimHei",80)
    textsurf,textrect = text_objects(text,largetext)
    textrect.center = ((display_width /2),(display_height/2))
    gamedisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

#unistr = u '識唔識揸車呀黃雅莉'.encode('utf-8')
def crash():
    message_display('識唔識揸車呀傻敏')

def background():
    gamedisplay.blit(backgroundpic,(0,0))



def game_loop():
    x = (display_width*0.45)
    y = (display_height*0.7)
    x_change = 0
    bumped = False

    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200,(display_width-200))
    obs_starty = -750
    obs_width = 47
    obs_height = 125

    while not bumped:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5

            if event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0


        x+=x_change
        gamedisplay.fill(quitcolor)
        background()

        #obs_starty -= (obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed

        car(x,y)

        if x> 750-car_width or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty = 0-obs_height
            obs_startx = random.randrange(170,(display_width-170))
            obs = random.randrange(0,3)

        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx + obs_width: #cars make contact with each other
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()

