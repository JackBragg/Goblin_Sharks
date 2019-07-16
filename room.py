import item

class Coord():
	def __init__(self, in_coord, item=None):
		self.coord = in_coord
		self.has = item

	def __str__(self):
		return str(self.coord)

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
			for j in range(width):
				self.coord_list[i][j] = 'w'

		# Make a single sample box at 1 down, 5 right
		# single_box = item.Item('box', '☐')
		# self.coord_list[1][5].place(single_box)
	
	def __repr__(self):
		temp_var = ''
		for i in range(self.height):
			for j in range(self.width):
				temp_var += self.coord_list[i][j]
			temp_var += '\n'
		return temp_var
