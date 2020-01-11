from arkanoid.game import Game
from arkanoid.stage_intro import IntroStage
from arkanoid.stage_game import GameStage
from arkanoid.stage_outro import OutroStage


class Arkanoid(Game):
    def __init__(self):
        super().__init__(100, 'Арканоид', (1130, 700))

        self._stages = {
            'intro': IntroStage(),
            'game': GameStage(),
            'outro': OutroStage(),
            'quit': None
        }


    def get_stage(self, name=None):
        if not name:
            name = 'intro'

        return self._stages.get(name, None)
