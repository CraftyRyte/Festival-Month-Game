import game
import pygame as pg

DIMENSIONS = [800, 700]
game_state = "collector"

if __name__ == "__main__":
    game = game.Game(45, DIMENSIONS, "Collector Lee")
    game.run()
