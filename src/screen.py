import pygame

class Screen:
    
    sprites = pygame.sprite.Group()
    on_screen = {}

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
    
    def set_screen(self, screen):
        self.screen = screen

    def blit(self, *args):
        return self.screen.blit(args)

    def get_size(self):
        return self.screen.get_size()
    
    def get_all_sprites(self):
        return self.sprites
    
    def add_sprite(self, sprite):
        self.sprites.add(sprite)
        self.update()
        
    def remove_sprite(self, sprite):
        self.sprites.empty()
        self.sprites.remove(sprite)
        self.update()
        
    def add_on_screen(self, nom, element):
        self.on_screen[nom] = element
        
    def remove_on_screen(self, nom):
        if nom in list(self.on_screen.keys()):
            self.remove_sprite(self.on_screen[nom])
            del self.on_screen[nom]

    def update(self):
        self.sprites.update()
        self.sprites.draw(self.screen)
        pygame.display.flip()