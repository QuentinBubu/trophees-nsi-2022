from src.utils.constante import BLANC
import pygame

INTERLIGNE = 10
MAIN = 'main'
PROLOGUE = 'prologue'

def display_set_mode(size:tuple):
    return pygame.display.set_mode(size, pygame.RESIZABLE)

def get_largeur(element:pygame.Surface) -> int:
    return element.get_size()[0]

def get_hauteur(element:pygame.Surface) -> int:
    return element.get_size()[1]

def pourcentage(gauche:int, haut:int, parent:pygame.Surface, element:pygame.Surface = None, nb_el:int = 1) -> tuple:
    screen_taille = parent.get_size()
    if element == None:
        return (gauche * screen_taille[0], haut * screen_taille[1])
    else:
        el_taille = element.get_size()
        return (
            (gauche * screen_taille[0]) + (el_taille[0] / 2) - el_taille[0],
            (haut * screen_taille[1]) + ((el_taille[1]) / 2) - nb_el / 2 * el_taille[1] - (INTERLIGNE * sum([i for i in range(nb_el - 1)]) / 2) / 2
        )

def afficher_text(text, parent:pygame.Surface, font, position = (0.5, 0.5), antialias = True, color = BLANC, background = None, alpha = 255):
    textes = text.split('\n')
    textes_traites = []
    for txt in textes:
        text_render = font.render(txt, antialias, color, background)
        text_render.set_alpha(alpha)
        textes_traites.append(text_render)
    position = pourcentage(position[0], position[1], parent, textes_traites[0], len(textes_traites))
    h_max = max([i.get_size() for i in textes_traites], key=lambda item:item[1])[1]
    for n, txt in enumerate(textes_traites):
        parent.screen.blit(txt, (position[0], position[1] + INTERLIGNE * n + h_max * n))
