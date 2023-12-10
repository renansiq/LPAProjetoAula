#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from pygame.font import Font

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # tamanho da tela

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
        pass


