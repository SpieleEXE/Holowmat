import pygame

pygame.init()

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

# Neue Klasse für animierten Text
class AnimatedText:
    def __init__(self, text, font, color, position, speed):
        self.text = text
        self.font = pygame.font.SysFont(None, 64)
        self.color = color
        self.position = position  # Dies ist die Mitte des gesamten Textblocks
        self.speed = speed
        self.index = 0
        self.displayed_text = ""
        self.complete_lines = []

        # Text in mehrere Zeilen aufteilen, nach jeweils 6 Wörtern
        self.lines = self.split_text_into_lines(self.text, 6)
        self.line_height = self.font.get_height() + 10  # Abstand zwischen Zeilen

    def split_text_into_lines(self, text, words_per_line):
        """ Teilt den Text in Zeilen, nach jedem `words_per_line`-ten Wort. """
        words = text.split()
        lines = []

        # Gehe durch die Wörter und teile sie in Zeilen auf
        for i in range(0, len(words), words_per_line):
            line = ' '.join(words[i:i + words_per_line])
            lines.append(line)

        return lines

    def update(self):
        """ Fügt nach und nach Buchstaben zum angezeigten Text hinzu. """
        if self.index < len(self.text):
            self.displayed_text += self.text[self.index]
            self.index += 1

        # Aktualisiere die komplett angezeigten Zeilen basierend auf dem aktuellen Text
        self.complete_lines = self.split_text_into_lines(self.displayed_text, 6)

    def draw(self, screen):
        screen_width, screen_height = screen.get_size()

        # Berechne die Höhe des gesamten Textblocks
        total_text_height = len(self.complete_lines) * self.line_height

        # Startposition der ersten Zeile so berechnen, dass der gesamte Textblock zentriert ist
        y = self.position[1] - total_text_height // 2

        # Jede Zeile separat rendern und horizontal zentrieren
        for line in self.complete_lines:
            text_surface = self.font.render(line, True, self.color)
            text_rect = text_surface.get_rect(center=(self.position[0], y))  # Horizontale Zentrierung
            screen.blit(text_surface, text_rect)
            y += self.line_height  # Position für nächste Zeile erhöhen

    def reset(self, new_text):
        """ Setzt den Text und die Animation zurück. """
        self.text = new_text
        self.index = 0
        self.displayed_text = ""
        self.complete_lines = []

        # Aktualisiere die Zeilen, nach jeweils 6 Wörtern
        self.lines = self.split_text_into_lines(new_text, 6)

