import pygame
import game


WIN_HEIGHT = 500
WIN_WIDTH = 500
WIN_RES = WIN_HEIGHT, WIN_WIDTH
DEBUG = True


def main(screen, debug):
    if debug: print "Main.main started."

    game.menu.loop(screen, debug)


if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode(WIN_RES)
    pygame.display.set_caption("Test Of Feb15 GameJam")

    main(display, DEBUG)

    if DEBUG:
        print("Game Shutting Down.")

    pygame.quit()
    if DEBUG: print('Game shut down.')