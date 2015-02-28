"""
Manager handles scene control.
"""


def run(view, scene, players=None, model=None, debug=False):
    """
    Run a game loop, running scenes that return scenes or a false value.
    Returns the elements of the game model.
    :param view: The pygame Surface associate with the display.
    :param scene: A scene to be run. Requires a run() method.
    :param players: an object representing a player or players.
    :param model: an object representing the game model.
    :param debug: boolean to control debug printing.
    :return: tuple players, model.
    """

    if debug: print('Manager started.')

    while scene:
        scene, players, model = scene.run(view, players=players, model=model, debug=debug)
        if debug: print('New scene: {}'.format(scene))

    if debug: print('Manager closed.')
    return players, model