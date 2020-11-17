import sys, pygame
pygame.init()

size = width, height = 1280, 940
speed = [3, 3]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("new_ball.gif")
ballrect = ball.get_rect()

while 1:
    pygame.time.delay(10) # T = 10ms => 100 Hz
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
