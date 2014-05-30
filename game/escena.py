# -*- coding: utf-8 -*-
import spyral
import spyral.debug
import pygame
import math
import random
pygame.mixer.init()

class Elemento1(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(100,100)).fill((255,0,0))
        self.pos = (200,200)

    def comportamiento1(self):
        # Aquí colocar comportamientos, animaciones, etc.
        pass

class Juego(spyral.Scene):
    def __init__(self, activity=None, SIZE=None, *args, **kwargs):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.Image(size=self.size).fill((255,255,255))

        self.elemento1 = Elemento1(self)

        # Define la función "chequea" para determinar el estado del juego
        spyral.event.register("director.update", self.chequea)
        
        # Esto es para poder salir correctamente del juego
        spyral.event.register("system.quit", spyral.director.pop)

        # Este código es para salir de la imagen de inicio del juego
        if activity:
            activity.game_button.set_active(True)
            activity.box.next_page()
            activity._pygamecanvas.grab_focus()
            activity.window.set_cursor(None)
            self.activity = activity

    def chequea(self):
        # Aquí se revisa el estado de los elementos, por ejemplo colisiones.
        pass
