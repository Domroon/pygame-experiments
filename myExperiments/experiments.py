import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))

x = 50
y = 50
width = 40
height = 60
vel = 5

pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
pygame.display.update()
pygame.time.delay(500)

window.fill((0, 0, 0))

pygame.draw.rect(window, (255, 0, 0), (x + 10, y, width, height))
pygame.display.update()
pygame.time.delay(500)

window.fill((0, 0, 0))

pygame.draw.rect(window, (255, 0, 0), (x + 30, y, width, height))
pygame.display.update()
pygame.time.delay(500)