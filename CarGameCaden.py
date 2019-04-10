import pygame

pygame.init()
quitcolor = (119,118,110)
display_width = 800
display_height = 600
gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("CarGameCaden")

clock = pygame.time.Clock()

carimg = pygame.image.load('Car1.jpg')
IMAGE_SMALL = pygame.transform.scale(carimg, (120, 200))   # the display can only recognize the RGB code of colors

def car(x,y):
    gamedisplay.blit(IMAGE_SMALL,(x,y))


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
        car(x,y)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

