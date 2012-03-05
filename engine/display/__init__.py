import pygame

class Display:
    def __init__(self,size):
        self.size = size
        self.surface = pygame.display.set_mode(self.size,pygame.HWSURFACE | pygame.DOUBLEBUF)
        
    def on_render(self):
        pygame.display.flip()