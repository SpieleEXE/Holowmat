import pygame

# Button class
class Button():
    def __init__(self, x, y, image, scale):
        # Setup button
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int (height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False


    def draw(self, screen):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouse
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw Button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# Buttons
class AnimatedButton:
    def __init__(self, x, y, frames, scale=1):
        self.frames = frames
        self.index = 0
        self.image = frames[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.scale = scale
        self.clicked = False

    def draw(self, screen):
        action = False
        # Animation
        self.index += 1
        if self.index >= len(self.frames):
            self.index = 0
        self.image = pygame.transform.scale(self.frames[self.index],
                                            (int(self.rect.width * self.scale),
                                             int(self.rect.height * self.scale)))

        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouse
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Button zeichnen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action