import sys
import pygame
from pygame.locals import *
import engine

class Application:
    def __init__(self):
        self._running = True
        self._display = None
        self.preferences = engine.preferences()
    
    def on_init(self):
        pygame.init()
        self.size = int(self.preferences["disp_width"]),int(self.preferences["disp_height"])
        self._display = engine.display.Display(self.size)
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_mainloop(self):
        pass
    
    def on_render(self):
        self._display.on_render()
        
    def on_quit(self):
        pygame.quit()
    
    def on_execute(self):
        self.on_init()
        
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_mainloop()
            self.on_render()
        self.on_quit()