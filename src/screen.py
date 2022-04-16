from unicodedata import name
import pygame

class Screen:

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.set_caption('Head Of States')
        self.set_fond('image/imagepygame.jpg')
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont('Candara', 30)
        self.font50 = pygame.font.SysFont('Candara', 50)

        
    def set_caption(self, caption:str):
        pygame.display.set_caption(caption)
        
    def set_fond(self, chemin:str = ''):
        if chemin != '':
            self.chemin = chemin
        self.fond = pygame.image.load(self.chemin).convert_alpha()
        self.fond = pygame.transform.scale(self.fond, self.screen.get_size())
        self.screen.blit(self.fond, (0,0))
        
    def get_screen(self):
        return self.screen

    def blit(self, *args):
        return self.screen.blit(args)

    def get_size(self):
        return self.screen.get_size()