import pygame
import random

pygame.init()

screenWidth = 700
screenHeight = 500

window = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()


class SnakeStartRect:
    def __init__(self, x, y, width, height, color, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


def redraw(startRect):
    window.fill((0, 0, 0))
    startRect.draw(window)
    pygame.display.update()


def main():
    # define middle of the rectangle
    rectWidth = 10
    rectHeight = 10
    middleXofRect = (screenWidth-rectWidth)/2
    middleYofRect = (screenHeight-rectHeight)/2

    # initialize one Rectangle - Object
    randomStartXvelocity = random.randint(-1, 1)
    randomStartYvelocity = random.randint(-1, 1)
    startRect = SnakeStartRect(middleXofRect, middleYofRect+70,
                               rectWidth, rectHeight, (255, 0, 0), randomStartXvelocity, randomStartYvelocity)

    # Screen Borders
    rightScreenBorder = screenWidth - startRect.width
    leftScreenBorder = 0
    topScreenBorder = 0
    bottomScreenBorder = screenHeight - startRect.height

    #x - Directions
    x_directions = [-1, 0, 1]
    y_directions = [-1, 0, 1]

    run = True
    while run:
        clock.tick(500)  # fps = 27

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        startRect.x += startRect.x_velocity
        startRect.y += startRect.y_velocity

        if startRect.y == topScreenBorder:
            startRect.y_velocity *= -1
        if startRect.x == rightScreenBorder:
            startRect.x_velocity *= -1
        if startRect.y == bottomScreenBorder:
            startRect.y_velocity *= -1
        if startRect.x == leftScreenBorder:
            startRect.x_velocity *= -1

        redraw(startRect)


if __name__ == '__main__':
    main()