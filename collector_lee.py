import pygame as pg
import keyboard as ky
import player

class CollectorLee:
    def __init__(self, surface, width, height, speed, delta_time) -> None:
        self.screen = surface
        self.width = width
        self.height = height
        self.background = pg.transform.scale(pg.image.load('assets/backgorund.png'), (width, height))
        self.player_img = pg.transform.scale(pg.image.load("assets/player.png"), (60, 80))
        self.player = player.Player(self.height, speed, delta_time)
        

    def run(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player_img, (self.player.x, self.player.y))
        self.player.move()
    

