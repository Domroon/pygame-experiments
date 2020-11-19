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


def redraw(startRect, rectangles):
    window.fill((0, 0, 0))
    startRect.draw(window)
    for rectangle in rectangles:
        rectangle.draw(window)
    pygame.display.update()

def main():
    rectangles = []

    # define middle of the rectangle
    rectWidth = 40
    rectHeight = 40
    middleXofRect = (screenWidth-rectWidth)/2
    middleYofRect = (screenHeight-rectHeight)/2

    # Rectangle Colors
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    color_list = [red, green, blue, yellow]
    random_color = color_list[random.randint(1, 3)]
    color_counter = 0

    # initialize one Rectangle - Object
    randomStartXvelocity = random.randint(-1, 1)
    randomStartYvelocity = random.randint(-1, 1)
    startRect = SnakeStartRect(middleXofRect+10, middleYofRect+70,
                               rectWidth, rectHeight, random_color, randomStartXvelocity, randomStartYvelocity)

    # Screen Borders
    rightScreenBorder = screenWidth - startRect.width
    leftScreenBorder = 0
    topScreenBorder = 0
    bottomScreenBorder = screenHeight - startRect.height

    # Directions
    x_directions = [-1, 0, 1]
    y_directions = [-1, 0, 1]

    run = True
    while run:
        clock.tick(500)  # fps = 27

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            randomRectXvelocity = random.randint(-1, 1)
            randomRectYvelocity = random.randint(-1, 1)
            rectangles.append(SnakeStartRect(middleXofRect, middleYofRect+70,
                               rectWidth, rectHeight, random_color, randomRectXvelocity, randomRectYvelocity))
            pygame.time.delay(100)

        startRect.x += startRect.x_velocity
        startRect.y += startRect.y_velocity

        # calculations for other rectangles
        for rectangle in rectangles:
            rectangle.x += rectangle.x_velocity
            rectangle.y += rectangle.y_velocity
            if rectangle.y == topScreenBorder:
                rectangle.y_velocity *= -1
            if rectangle.x == rightScreenBorder:
                rectangle.x_velocity *= -1
            if rectangle.y == bottomScreenBorder:
                rectangle.y_velocity *= -1
            if rectangle.x == leftScreenBorder:
                rectangle.x_velocity *= -1

        if startRect.y == topScreenBorder:
            startRect.y_velocity *= -1
            startRect.color = color_list[color_counter]
            color_counter += 1
            if color_counter == 4:
                color_counter = 0

        if startRect.x == rightScreenBorder:
            startRect.x_velocity *= -1
            startRect.color = color_list[color_counter]
            color_counter += 1
            if color_counter == 4:
                color_counter = 0

        if startRect.y == bottomScreenBorder:
            startRect.y_velocity *= -1
            startRect.color = color_list[color_counter]
            color_counter += 1
            if color_counter == 4:
                color_counter = 0

        if startRect.x == leftScreenBorder:
            startRect.x_velocity *= -1
            startRect.color = color_list[color_counter]
            color_counter += 1
            if color_counter == 4:
                color_counter = 0



        redraw(startRect, rectangles)


if __name__ == '__main__':
    main()