from pygame import Color, Rect, Surface
from random import randint

class Scene():
    def __init__(self):
        self.frame_count = 0
        self.bg_colour = [0, 0, 0]

    def start(self):
        return True

    def update(self, delta):
        self.frame_count += 1

        if self.frame_count % 50 == 0:
            self.bg_colour = [randint(0, 255), randint(0, 255), randint(0, 255)]

    def render(self, target):
        target.fill(self.bg_colour)
        
