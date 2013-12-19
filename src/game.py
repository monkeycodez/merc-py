#!/usr/bin/python
#
#
#
#

class Group:
	def __init__(self, *sprites):
		if sprites is not None:
			self.sprites = sprites
		else:
			self.sprites = []
	def copy(self):
		return Group(sprites)
	def add(self, sprite):
		self.sprites.append(sprite)

class GameBoard:
	"""Represents the game board with a 2d list of tiles
	
	Notes:
		map is a 2d list that stores the data,
		<instance>[x][y] is the proper way to access a tile

	"""
	def __init__(self, xlen, ylen):
		self.map = [None] * xlen
		for i, ig in enumerate(self):
			self.map[i] = [None] * ylen
		self.ents = []
		self.size = (xlen, ylen)

	def __getitem__(self, key):
		return self.map[key]

	def __len__(self):
		'''Returns the xlen of the map'''
		return len(self.map)


class BasicTile:
	'''A basic tile for GameBoard'''
	def __init__(self, xl, yl, surf, ent=None):
		self.xl = xl
		self.yl = yl
		self.surf = surf
		self.ent = ent

class BasicEnt:
	'''Basic Entity'''
	def __init__(self, tile, surf):
		self.tile = tile
		self.surf = surf
		tile.ent = self
	
	def move_to(self, tile):
		self.tile.ent = None
		tile.ent = self
		self.tile = tile


def build_gb(genv):
	xlen, ylen = genv['gridsz']
	gb = GameBoard(xlen, ylen)
	imgs = genv['imgs']
	for xl, lx in enumerate(gb):
		for yl, ly in enumerate(lx):
			gb[xl][yl] = BasicTile(xl, yl, imgs['forest_t'])
	return gb

if __name__ == "__main__":
	gb = GameBoard(20, 20)


