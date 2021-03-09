
def get_current_player(step, player1, player2):
    """
    This function is used for getting data about the current player.
    :param step: Integer about the current iteration.
    :return: (player_name, player_sign)
    """
    if step % 2 == 0:
        name = player1["name"]
        sign = 'x'
    else:
        name = player2["name"]
        sign = 'o'

    return name, sign
