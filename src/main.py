import os
import pygame
from pygame.locals import *


def load_image(name, colorkey=None):
    fullname = os.path.join('image', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("BlockOut")

    pack, rect = load_image('pack.png')

    screen.blit(pack, (screen.get_rect().width / 2 - rect.width / 2, screen.get_rect().height - (rect.height + 2)))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return


if __name__ == '__main__':
    main()