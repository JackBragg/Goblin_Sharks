import item

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
				if (i == 0) or (i == width-1):
					inside = Coord((i, j), "☐")
					temp.append(inside)
				elif (j == 0) or (j == height-1):
					inside = Coord((i, j), "☐")
					temp.append(inside)
				else:
					temp.append(' ')	
				
			self.coord_list.append(temp)

		# Make a single sample box at 1 down, 5 right
		# single_box = item.Item('box', '☐')
		# self.coord_list[1][5].place(single_box)
	
	def __repr__(self):
		temp_var = ''
		for i in range(self.height):
			for j in range(self.width):
				temp_var += str(self.coord_list[i][j]) + ' '
			temp_var += '\n'
		return temp_var
