#!/usr/bin/python
#
#
#
#
#

import pygame
import pygame.draw
from pygame.locals import *

def draw_selected(tl, gb, genv, surf):
	tilesz = genv['tilesz']
	x = (tl.xl ) * tilesz
	y = (tl.yl ) * tilesz
	pygame.draw.rect(surf, Color('blue'), (x, y, tilesz, tilesz), 1)

def get_tile(gb, pos, genv):
	tilesz = genv['tilesz']
	return gb[pos[0] / tilesz][pos[1] / tilesz]

def draw_gb(gb, genv, to=None):
	tsz = genv['tilesz']
	xsz = len(gb)
	ysz = len(gb[0])
	xend = tsz * xsz
	yend = tsz * ysz
	rct = Rect(0, 0, 1, 1)
	surf = to
	if surf is None:
		surf = pygame.Surface((xend, yend), 0, genv['screen'])
	gcol = genv.get('grid_col', Color('black'))
	#start off by drawing the gridlines
	surf.fill(Color('black'))
	pygame.draw.rect(surf, gcol, Rect(0, 0, xend, yend), 1)
	linel = []			
	for i in range(tsz - 1, ysz * tsz - 1, tsz):
		pygame.draw.line(surf, gcol, (0, i), (xend - 1, i), 2)
	for i in range(tsz - 1, ysz * tsz - 1, tsz):
		pygame.draw.line(surf, gcol, (i, 0), (i, yend - 1), 2)
	#now draw the tiles
	surf.unlock()
	for dm in gb:
		for tl in dm:
			if tl is None:
				continue
			rct.x = tl.xl * tsz + 1
			rct.y = tl.yl * tsz + 1
			surf.blit(tl.surf, rct)
		#	if tl.ent is not None:
		#		surf.blit(tl.ent.surf, rct)

	return surf

def draw_ent(gb, genv, to=None):
	tsz = genv['tilesz']
	xsz, ysz = gb.size
	xend = tsz * xsz
	yend = tsz * ysz
	if to is None:
		to = pygame.Surface((xend, yend), 0, gb['screen'])
	for xl in gb:
		for tl in xl:
			if tl.ent is not None:
				to.blit(tl.ent.surf, (tl.xl * tsz + 1, tl.yl * tsz + 1))

