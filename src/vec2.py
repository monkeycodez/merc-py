#!/usr/bin/python
#
#	File: vec2.py
#		Contains a 2d vector implementation
#		
#
#######################################################################

import pygame

class vec2(object):
	"""2d vector class, supports various vector operations"""
	__slots__ = ['x', 'y']
	def __init__(self, x_or_p, y = None):
		if y is None:
			self.x = x_or_p[0]
			self.y = x_or_p[1]
		else:
			self.x = x_or_p
			self.y = y
	
	def __len__(self):
		return 2
	
	def __getitem__(self, key):
		if key == 0:
			return self.x
		elif key == 1:
			return self.y
		else:
			raise IndexError("Invalid subscript to vec2:"
					.join(str(key)))
	
	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)
	
	def __repr__(self):
		return "vec2:(%s, %s)" % (self.x, self.y)
	
	def __eq__(self, o):
		if hasattr(o, "__getitem__") and len(o) == 2:
			return self.x == o[0] and self.y == o[1]
		else:
			return False
	
	def __ne__(self, o):
		if hasattr(o, "__getitem__") and len(o) == 2:
			return self.x != o[0] or self.y != o[1]
		else:
			return True

	def __nonzero__(self):
		return self.x or self.y


if __name__ == "__main__":
		vec = vec2(2, 2)
		

	


