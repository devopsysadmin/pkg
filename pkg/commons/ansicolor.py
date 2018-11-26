NOCOLOR = '\033[0m'
ATTRIBUTES = {
	'normal' : 0,
	'bold' : 1
}
BGCOLORS = {
	'none' : 49
	
}
FGCOLORS = {
	'none': 39,
	'red' : 31,
	'green' : 32,
	'blue' : 34
}


class bg(object):
	def __init__(self, color, attribute='normal'):
		self.bgcolor = BGCOLORS.get(color, BGCOLORS['none'])
		self.fgcolor = FGCOLORS['none']
		self.attr = ATTRIBUTES.get(attribute, ATTRIBUTES['normal'])

	def fg(self, color, attribute='normal'):
		self.fgcolor = FGCOLORS.get(color, FGCOLORS['none'])


class fg(object):
	def __init__(self, color, attribute='normal'):
		self.fgcolor = FGCOLORS.get(color, FGCOLORS['none'])
		self.bgcolor = BGCOLORS['none']
		self.attr = ATTRIBUTES.get(attribute, ATTRIBUTES['normal'])

	def bg(self, color, attribute='normal'):
		self.bgcolor = BGCOLORS.get(color, BGCOLORS['none'])


def prints(message, color=None):
	if color:
		xcolor = '\033[%s;%s;%sm' %(color.attr, color.bgcolor, color.fgcolor)
		print('%s%s%s' %(xcolor,message,NOCOLOR) )
	else:
		print(message)







