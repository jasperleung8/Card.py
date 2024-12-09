import pygame
import time
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Christmas card")

image1 = pygame.image.load("Card1.jpeg")
image2 = pygame.image.load("Card2.jpeg")
image3 = pygame.image.load("Card3.jpg")

image1 = pygame.transform.scale(image1,(500,500))
image2 = pygame.transform.scale(image2,(500,500))
image3 = pygame.transform.scale(image3,(500,500))

while (True):

    screen.fill((255,255,255))
    screen.blit(image1,(0,0))
    pygame.display.update()
    time.sleep(2)

    screen.fill((255,255,255))
    screen.blit(image3,(0,0))
    pygame.display.update()
    time.sleep(2)

    font = pygame.font.SysFont("Arial",36)
    text = font.render("Merry Christmas !",True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(image2,(0,0))
    screen.blit(text,(0,0))
    pygame.display.update()
    time.sleep(2)

    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
