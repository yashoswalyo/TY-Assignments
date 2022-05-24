# Assignment 5 - Constrain Satisfaction
# 1. Map Coloring
# 2. Cryptarithmetic
# Name - Hasnain Merchant Div - B Roll No - 30
from colorama import Fore, Back, Style, init
init(strip=False)
init(autoreset=True)
class map_coloring():
	# Colors Used
	colors = [Fore.RED+'Red', Fore.GREEN+'Green', Fore.YELLOW+'Yellow',
	Fore.MAGENTA+'Violet']
	# Map
	states = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
	neighbors = {}
	neighbors['A'] = ['B', 'C', 'D']
	neighbors['B'] = ['A', 'C']
	neighbors['C'] = ['A', 'B', 'D', 'E']
	neighbors['D'] = ['A', 'C', 'F', 'E']
	neighbors['E'] = ['F', 'C', 'D']
	neighbors['F'] = ['E', 'D', 'G']
	neighbors['G'] = ['F']
	# Output
	colors_of_states = {}
	def print_graph(self):
		for key in self.neighbors:
			print(Fore.CYAN+ key + Fore.WHITE + ' -> ', self.neighbors[key])
	def promising(self, state, color):
		for neighbor in self.neighbors.get(state):
			color_of_neighbor = self.colors_of_states.get(neighbor)
			if color_of_neighbor == color:
				return False
		return True
	def get_color_for_state(self, state):
		for color in self.colors:
			if self.promising(state, color):
				return color
	def start(self):
		print(Fore.BLUE+"\n\n\t\tThe Graph Is ")
		self.print_graph()
		print("\n\n")
		for state in self.states:
			self.colors_of_states[state] = self.get_color_for_state(state)
			print(f"Color Used For State {state} is {self.colors_of_states[state]}")
			print(Fore.BLUE+"\n\n\t\tThe Solution Is - ")
			for key in self.colors_of_states:
				print(Fore.BLUE+key + Fore.WHITE+' -> ', self.colors_of_states[key])

class cryptarithmetic():
	solved = False
	count = 0
	def start(self):
		word1 = input("Enter First Word - ").upper()
		word2 = input("Enter Second Word - ").upper()
		result = input("Enter Result - ").upper()
		values = []
		visited = [False for x in range(10)]
		equation = [word1, word2, result]
		# Get Unique Words
		set = []
		for c in word1:
			if c not in set:
				set.append(c)
		for c in word2:
			if c not in set:
				set.append(c)
		for c in result:
			if c not in set:
				set.append(c)
		if len(set) > 10:
			print("\nNo Solution (as values will repeat)\n")
			exit()
		print("Solution Is - ")
		print(f" \t{word1}\n+\t{word2}\n-------------\n\t{result}\n\n")
		self.solve(set, values, visited, equation)
	def solve(self, letters, values, visited, equation):
		if len(letters) == len(values):
			map = {}
			for letter, val in zip(letters, values):
				map[letter] = val
			if map[equation[0][0]] == 0 or map[equation[1][0]] == 0 or map[equation[2][0]] == 0:
				return
			word1, word2, res = "", "", ""
			for c in equation[0]:
				word1 += str(map[c])
			for c in equation[1]:
				word2 += str(map[c])
			for c in equation[2]:
				res += str(map[c])
			if int(word1) + int(word2) == int(res):
				self.count += 1
				print(Fore.GREEN+f"Result {self.count} = {word1} + {word2} = {res}\n")
				solved = True
			return
		for i in range(10):
			if not visited[i]:
				visited[i] = True
				values.append(i)
				self.solve(letters, values, visited, equation)
				values.pop()
				visited[i] = False

print(Fore.GREEN+"\t\t\t\tConstraint Satisfaction")
print("1. Map Coloring\n2. Cryptarithmetic\n")
choice = int(input("\nEnter Choice - "))
if choice == 1:
	temp = map_coloring()
	temp.start()
elif choice == 2:
	temp = cryptarithmetic()
	temp.start()