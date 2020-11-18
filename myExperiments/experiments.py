import pygame
import random

pygame.init()

screenWidth = 250
screenHeight = 250

window = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()


class SnakeStartRect:
    def __init__(self, x, y, width, height, color, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = velocity

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


def redraw(startRect):
    window.fill((0, 0, 0))
    startRect.draw(window)
    pygame.display.update()


def main():
    # define middle of the rectangle
    rectWidth = 20
    rectHeight = 20
    middleXofRect = (screenWidth-rectWidth)/2
    middleYofRect = (screenHeight-rectHeight)/2

    # initialize one Rectangle - Object
    randomStartXvelocity = random.randint(-2, 2)
    randomStartXvelocity = random.randint(-2, 2)
    startRect = SnakeStartRect(middleXofRect, middleYofRect, rectWidth, rectHeight, (255, 0, 0), 1)

    # Screen Borders
    rightScreenBorder = screenWidth - startRect.width
    leftScreenBorder = 0
    topScreenBorder = 0
    bottomScreenBorder = screenHeight - startRect.height

    run = True
    while run:
        clock.tick(100)  # fps = 27

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        startRect.x += startRect.velocity
        # startRect.y += startRect.velocity

        if startRect.x > rightScreenBorder or startRect.x == leftScreenBorder:
            startRect.velocity *= -1
        elif startRect.y == topScreenBorder or startRect.y > bottomScreenBorder:
            startRect.velocity *= -1

        redraw(startRect)


if __name__ == '__main__':
    main()