# import player


maps = object()
maps.bar = object()
maps.bar.loop = lambda *args: True

def loop(screen, debug, new_game=True):
    if debug:
        print 'game.game.loop started'

    # create_player
    if not new_game:
        if debug: print 'game.game.loop load continue'
        next_map = maps.bar.loop
    else:
        if debug: print 'game.game.loop new game'

        next_map = maps.bar.loop

    while next_map:
        next_map = next_map(screen, debug)