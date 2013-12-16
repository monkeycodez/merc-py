#!/usr/bin/python
#
#	anim.py:	animation related stuff
#
#
#

import pygame

class BasicAnim(object):
	'''very simple animation, iterates through a list of images
	
	includes an internal clock
	'''
	def __init__(self, scr_period, images, duration=-1):
		'''Create an animation:
			scr_period: time to scroll through each image
			images: list of images
			duration: optional time to last
		'''
		self.active = True
		self.images = images
		self.img_ptr = 0
		self.scr_per = scr_period
		self.dur_cnt = 0
		self.scr_cnt = 0
		self.rect = pygame.Rect(0, 0, 0, 0)
		self.dur = duration
		self._clock = pygame.time.Clock()

	def is_active(self):
		'''is animation still running'''
		return self.active
	
	def update(self, time_passed=-1):
		'''Updates the animation
		
		if time_passed is not passed, the internal clock is used
		'''
		tm = self._clock.tick()
		if time_passed < 0:
			time_passed = tm
		self.scr_cnt += time_passed
		if self.scr_cnt > self.scr_per:
			self.scr_cnt -= self.scr_per
			self.img_ptr = (self.img_ptr + 1) % len(self.images)

		if self.dur > 0:
			self.dur_cnt += time_passed
			if self.dur_cnt >= self.dur:
				self.active = False
	
	def get_img(self):
		return self.images[self.img_ptr]
	
	def draw(self, pos, surf):
		if self.active:
			cimg = self.get_img()
			self.rect.move_ip(pos)
			surf.blit(cimg, self.rect)





