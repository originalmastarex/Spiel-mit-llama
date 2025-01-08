from os.path import join
import pygame.image
import sys

pygame.init()
screen = pygame.display.set_mode((600,500))

#Spieler

Raumschiff_Bild = pygame.image.load(join("Bilder", "Spieler", "Raumschiff.png")).convert_alpha()




Gameover_Bild = pygame.image.load(join("Bilder", "Gameover", "Gameover_Bild.png")).convert_alpha()
Weltraum_Bild= pygame.image.load(join("Bilder", "Map", "Weltraum.jpeg")).convert_alpha()

#Flammen

Komet_Bild= pygame.image.load(join("Bilder", "Objekte", "Komet.png")).convert_alpha()


#Spieler

Raumschiff = pygame.transform.scale(Raumschiff_Bild, (80, 90))




Gameover = pygame.transform.scale(Gameover_Bild, (400, 400))
Weltraum = pygame.transform.scale(Weltraum_Bild, (600, 500))

#Flammen

Komet = pygame.transform.scale(Komet_Bild, (80, 80))


pygame.quit()

