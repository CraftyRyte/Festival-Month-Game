import pygame as pg

DIMENSIONS = [800, 700]

class Game:
    def __init__(self, fps, dimensions: list, caption) -> None:
        pg.init()
        self.clock = pg.time.Clock()
        self.fps = fps
        self.screen = pg.display.set_mode((dimensions[0], dimensions[1]))
        self.caption = caption

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
    
    def run(self):
        pg.display.set_caption(self.caption)
        while True:
            self.check_events()
            self.screen.fill((255, 255, 255))
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game(45, DIMENSIONS, "Festival game")
    game.run()
