import pygame,sys
from pygame.locals import *

##ITEMS
class Item(pygame.sprite.Sprite):
    def __init__(self, name, x, y, itemType, image, sound=None):
        '''name: must be a unique string in order to be loaded correctly
        x: x coordinate
        y: y coordinate
        itemType: a dict with one key value pair {'item_name':quantity}
        image: image string
        sound: sound string'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.itemType = itemType
        self.load_sound(sound)

    def get_name(self):
        return self.name

    def load_sound(self, sound):
        '''loads sound for later use.
        sound: a string location of .WAV file'''
        if sound != None:
            self.sound = pygame.mixer.Sound(sound)
        else:
            self.sound = None

    def play_sound(self):
        '''plays sound'''
        if self.sound != None:
            self.sound.play()

    def pick_up(self):
        '''plays sound and returns itemType'''
        self.play_sound()
        return self.itemType
