# import player


# These classes are stand-ins for a none existent module.

class bar(object):

    def __init__(self):
        pass

    def loop(self):
        return None


class maps(object):
    pass
    bar = bar()

# End stand in classes.


def loop(screen, debug, new_game=True):
    if debug:
        print 'game.game.loop started'

    # create_player
    if not new_game:
        if debug: print 'game.game.loop load continue'
        next_map = maps.bar.loop
    else:
        if debug: print 'game.game.loop new game'

        next_map = maps.bar.loop()

    while next_map:
        next_map = next_map(screen, debug)

    if debug: print 'game.game.loop ended'