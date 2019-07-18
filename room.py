from item import Item

class Coord():
	def __init__(self, in_coord, item=None):
		self.coord = in_coord
		self.has = item

	def __str__(self):
		return str(self.has)

	def __repr__(self):
		return str(self.has)

	def place(self, in_item):
		self.has = in_item

class Room():
	def __init__(self, characters, width, height):
		self.characters = characters
		self.coord_list = []
		self.width = width
		self.height = height
		
		# Fill the room with coordinates that have no item
		for i in range(height):
			temp = []
			for j in range(width):	
				item = Item('WALL', "☐")
				if (i == 0) or (i == width-1):
					inside = Coord((i, j), item)
					temp.append(inside)
				elif (j == 0) or (j == height-1):
					inside = Coord((i, j), item)
					temp.append(inside)
				else:
					inside = Coord((i,j), Item('Blank', ' '))
					temp.append(inside)
				
			self.coord_list.append(temp)

		# Make a single sample box at 1 down, 5 right
		# single_box = item.Item('box', '☐')
		# self.coord_list[1][5].place(single_box)
	
	def __repr__(self):
		temp_var = ''
		for i in range(self.height):
			for j in range(self.width):
				temp_var += str(self.coord_list[i][j].has.uni) + ' '
			temp_var += '\n'
		return temp_var

	def spawn(self, item, position=(0, 0)):
		i, j = position
		# TODO Change .has to .has.name
		if self.coord_list[i][j].has.name not in ['WALL', 'BOSS', 'Hero', 'Key']: 
			self.coord_list[i][j].has = item
			return True
		return False

	def set_blank(self, pos):
		i, j = pos
		if self.coord_list[i][j].has.name is not 'WALL':
			self.coord_list[i][j].has = Item('Blank', ' ')