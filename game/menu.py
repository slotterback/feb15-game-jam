import game
import pygame
from pygame.locals import KEYUP, QUIT, MOUSEBUTTONUP, K_ESCAPE, K_RETURN


def loop(screen, debug):
    if debug:
        print "game.menu.loop started"
    font = pygame.font.Font('freesansbold.ttf', 20)
    message = font.render('Start', True, (255, 255, 255))
    m_rect = message.get_rect()
    screen_rect = screen.get_rect()

    m_rect.center = screen_rect.center
    screen.blit(message, m_rect)
    running = True
    while running:
        running = handle_events(screen, debug)
        screen.blit(message, m_rect)
        pygame.display.update()
    if debug:
        print "game.menu.loop ended"


def handle_events(screen, debug):
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                return False
            elif event.key == K_RETURN:
                game.loop(screen, debug)
        elif event.type == MOUSEBUTTONUP:
            game.loop(screen, debug)
        elif event.type == QUIT:
            return False

    return True