import copy
from math import nextafter
from colorama import Fore,Back,Style,init
init(autoreset=True)

class Puzzle():
	board = [
		[1,2,3],
		[0,4,6],
		[7,5,8]
	]
	goal = [
		[1,2,3],
		[4,5,6],
		[7,8,0]
	]
	startX = 0
	startY = 0
	queue = []
	generatedBoards = []

	def calcHeuristic(self,board):
		h = 0
		for i in range(3):
			for j in range(3):
				if board[i][j] != self.goal[i][j]:
					h = h+1
		return h-1
	
	def getValidMoves(self,board):
		for i in range(3):
			for j in range(3):
				if board[i][j] == 0:
					self.startX = j
					self.startY = i
		position = [0]*4
		validMoves = []
		position[0] = [self.startX+1,self.startY]
		position[1] = [self.startX-1,self.startY]
		position[2] = [self.startX,self.startY-1]
		position[3] = [self.startX,self.startY+1]
		for i in range(4):		
			if position[i][1]>-1 and position[i][1]<3 and position[i][0]>-1 and position[i][0]<3:
				validMoves.append(position[i])
		return validMoves
	
	def playMove(self, move:list, board:list):
		newBoard = copy.deepcopy(board)						# ©️ Yash Oswal
		temp = newBoard[move[1]][move[0]]
		newBoard[move[1]][move[0]] = newBoard[self.startY][self.startX]
		newBoard[self.startY][self.startX] = temp
		return newBoard

	def bestFirstSearch(self):
		self.calcHeuristic(self.board)
		self.queue.append((self.calcHeuristic(self.board), self.board)) 
		self.generatedBoards.append(self.board)
		i = 0
		while(1<1000):
			next = self.queue.pop()
			moves = self.getValidMoves(next[1])
			print('\n---------------\n')
			print(f"	step {i}\n")
			for j in range(3):
				print("	",next[1][j])
			if next[1] == self.goal:
				print(f"\nGoal state reached in {i} steps")
				print('\n------------------------------\n')
				exit(1)
			for move in moves:
				newBoard = self.playMove(move,next[1])
				if newBoard not in self.generatedBoards:
					self.generatedBoards.append(newBoard)
					self.queue.append((self.calcHeuristic(newBoard), newBoard))
					self.queue.sort(reverse=True) [(5,[])(4,[])(3,[])]
			i+=1
		return None

class Robot():
	table = [
		['-','-','-','-','-','-','-','-','-','-','-'],
		['-',Fore.YELLOW+'#','-','-','-',Fore.YELLOW+'#',Fore.YELLOW+'#',Fore.YELLOW+'#',Fore.YELLOW+'#',Fore.YELLOW+'#','-'],
		['-',Fore.YELLOW+'#',Fore.YELLOW+'#','-','-','-','-','-','-',Fore.YELLOW+'#','-'],
		['-','-',Fore.YELLOW+'#',Fore.YELLOW+'#',Fore.YELLOW+'#',Fore.YELLOW+'#',Fore.YELLOW+'#',Fore.YELLOW+'#',Fore.YELLOW+'#',Fore.YELLOW+'#','-'],
		['-','-','-','-','-','-','-','-','-','-','-']
	]
	goalX = 6
	goalY = 2
	startX = 0
	startY = 3	
	newTable = copy.deepcopy(table)
	queue = []
	visited = []

	def calcManhatten(self):
		self.table[self.startY][self.startX] = Fore.BLUE+'S'
		self.table[self.goalY][self.goalX] = Fore.RED+'G'
		print("\n Manhatten Distance: \n")
		for i in range(5):
			for j in range(11):
				if self.table[i][j]!=Fore.YELLOW+'#':
					self.newTable[i][j] = abs(self.goalX - j) + abs(self.goalY-i)
				print('\t',self.newTable[i][j], end='')
			print('\n')
		position = [self.startX,self.startY]
		self.queue.append((self.newTable[self.startY][self.startX],position))
		

	def getNeighbors(self):
		position = [0]*4
		value = [0]*4
		position[0] = [self.startX+1,self.startY]
		position[1] = [self.startX-1,self.startY]
		position[2] = [self.startX,self.startY-1]
		position[3] = [self.startX,self.startY+1]
		for i in range(4):			# ©️ Yash Oswal
			if position[i][1]>-1 and position[i][1]<5 and position[i][0]>-1 and position[i][0]<11:
				value[i] = self.newTable[position[i][1]][position[i][0]]
				if value[i] != Fore.YELLOW+'#' and ((value[i], position[i]) not in self.visited) :
					self.queue.append((value[i], position[i]))
		self.queue.sort(reverse=True)

	def bestFirstSearch(self):
		steps = 0
		while (self.queue) :
			input()
			print(f"Steps taken: {steps}")
			print(f"Queue: {self.queue}")
			next = self.queue.pop()
			print(f"Selecting: {next}")
			print(f"Current queue: {self.queue}")
			if next[1][0] == self.goalX and next[1][1] == self.goalY :
				print(f"Goal State reached in {steps} steps")
				exit(1)
			if next[1] == [self.startX,self.startY]:
				self.table[next[1][1]][next[1][0]] = Fore.BLUE+'S'
			else: 
				self.table[next[1][1]][next[1][0]] = Fore.GREEN+str(next[0])
			self.visited.append(next)
			self.startX = next[1][0]
			self.startY = next[1][1]
			self.getNeighbors()
			print(f"Adding neighbours of {next} to queue\nCurrent queue: {self.queue}\n")
			self.printTable(self.table)
			print('\t---------------------------------------------------------------------------------')
			steps+=1

	def printTable(self,table):
		for i in range(5):
			for j in range(11):
				print("\t"+Fore.WHITE+table[i][j], end='')
			print('\n')

class cityDistance():
	cityMap = {
	'Delhi' : [(800, 'Indore'),(1300, 'Kolkata')],
	'Indore': [(600, 'Mumbai'),(500, 'Nagpur'),(800,'Delhi')],
	'Kolkata': [(1200,'Nagpur'),(1500,'Hyderabad'),(1300,'Delhi')],
	'Mumbai': [(800,'Hyderabad'),(1000,'Bangalore'),(600,'Indore')],
	'Nagpur':[(500,'Indore'),(1200,'Kolkata'),(500,'Hyderabad')],
	'Hyderabad':[(800,'Mumbai'),(500,'Nagpur'),(1500,'Kolkata'),(500,'Bangalore')],
	'Bangalore':[(1000,'Mumbai'),(500,'Hyderabad')]
	} #based on ppt bfs cities distance problem

	hSLD = {
		'Delhi':0,
		'Indore':800,
		'Mumbai':1300,
		'Hyderabad':1500,
		'Bangalore':1800,
		'Nagpur':1000,
		'Kolkata':1300
	}

	queue = []
	open = []
	closed = []
	start = "Hyderabad"
	end = "Delhi"
	totalDistance = 0

	def expand(self,s:str):
		near_cities:list = self.cityMap.get(s)
		near_cities.sort(reverse=True)
		return near_cities
	
	def validMove(self,near_cities:list):
		distance = 0
		for city in near_cities:
			self.queue.append((self.hSLD.get(city[1]),city[1],city[0]))
			if city[1] not in self.closed:		# ©️ Yash Oswal
				self.open.append(city[1])
			if self.open.count(city[1])>1:
				self.open.remove(city[1])
		self.queue.sort(reverse=True)
		
	def bestFirstSearch(self):
		self.queue.append((self.hSLD.get(self.start),self.start,0))
		self.open.append(self.start)
		i = 0
		while(1):
			next:str = self.queue.pop()
			near_cities = self.expand(next[1])
			self.closed.append(next[1])
			self.totalDistance = self.totalDistance + int(next[2])
			self.validMove(near_cities)
			self.open.remove(next[1])
			print(f"\nOpen List: {self.open}\nClosed List: {self.closed}")
			if next[1] == self.end:
				print("Path Reached")
				print(f"Total Distance from {self.start} to {self.end}: {self.totalDistance} km")
				exit(1)
			i+=1

print("Select a problem(Best First Search): ")
print("1. 8-Puzzle")
print("2. Robot Navigation")
print("3. City Distance Problem")
ch = int(input("Enter your choice(1-3):"))

if ch == 1:
	print("[+]8 Puzzle")
	s = Puzzle()
	s.bestFirstSearch()
elif ch == 2:
	print('[+]Robot Navigation')
	s = Robot()
	s.calcManhatten()
	print('\n Current State:')
	s.printTable(s.table)
	s.bestFirstSearch()
elif ch == 3:
	print('[+]City Distance')
	s = cityDistance()
	s.bestFirstSearch()
else:	
	print("[-]Run again and enter valid choice")
	exit(1)
