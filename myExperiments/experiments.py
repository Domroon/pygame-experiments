import pygame
import random


class Rectangle:
    def __init__(self, x, y, width, height, color, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.top_left_corner = {'x': self.x, 'y': self.y}
        self.top_right_corner = {'x': self.x + self.width, 'y': self.y}
        self.bottom_right_corner = {'x': self.x + self.width + self.height, 'y': self.y + self.height}
        self.bottom_left_corner = {'x': self.x, 'y': self.height}
        self.all_x_corner = [self.top_left_corner['x'],
                             self.top_right_corner['x'],
                             self.bottom_right_corner['x'],
                             self.bottom_left_corner['x']]

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

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        # change the corner - coordinates
        self.top_left_corner = {'x': self.x, 'y': self.y}
        self.top_right_corner = {'x': self.x + self.width, 'y': self.y}
        self.bottom_right_corner = {'x': self.x + self.width + self.height, 'y': self.y + self.height}
        self.bottom_left_corner = {'x': self.x, 'y': self.height}
        self.all_x_corner = [self.top_left_corner['x'],
                             self.top_right_corner['x'],
                             self.bottom_right_corner['x'],
                             self.bottom_left_corner['x']]

    def other_rect_hit(self, other_rectangle, color_list):
        for corner in range(0, len(self.all_x_corner)):
            for corner2 in range(0, len(other_rectangle.all_x_corner)):
                if self.all_x_corner[corner] == other_rectangle.all_x_corner[corner2]:
                    return True
                else:
                    return False

        # if other_rectangle.top_left_corner['x'] == self.top_right_corner['x']:
        #    other_rectangle.change_color(color_list)
        #    print(self.top_right_corner['x'])


def redraw(rectangles, test_Rect_1, test_Rect_2, window):
    window.fill((0, 0, 0))
    for rectangle in rectangles:
        rectangle.draw(window)
    test_Rect_1.draw(window)
    test_Rect_2.draw(window)
    pygame.display.update()


def generate_rectangle(leftScreenBorder, rightScreenBorder, topScreenBorder, bottomScreenBorder, rectangles, color_list, rectWidth, rectHeight):
    randomRectXvelocity = random.randint(-1, 1)
    randomRectYvelocity = random.randint(-1, 1)

    # if the direction velocities would both 0, the rectangle would not move
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


def main():
    pygame.init()

    screenWidth = 1280
    screenHeight = 720

    window = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Rectangles")

    clock = pygame.time.Clock()

    rectangles = []  # list to store all rectangles for the screen

    # define the dimensions of a rectangle
    rectWidth = 20
    rectHeight = 20

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

    test_Rect_1 = Rectangle(10, 10, rectWidth, rectHeight, red, 1, 0)
    test_Rect_2 = Rectangle(1250, 10, rectWidth, rectHeight, red, -1, 0)

    run = True
    while run:
        clock.tick(240)  # fps = 27

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            generate_rectangle(leftScreenBorder, rightScreenBorder, topScreenBorder, bottomScreenBorder, rectangles,
                                color_list, rectWidth, rectHeight)

        for rectangle in rectangles:

            rectangle.move()  # move the rectangles

            # check for border collision and change color and direction
            if rectangle.y == topScreenBorder or rectangle.y == bottomScreenBorder:
                rectangle.y_velocity *= -1
                rectangle.change_color(color_list)
            if rectangle.x == rightScreenBorder or rectangle.x == leftScreenBorder:
                rectangle.x_velocity *= -1
                rectangle.change_color(color_list)

        test_Rect_1.move()
        test_Rect_2.move()

        if test_Rect_1.other_rect_hit(test_Rect_2, color_list):
            test_Rect_1.change_color(color_list)
            test_Rect_2.change_color(color_list)


        redraw(rectangles, test_Rect_1, test_Rect_2, window)


if __name__ == '__main__':
    main()