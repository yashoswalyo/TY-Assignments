import random
from time import sleep
compiterMove = 'X'
userMove = 'O'
flag = 0
class Magic():
	def __init__(self) -> None:
		self.board = ['_','_','_','_','_','_','_','_','_']
		self.magicSquare = [2,7,6,9,5,1,4,3,8,]
		self.remainingMovies = [2,7,6,9,5,1,4,3,8,]
		self.humanMoves = [0]
		self.machineMoves = [0]
		pass

	def showBoard(self):
		a = 0
		for i in range(3):
			print(self.board[a], self.board[a+1], self.board[a+2] )
			a+=3

	def showMagicSquare(self):
		a = 0
		print("\n")
		print("Remaining Positions: ")
		for i in range(3):
			print(self.magicSquare[a], self.magicSquare[a+1], self.magicSquare[a+2] )
			a+=3
		umove = int(input("\n Enter your Move: "))
		return umove

	def humanMove(self,vertex):
		if vertex not in self.humanMoves or vertex not in self.machineMoves:
			self.board[self.magicSquare.index(vertex)] = userMove
			self.magicSquare[self.magicSquare.index(vertex)] = '-'
			self.humanMoves.append(vertex)
			self.remainingMovies.remove(vertex)
		else: print("Move not Valid")
		return

	def machineMove(self,vertex):
		if vertex not in self.humanMoves or vertex not in self.machineMoves:
			global flag

			if len(self.humanMoves) > 2:
				l=1
				h=len(self.humanMoves)-1
				if 15-(self.humanMoves[l]+self.humanMoves[h]) in self.remainingMovies:
					vertex = 15-(self.humanMoves[l]+self.humanMoves[h])
					flag = 0
			if len(self.machineMoves) > 2:
				l=1
				h=len(self.machineMoves)-1
				if 15-(self.machineMoves[l]+self.machineMoves[h]) in self.remainingMovies:
					vertex = 15-(self.machineMoves[l]+self.machineMoves[h])
					flag = 1
			
			self.board[self.magicSquare.index(vertex)] = compiterMove
			self.magicSquare[self.magicSquare.index(vertex)] = '-'
			self.machineMoves.append(vertex)
			self.remainingMovies.remove(vertex)
		return

if __name__ == '__main__':
	obj = Magic()
	ch = input("Who will play first ( H=Human / M=Machine ): ")

	while(1):
		if ch in ['H' , 'h']:
			userMove = "X"
			compiterMove = "O"
			umove = obj.showMagicSquare()
			obj.humanMove(umove)
			obj.showBoard()
			obj.machineMove(random.choice(obj.remainingMovies))
			print("\nMachine turn")
			sleep(1)
			obj.showBoard()
			if flag == 1:
				print("Machine Won")
				exit(0)

		if ch in ['M' , 'm']:
			print("\nMachine turn")
			obj.machineMove(random.choice(obj.remainingMovies))
			obj.showBoard()
			if flag == 1:
				print("Machine Won")
				exit(0)
			umove = obj.showMagicSquare()
			sleep(1)
			obj.humanMove(umove)
			obj.showBoard()
