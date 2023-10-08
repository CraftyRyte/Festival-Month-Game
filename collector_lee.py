import game
import pygame as pg

class CollectorLee:
    def __init__(self, surface, width, height) -> None:
        self.screen = surface
        self.width = width
        self.height = height
        self.background = pg.transform.scale(pg.image.load('assets/backgorund.png'), (width, height))

    def run(self):
        self.screen.blit(self.background, (0, 0))
