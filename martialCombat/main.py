import pygame;
from os.path import join;
from player import Player;

pygame.init();

WIDTH, HEIGTH = 600, 600;

screen = pygame.display.set_mode((WIDTH, HEIGTH));
pygame.display.set_caption("Martial Combat");

#Groups
allSprites = pygame.sprite.Group();

#images
playerImg = pygame.image.load("C:/Users/MO/Desktop/mcGame/martialCombat/images/xora.png"); 


#sprites 
player = Player(playerImg, (WIDTH/2, HEIGTH/2), allSprites);
running = True;

clock = pygame.time.Clock();

while running:
    dt = clock.tick();

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;

    screen.fill("gray");

    allSprites.draw(screen);
    allSprites.update(dt/1000);
    
    pygame.display.update();

pygame.quit();