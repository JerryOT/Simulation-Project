import pygame

Colors = {
    'BLACK' : (0, 0, 0),
    'WHITE' : (255, 255, 255),
    'RED' : (255, 0, 0),
    'GREEN' : (0, 255, 0),
    'BLUE' : (0, 0, 255)
}

def Get_Colors():
    return Colors

class MyText():
    def __init__(self,
                 color,
                 background = Colors['BLACK'], antialias=True,
                 fontname="comicsansms", fontsize=16
                 ):
        pygame.font.init()
        self.font = pygame.font.SysFont(fontname, fontsize)
        self.string = ""
        self.pos = (0,0)
        self.color = color
        self.background = background
        self.antialias = antialias

    def Set_String(self, s):
        self.string = s

    def Set_Position(self, x, y):
        new_x = x
        new_y = y
        self.pos = (new_x, new_y)
    
    def Draw(self, screen):
        text = self.font.render(self.string, self.antialias, self.color, self.background)
        screen.blit(text, self.pos)


class Box(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        self.pos = (0,0)
        self.angle = 0
        self.Set_Size(width, height)

    def Set_Size(self, width, height):
        self.image = pygame.Surface([width, height], flags=pygame.SRCALPHA)
        self.image.fill(self.color)

    def Set_Rotation(self, angle):
        self.angle = angle

    def Set_Position(self, x, y):
        new_x = x
        new_y = y
        self.pos = (new_x, new_y)

    def Draw(self, surface, screenWidth, screenHeight):
        image_rot = pygame.transform.rotate(self.image, self.angle)
        rect = image_rot.get_rect()
        rect.center = (self.pos[0] + screenWidth / 2, self.pos[1] + screenHeight / 2)
        surface.blit(image_rot, rect)


class Circle(pygame.sprite.Sprite):
    def __init__(self, color, radius):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        self.pos = (0,0)
        self.radius = radius
        self.Set_Size(radius)

    def Set_Size(self, radius):
        size = radius * 2
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def Set_Position(self, x, y):
        new_x = x
        new_y = y
        self.pos = (new_x, new_y)

    def Draw(self, surface, screenWidth, screenHeight):
        image = self.image
        rect = image.get_rect()
        rect.center = (self.pos[0] + screenWidth / 2, self.pos[1] + screenHeight / 2)
        surface.blit(image, rect)



