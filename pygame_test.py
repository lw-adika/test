import sys
import pygame

#def check_event():
#    for event in pygame.event.get():
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
        #if event.type == pygame.QUIT:
        #    pygame.quit()
        #    sys.exit()
        #elif event.type == pygame.QUIT: 
        #    pygame.quit()
        #    sys.exit()

pygame.init()

size = width, height = 640, 480
speed = [1, 1]
black = 0, 0, 0
#screen = pygame.display.set_mode((10,10),0)
screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            #pygame.event.post(pygame.event.Event(pygame.QUIT))
            pygame.quit()
            sys.exit()

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
