import pygame as pg
import pdb
import collector_lee

class Game:
    def __init__(self, fps, dimensions: list, caption) -> None:
        pg.init()
        self.clock = pg.time.Clock()
        self.fps = fps
        self.screen = pg.display.set_mode((dimensions[0], dimensions[1]))
        self.caption = caption
        # pdb.set_trace()
        (self.clock.tick(self.fps))
        self.collector_lee = collector_lee.CollectorLee(self.screen, dimensions[0], dimensions[1], 500, self.clock.tick(self.fps)/1000.0)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
    
    def run(self):
        pg.display.set_caption(self.caption)
        while True:
            self.clock.tick(self.fps)
            self.check_events()
            self.collector_lee.run()
            pg.display.update()
            pg.display.flip()
