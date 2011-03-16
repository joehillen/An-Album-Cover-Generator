#!/usr/bin/python

"""
* Copyright (C) 2011 Joe Hillenbrand <joehillen@gmail.com>
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Affero General Public License as
* published by the Free Software Foundation, either version 3 of the
* License, or (at your option) any later version.
* 
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU Affero General Public License for more details.
* 
* You should have received a copy of the GNU Affero General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import Image, ImageDraw, ImageFont
import commands, os

class CoverCreator:

	def __init__(self, ideal_width=500, ideal_height=500, image=None):
		self.image = image
		self.ideal_width = ideal_width
		self.ideal_height = ideal_height
		
	# apply vintage effect using GIMP
	def vintage(self, filename):
		tmp_file = "/tmp/" + os.path.basename(filename)
		commands.getoutput("gimp-console -i -b '(once-vintage-look \"{0}\" \"{1}\")' -b '(gimp-quit 0)'".format(filename, tmp_file))
		self.image = Image.open(tmp_file)
		os.remove(tmp_file)

	# crop and/or add a border
	def resize(self, color):
		# im is for image
		im_width, im_height = self.image.size
		
		#if image is too big, crop it
		if self.ideal_width < im_width and self.ideal_height < im_height:
			left = (im_width - self.ideal_width)/2
			upper = (im_height - self.ideal_height)/2
			right = left + self.ideal_width
			lower = upper + self.ideal_width
			image = self.image.crop((left, upper, right, lower))
			im_width, im_height = self.image.size
		
		#image is too wide
		if self.ideal_width < im_width and self.ideal_height >= im_height:
			left = (im_width - self.ideal_width)/2
			right = left + self.ideal_width
			self.image = self.image.crop((left, 0, right, im_height))
			im_width, im_height = self.image.size
		
		#image is too tall
		if self.ideal_width >= im_width and self.ideal_height < im_height:
			upper = (im_height - self.ideal_height)/2
			lower = upper + self.ideal_width
			self.image = self.image.crop((0, upper, im_width, lower))
			im_width, im_height = self.image.size
		
		# if image is too small, add a border
		if self.ideal_width > im_width:
			new_image = Image.new(mode="RGB", size=(self.ideal_width,im_height), color=color)
			left = (self.ideal_width - im_width)/2
			right = left + im_width
			new_image.paste(self.image, (left, 0, right, im_height))
			self.image = new_image
			im_width, im_height = self.image.size
			
		if self.ideal_height > im_height:
			new_image = Image.new(mode="RGB", size=(im_width,self.ideal_height), color=color)
			upper = (self.ideal_height - im_height)/2
			lower = upper + im_height
			new_image.paste(self.image, (0, upper, im_width, lower))
			self.image = new_image
			im_width, im_height = self.image.size
		
		if (im_width, im_height) != (self.ideal_width, self.ideal_height):
			print "Invalid Image Size"
			print "Height: " + im_height
			print "Width: " + im_width
			raise Exception

	# add text
	def text(self, band, album, space, font_size, font_path="FreeSansBold.ttf"):
	
		draw = ImageDraw.Draw(self.image)

		# im is for image
		im_width, im_height = self.image.size

		def fit_font(text, size, font_path, space, width):
			while True:
				font = ImageFont.truetype(font_path, size)
				# t is for text
				t_width, t_height = draw.textsize(text, font=font)
				if (t_width + 2*space) > width :
					size -= 1
					continue
				else:
					break
			return font, t_width, t_height

		band_font, band_width, band_height = fit_font(band[0], font_size, font_path, space, im_width)
		album_font, album_width, album_height = fit_font(album[0], font_size, font_path, space, im_width)

		# d is for draw
		d_height = im_height - album_height # - space
		d_width = im_width - album_width  - space

		draw.text((space, 0), band[0], font=band_font, fill=band[1])
		draw.text((d_width, d_height), album[0], font=album_font, fill=album[1])
		
	def cover(self, filename, band, album, output_filename="album.png", bg_color="black", 
				band_color="white", album_color="white",
				space=10, font_size=64, font=None):
		self.vintage(filename)
		self.resize(bg_color)
		if font:
			self.text((band, band_color),(album, album_color), space, font_size, font)
		else:
			self.text((band, band_color),(album, album_color), space, font_size)
		self.image.save(output_filename)

# test code
if __name__ == "__main__":
	x = CoverCreator()
	x.vintage("test.jpg")
	x.resize("black")
	x.text(("Hello World", "white"), ("herp a derp jerp herp","white"), 10, 64)
	x.image.save("album.png")
