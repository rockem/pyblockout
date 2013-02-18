import pygame
from pygame.locals import *
from pack_sprite import PackSprite
from action_provider import UserActionsProvider
from player.pack_player import PackPlayer


def create_background(screen):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    return background


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("BlockOut")

    actionsProvider = UserActionsProvider()

    clock = pygame.time.Clock()
    player = PackPlayer((screen.get_rect().width, screen.get_rect().height))
    player.actionsProvider = actionsProvider
    pack = PackSprite(player)
    allSprites = pygame.sprite.RenderPlain(pack)

    background = create_background(screen)
    while True:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            else:
                actionsProvider.handleEvent(event)

        allSprites.update()
        screen.blit(background, (0, 0))
        allSprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()