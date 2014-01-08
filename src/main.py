#!/usr/bin/python

#	Main initalizer/loop for merc
#
#		args supported:	
#			-s WxH 		: set the size of the display
#			-size WxH	: same as above
#			-f,--fullscreen : set fullscreen
#
#
#		genv: the global enviroment dictionary. All globals are to be put 
#			in here, and all config file options will be stored here
#		|name|		|default|	|description|					
#		size		(640,480)	size of the display
#		fullscr		False		wheither or not to use fullscreen
#		grid_col	BLACK		color to use for gridlines
#		screen		<None>		The main 'screen' Surface
#		gclock		<Clock>		A global clock used to control 
#									framerate
#		tilesz		66			The size in pixels of game tiles for drawing
#

import 	os, sys, re
import pygame
from pygame.locals import *
from getopt import getopt, GetoptError
import gd, game
import loadim

def begin_game(genv):
	scr = pygame.display.set_mode(genv['size'], 0, 32)
	genv['screen'] = scr
	gb = game.GameBoard(5, 5)
	genv['gclock'] = pygame.time.Clock()
	genv['grid_col'] = Color('red')
	imgs = loadim.load_file('../dat/img.xml')
	for x, d in enumerate(gb):
		for y, d2 in enumerate(d):
			gb[x][y] = game.BasicTile(x, y, imgs['forest_t'])
	sel = False
	tsel = None
	while True:
		gd.draw_gb(gb, genv, scr)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if (event.type == MOUSEBUTTONDOWN and
					event.button == 1):
				pos = event.pos
				sel = True
				try:
					tsel = gd.get_tile(gb, pos, genv)
				except IndexError:
					sel = False
		if sel:
			gd.draw_selected(tsel, gb, genv, scr)
		genv['gclock'].tick(30)
		pygame.display.flip()

def main(argv):
	'''
		Main method, initalizes pygame
	'''

	pygame.init()
	pygame.font.init()
	pygame.key.set_repeat(800, 50)

	genv = {
		'size' : (640, 480),
		'fullscr' : False,
		'grid_col' : Color('BLACK'),
		'screen' : None,
		'tilesz' : 66
	}

	try:
		opts, args = getopt(
				argv[1:], "s:f", ["size=", "fullscreen"])
	except GetoptError as err:
		print str(err)
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-s", "--size"):
			m = re.match(r'^(\d*)[x](\d*)$', arg)
			if m is None:
				raise Exception("Bad Resolution string: " + str(arg))
			genv["size"] = (int(m.group(1)), int(m.group(2)))
		elif opt in ("-f", "--fullscreen"):
			genv["fullscr"] = True
		else:
			assert False, "unhandled opt" + str(opt)
	print genv
	begin_game(genv)

if __name__ == "__main__":
	main(sys.argv)
