import pygame

screen = pygame.display.set_mode((500, 500))

x = 50
y = 50
width = 20
height = 20

rectangle = pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
rectangle2 = pygame.draw.rect(screen, (0, 255, 0), (x + 20, y, width, height))
rectangle2.move((100, 100))
rectangle2.
pygame.display.update()
pygame.time.delay(5000)

