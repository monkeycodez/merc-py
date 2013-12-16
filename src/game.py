#!/usr/bin/python
#
#
#
#

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

	def __getitem__(self, key):
		return self.map[key]

	def __len__(self):
		'''Returns the xlen of the map'''
		return len(self.map)


class BasicTile:
	'''A basic tile for GameBoard'''
	def __init__(self, xl, yl, surf):
		self.xl = xl
		self.yl = yl
		self.surf = surf;

class BasicEnt:
	'''Basic Entity'''
	def __init__(self, tile, surf):
		self.tile = tile
		self.surf = surf

if __name__ == "__main__":
	gb = GameBoard(20, 20)

