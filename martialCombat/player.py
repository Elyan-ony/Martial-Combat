import pygame;

class Player(pygame.sprite.Sprite):

    def __init__(self, image, pos:tuple, group):
        super().__init__(group);
        self.image = pygame.transform.scale(image, (100, 150));
        self.rect = self.image.get_frect(center = pos);
        self.speed = 430;
        self.direction = pygame.math.Vector2(0, 0);

    def update(self, dt):

        key = pygame.key.get_pressed();

        self.direction.x = key[pygame.K_RIGHT] - key[pygame.K_LEFT];
        self.direction.y = key[pygame.K_DOWN] - key[pygame.K_UP];

        self.direction = self.direction.normalize() if self.direction else self.direction;

        self.rect.center += self.direction * self.speed * dt;