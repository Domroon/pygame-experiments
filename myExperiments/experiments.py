import pygame
import random

pygame.init()

screenWidth = 1280
screenHeight = 720

window = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()


class Rectangle:
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

    def change_color(self, color_list):
        current_color = self.color
        random_number = random.randint(0, 3)
        random_color = color_list[random_number]
        if current_color == random_color:
            if random_number == 3:
                self.color = color_list[random_number - 1]
            elif random_number == 0:
                self.color = color_list[random_number + 1]
            else:
                self.color = color_list[random_number + 1]
        else:
            self.color = color_list[random_number]


def redraw(rectangles):
    window.fill((0, 0, 0))
    # startRect.draw(window)
    for rectangle in rectangles:
        rectangle.draw(window)
    pygame.display.update()


def main():
    rectangles = []

    # define middle of the rectangle
    rectWidth = 20
    rectHeight = 20
    middleXofRect = (screenWidth-rectWidth)/2
    middleYofRect = (screenHeight-rectHeight)/2

    # Rectangle Colors
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    color_list = [red, green, blue, yellow]
    color_counter = 0

    # Screen Borders
    rightScreenBorder = screenWidth - rectWidth
    leftScreenBorder = 0
    topScreenBorder = 0
    bottomScreenBorder = screenHeight - rectHeight


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

            # if the direction velocities would both 0, the rectangle would not movr
            if randomRectXvelocity == 0 and randomRectYvelocity == 0:
                randomRectXvelocity += 1
                randomRectYvelocity += 1

            # put the rectangle on a random place on screen
            randomXcoord = random.randint(leftScreenBorder, rightScreenBorder)
            randomYcoord = random.randint(topScreenBorder, bottomScreenBorder)

            random_color = color_list[random.randint(0, 3)]

            rectangles.append(Rectangle(randomXcoord, randomYcoord,
                               rectWidth, rectHeight, random_color, randomRectXvelocity, randomRectYvelocity))
            pygame.time.delay(100)

        # move the rectangles
        for rectangle in rectangles:
            rectangle.x += rectangle.x_velocity
            rectangle.y += rectangle.y_velocity

        # check for border collision and change color and direction
        for rectangle in rectangles:
            if rectangle.y == topScreenBorder:
                rectangle.y_velocity *= -1
            if rectangle.x == rightScreenBorder:
                rectangle.x_velocity *= -1
            if rectangle.y == bottomScreenBorder:
                rectangle.y_velocity *= -1
            if rectangle.x == leftScreenBorder:
                rectangle.x_velocity *= -1
            if rectangle.y == topScreenBorder or rectangle.y == bottomScreenBorder or rectangle.x == rightScreenBorder\
                    or rectangle.x == leftScreenBorder:
                rectangle.change_color(color_list)

        redraw(rectangles)


if __name__ == '__main__':
    main()