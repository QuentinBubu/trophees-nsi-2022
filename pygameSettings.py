from src.utils.constante import BLANC, NOIR
import pygame

INTERLIGNE = 5

pygame.init()

font = pygame.font.SysFont('Candara', 40)

screen = pygame.display.set_mode((1280, 720))

def get_largeur(element:pygame.Surface) -> int:
    return element.get_size()[0]

def get_hauteur(element:pygame.Surface) -> int:
    return element.get_size()[1]

def pourcentage(gauche:int, haut:int, element:pygame.Surface = None, nb_el:int = 1) -> tuple:
    screen_taille = screen.get_size()
    if element == None:
        return (gauche * screen_taille[0], haut * screen_taille[1])
    else:
        el_taille = element.get_size()
        return (
            (gauche * screen_taille[0]) + (el_taille[0] // 2) - nb_el // 2 * el_taille[0],
            (haut * screen_taille[1]) + (el_taille[1] // 2) - nb_el // 2 * el_taille[1]
        )

def afficher_text(text, position = (0.5, 0.5), screen = screen, font = font, antialias = True, color = BLANC, background = NOIR):
    textes = text.split('\n')
    textes_traites = []
    for txt in textes:
        textes_traites.append(font.render(txt, antialias, color, background))
    position = pourcentage(position[0], position[1], textes_traites[0], len(textes_traites))
    for n, txt in enumerate(textes_traites):
        screen.blit(txt, (position[0], position[1] + get_hauteur(txt) * n))