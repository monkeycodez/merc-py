#!/usr/bin/python
#
#	Loads a set of images from the "spritexml" format
#
#	Format specification:
#		This uses an xml file to specify sprites from images
#		
#		XML format:
#			root tag:	"spritedef"

import os
import re
import pygame
import lxml.etree as ET

def _get_sprite(text, surf, line):
	mch = text.split(',')
	if len(mch) != 4:
		raise Exception,'Bad sprite specifier'.join(str(line))
	x1 = int(mch[0])
	y1 = int(mch[1])
	x2 = int(mch[2])
	y2 = int(mch[3])
	sprite = pygame.Surface((x2 - x1, y2 - y1))
	sprite.blit(surf, (0, 0), pygame.Rect(x1, y1, x2 - x1, y2 - y1))
	return sprite


def _lf(elem, root_tag, path, dict):
	f_tag = elem.get('prefix', '')
	fn = elem.get('fname', None)
	if fn is None:
		raise Exception,'Error, no file name: @'.join(str(elem.sourceline))
	surf = pygame.image.load(os.path.join(path, fn))
	surf = surf.convert()
	for el in elem:
#		print el
		if el.tag != 'sprite':
			raise Exception,'Error, bad tag: '.join(el.tag).join(
					'@').join(str(el.sourceline))
		el_name = el.get('name', None)
		if el_name is None:
			raise Exception,'Error: no sprite name @'.join(str(el.souceline))
		full_name = root_tag.join(f_tag).join(el_name)
		if dict.get(full_name, None) is not None:
			raise Exception,'Error: full name already defined: '.join(
					full_name).join('@').join(el.sourceline)
		sprite = _get_sprite(el.text, surf, el.sourceline)
		dict[full_name] = sprite

def load_file(fn):
	'''Loads a spritexml file
		fn: string of the path to the filename
		returns: dict mapping sprite_name -> sprite_surf
	'''
	tree = ET.parse(fn)
	path = fn
	path = os.path.dirname(path)
	root = tree.getroot()
	dict = {}
	if root.tag != 'spritedef':
		raise Exception, 'Error: Root node is not spritedef'.join(root.tag)
	root_tag = root.get('prefix', '')
	for elem in root:
		if elem.tag != 'file':
			raise Exception, 'Error, bad tag: '.join(elem.tag).join(
					'@').join(str(elem.sourceline))
#		print elem
		_lf(elem, root_tag, path, dict)
	return dict

if __name__ == '__main__':
	pygame.init()
	load_file('../dat/img.xml')
