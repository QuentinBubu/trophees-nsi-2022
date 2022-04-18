import pygame

from pygameSettings import afficher_text

class Screen:

    WAITING = 'waiting'
    PROLOGUE = 'prologue'
    MAIN = 'main'

    sprites = pygame.sprite.Group()
    on_screen = {}

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.set_caption('Head Of States')
        self.set_fond('image/temp_debut.jpg')
        self.clock = pygame.time.Clock()
        self.set_logo('image/logo.png')
        self.font = pygame.font.SysFont('Arial', 30)
        self.font50 = pygame.font.SysFont('Arial', 50)

        
    def set_caption(self, caption:str):
        pygame.display.set_caption(caption)
        
    def set_fond(self, chemin:str = ''):
        if chemin != '':
            self.chemin = chemin
        self.fond = pygame.image.load(self.chemin).convert_alpha()
        if self.fond.get_width() < self.fond.get_height():
            self.fond = pygame.transform.rotate(self.fond, -90)
        self.fond = pygame.transform.scale(self.fond, self.screen.get_size())
        self.screen.blit(self.fond, (0,0))
        
    def set_logo(self, chemin:str = ''):
        self.logo = pygame.image.load(chemin).convert_alpha()
        pygame.display.set_icon(self.logo)
        

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
        t = pygame.sprite.Group()
        if type(sprite) == type(t):
            for el in sprite:
                el.kill()
        else:
            sprite.kill()
        self.sprites.remove(sprite)
        self.sprites.empty()
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
        
    def error(self, text:str):
        for sprite in self.get_all_sprites():
            self.remove_sprite(sprite)
        self.screen.fill((255,0,0))
        afficher_text("ERREUR\n" + text + "\nPRESSEZ UNE TOUCHE", self, self.font50, 'ERROR')
        pygame.display.flip()
        stop = False
        while not stop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    stop = True
                if event.type == pygame.QUIT:
                    stop = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    stop = True
        return False