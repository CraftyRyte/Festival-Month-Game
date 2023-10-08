import pygame as pg
import keyboard as ky

class Player:
    def __init__(self, height, speed, delta_time) -> None:
        self.height = height
        self.x = 80
        self.y = self.height//2
        self.player = pg.Rect(self.x, self.y, 60, 80)
        self.speed = speed
        self.dt = delta_time
    
    def move(self):
        if self.y < 0:
            self.y = 0
        elif self.y > (self.height-self.player.height):
            self.y = self.height-self.player.height

        if ky.is_pressed('up'):
            self.y -= self.speed * self.dt
        elif ky.is_pressed('down'):
            self.y += self.speed * self.dt