""" We need
	1. initial_position - starting position
	2. primitive(pos) - returns if pos is a terminal state
	3. gen_moves(pos) - returns list of possible moves
	3. do_moves(pos, move) - makes move from pos if legal """

""" Simple solver for a subtraction game.
	Default is the four-to-one game. 
	Written in python 3.5"""

class Subtraction_Game:

	def __init__(self, position = 4, primitives = 0, subtraction = [1,2]):
		self.initial_position = position
		self.subtraction = subtraction
		self.primitives = primitives
		self.current = 0

	def primitive(self, pos):
		if pos == self.primitive:
			return True
		return False

	def gen_moves(self, pos):
		return [x for x in self.subtraction if pos - x >= 0]

	def do_moves(self, pos, move):
		next_moves = self.gen_moves(pos)

		if move in next_moves:
			return pos - move
		else:
			return "Illegal Move"

	# solve will return whether a position (default initial position) is a winning position or not
	def solve(self, pos = self.intial_position):
		if primitive(pos) and self.current == 0:
			return "Win"
		elif primitive(pos) and self.current == 1:
			return "Lose"

		# not finished yet
		


		











