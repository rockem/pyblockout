# def create_background(screen):
#     background = pygame.Surface(screen.get_size())
#     background = background.convert()
#     background.fill((0, 0, 0))
#     return background
#
#
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("BlockOut")
#
#     actionsProvider = UserActionsProvider()
#
#     clock = pygame.time.Clock()
#     control = PackControl((screen.get_rect().width, screen.get_rect().height))
#     control.actionsProvider = actionsProvider
#     pack = PackSprite(control)
#     allSprites = pygame.sprite.RenderPlain(pack)
#
#     background = create_background(screen)
#     while True:
#         clock.tick(120)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 return
#             elif event.type == KEYDOWN and event.key == K_ESCAPE:
#                 return
#             else:
#                 actionsProvider.handle_event(event)
#
#         allSprites.update()
#         screen.blit(background, (0, 0))
#         allSprites.draw(screen)
#         pygame.display.flip()
from BlockOut import BlockOut

if __name__ == '__main__':
    BlockOut().run()