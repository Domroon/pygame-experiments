import pygame

pygame.init()

screenWidth = 500
screenHeight = 500

window = pygame.display.set_mode((500, 500))

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
    startRect = SnakeStartRect(20, 20, 50, 50, (255, 0, 0), 1)

    run = True
    while run:
        clock.tick(250)  # fps = 27

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        startRect.x += startRect.velocity
        startRect.y += startRect.velocity

        if startRect.x > (screenWidth - startRect.width) or startRect.y > (screenHeight - startRect.height):
            startRect.velocity *= -1
        elif startRect.x == 0 or startRect.y == 0:
            startRect.velocity *= -1

        redraw(startRect)


if __name__ == '__main__':
    main()