from constants import COLORS
import random

class BaseFloor:
    def __init__(self):
        self.options = [
            ['!', '.', '.', '!', '.', '.', '.', '!'],
            ['.', '.', '!', '.', '.', '.', '!', '.'],
            ['.', '.', '.', '!', '.', '.', '.', '!'],
            ['!', '.', '.', '!', '.', '.', '.', '!'],
            ['.', '.', '!', '.', '.', '.', '!', '.'],
            ['.', '.', '.', '!', '.', '.', '.', '!'],
            ['!', '.', '.', '!', '.', '.', '.', '!'],
            ['.', '.', '!', '.', '.', '.', '!', '.'],
            ['.', '.', '.', '!', '.', '.', '.', '!'],
        ]
        self.colors = {
            '.': COLORS['darkgreen'],
            '!': COLORS['lightgreen'],
        }
        self.pattern = self.get_random_pattern()

    def get_random_pattern(self):
        random_pattern = []
        for i in range(8):
            random_pattern.append(random.choice(self.options))
        return random_pattern
