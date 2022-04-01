import pygame 

pygame.init()

screen = pygame.display.set_mode((800 ,800))

pygame.draw.rect(screen , (139, 0, 0), (100 ,150 ,270 ,30), 0) #A la place de 270 -> jauge
pygame.draw.rect(screen , (0, 0, 255), (100 ,350 ,270 ,30), 0) #A la place de 270 -> jauge
pygame.draw.rect(screen , (0, 200, 0), (100 ,550 ,270 ,30), 0) #A la place de 270 -> jauge

pygame.display.flip()

ouvert = True

while ouvert: 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP :
            ouvert = False


pygame.quit()