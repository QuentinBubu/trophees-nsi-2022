from src.utils.constante import BLANC
import pygame

INTERLIGNE = 10

def display_set_mode(size:tuple):
    """S'occupe du resize (variation de la taille de la fenêtre)

    Args:
        size (tuple): taille de la fenêtre

    Returns:
        Pygame : Redimenssionage
    """
    return pygame.display.set_mode(size, pygame.RESIZABLE)

########################GETTRE########################

def get_largeur(element:pygame.Surface) -> int:
    return element.get_size()[0]

def get_hauteur(element:pygame.Surface) -> int:
    return element.get_size()[1]

###################################################

def pourcentage(gauche:int, haut:int, parent:pygame.Surface, element:pygame.Surface = None, nb_el:int = 1) -> tuple:
    """Permet de donner un pourcentage de la hauteur 
    de la longueur souhaitée par rapport aux dimensions
    de l'écran

    Args:
        gauche (int): largeur
        haut (int): hauteur
        parent (pygame.Surface): Surface
        element (pygame.Surface, optionel): _____________________. Par défaut None.
        nb_el (int, optionel): ______________________. Par défaut 1.

    Returns:
        tuple: Largeur et Hauteur en pourcentages par rapport aux dimensions de la
        fenetre
    """
    screen_taille = parent.get_size()
    if element == None:
        return (gauche * screen_taille[0], haut * screen_taille[1])
    else:
        el_taille = element.get_size()
        return (
            (gauche * screen_taille[0]) + (el_taille[0] / 2) - el_taille[0],
            (haut * screen_taille[1]) + ((el_taille[1]) / 2) - nb_el / 2 * el_taille[1] - (INTERLIGNE * sum([i for i in range(nb_el - 1)]) / 2) / 2
        )

def afficher_text(text:str, screen, font:str, nom:str, position:tuple = (0.5, 0.5), antialias:bool = True, color:tuple = BLANC, background:tuple = None, alpha:int = 255):
    """Affiche proprement un texte sur l'écran

    Args:
        text (str): texte
        screen (Screen): fenêtre d'affichage
        font (str): police d'écriture
        nom (str): nom
        position (tuple, optionel): Postion sur la fenêtre. Par défaut (0.5, 0.5).
        antialias (bool, optionel): _description_. Par défaut True.
        color (tuple, optionel): couleur du texte. Par défaut BLANC.
        background (tuple, optionel): arrière plan. Par défaut None.
        alpha (int, optionel): couleur invisible. Par défaut 255.

    Returns:
        Pygame (sprite): Renvoie un sprite qui est le texte
    """
    txt_sprite = pygame.sprite.Group()
    textes = text.split('\n')
    textes_traites = []
    for txt in textes:
        textes_traites.append(Text(txt, font, antialias, color, background))
    position = pourcentage(position[0], position[1], screen.get_screen(), textes_traites[0], len(textes_traites))
    h_max = max([i.get_size() for i in textes_traites], key=lambda item:item[1])[1]
    for n, txt in enumerate(textes_traites):
        txt.rect.x = position[0]
        txt.rect.y = position[1] + INTERLIGNE * n + h_max * n
        txt_sprite.add(txt)
    screen.add_sprite(txt_sprite)
    screen.add_on_screen(nom, txt_sprite)
    return txt_sprite
    
class Text(pygame.sprite.Sprite):
    """Sprite du texte

    Args:
        pygame (_type_): sprite
    """
    def __init__(self, txt, font, antialias, color, background):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(txt, antialias, color, background)
        self.rect = self.image.get_rect()
    def get_size(self) -> tuple:
        return (self.rect.width, self.rect.height)