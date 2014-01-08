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

def _get_sprite(el, surf, line, ckey=None):
	text = el.text
	m = re.search(r'\s?(\d*)\s?,\s?(\d*)\s?,\s?(\d*)\s?,\s?(\d*)', text)
	if m is None:
		raise Exception('Bad text: @'.join(str(elem.sourceline)))
	x1 = int(m.group(1))
	y1 = int(m.group(2))
	x2 = int(m.group(3))
	y2 = int(m.group(4))
	sprite = pygame.Surface((x2 - x1, y2 - y1), 0, surf)
	sprite.blit(surf, (0, 0), pygame.Rect(x1, y1, x2 - x1, y2 - y1))
	if ckey is not None:
		sprite.set_colorkey(ckey)
	return sprite


def _lf(elem, root_tag, path, dict):
	f_tag = elem.get('prefix', '')
	fn = elem.get('fname', None)
	if fn is None:
		raise Exception,'Error, no file name: @'.join(str(elem.sourceline))
	surf = pygame.image.load(os.path.join(path, fn))
	ckey = elem.get('colorkey', None)
	if ckey is not None and surf.get_masks()[3] == 0:
		ckey = pygame.Color(ckey)
		surf.set_colorkey(ckey)
	elif surf.get_masks()[3] != 0:
		ckey = None
		surf = surf.convert_alpha()
	else:
		surf = surf.convert()
	for el in elem:
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
		sprite = _get_sprite(el, surf, el.sourceline, ckey)
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
		_lf(elem, root_tag, path, dict)
	return dict

if __name__ == '__main__':
	pygame.init()
	load_file('../dat/img.xml')









