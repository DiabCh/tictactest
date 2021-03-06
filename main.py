import logging
import game
import uuid
import os.path
from game import intro_graphic
logging.basicConfig(
    filename=os.path.join('games', f'{uuid.uuid4()}.txt'),
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger('Tic-Tac-Toe App')
if __name__ == '__main__':
    try:
        intro_graphic()
        game.start()
    except BaseException as e:
        logger.exception(e)
