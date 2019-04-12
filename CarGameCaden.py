import pygame
import time


pygame.init()
quitcolor = (119,118,110)
black=(0,0,0)
display_width = 800
display_height = 600
gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("CarGameCaden")

clock = pygame.time.Clock()

carimg = pygame.image.load('Car1WNL.jpg')
backgroundpic = pygame.image.load('background-1_0.png')
IMAGE_SMALL = pygame.transform.scale(carimg, (80, 180))
car_width = 100

def car(x,y):
    gamedisplay.blit(IMAGE_SMALL,(x,y))


def text_objects(text,font):
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
    message_display('識唔識揸車呀黃雅莉')

def background():
    gamedisplay.blit(backgroundpic,(0,0))



def game_loop():
    x = (display_width*0.45)
    y = (display_height*0.7)
    x_change = 0
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                bumped = True
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
        car(x,y)
        if x> 680-car_width or x<110:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

