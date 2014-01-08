#!/usr/bin/python
#	
#	winsys.py:	implements a psudo window system on pygame
#	
#

import pygame
from pygame.locals import *

class WinSysError(Exception): pass

class Window(object):
	def __init__(size, alpha=True, news=False):
		self.size = size
		if alpha:
			self.win = pygame.Surface(size).convert_alpha()
		else:
			self.win = pygame.Surface(size, 0, pygame.display.get_surface())

class Screen(object):
	def __init__(**kargs):
		'''Initalizes the screen
		avalible args:
			scr - an already initalized screen.  cannot be used with
				anything else

		'''
		scr = kargs.get('scr')
		if scr is not None:
			self.scr = scr
			self.size = scr.get_size()
			fl = scr.get_flags() & FULLSCREEN
			self.full = False
			if fl:
				self.full = True
		else:
			raise WinSysError('other modes not implemented yet')

	def add_win(win, layer):
		pass

	def draw():
		pass
			

