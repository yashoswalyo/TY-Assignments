from typing import List
def check_right(i, j, grid) -> tuple[int, int, int]:
	counter = 0
	while (counter + j) < len(grid[i]):
		if grid[i][j + counter] == ' ':
			counter += 1
		else:
			break
	if counter < 2:
		return None
	else:
		return (i, j, counter)
		
def check_down(i, j, grid) -> tuple[int, int, int]:
	counter = 0
	while (counter + i) < len(grid):
		if grid[i + counter][j] == ' ':
			counter += 1
		else:
			break
	if counter < 2:
		return None
	else:
		return (i, j, counter)
		
def get_across_slots(grid: list[str]):
	accross_slots = []
	i = 0
	while i < len(grid):
		j = 0
		while j < len(grid[i]):
			if grid[i][j] == ' ':
				if slot := check_right(i, j, grid):
					accross_slots.append(slot)
					j += slot[2]
			j += 1
		i += 1
	return accross_slots

def get_down_slots(grid: list[str]):
	t_grid = []
	# Get transpose of grid
	for i in range(len(grid)):
		string = ''.join([row[i] for row in grid])
		t_grid.append(string)
	down_slots = get_across_slots(t_grid)
	# The down slots are for the transposed grid,
	# so we need to convert them to our original grid's coordinates
	down_slots = [(slot[1], slot[0], slot[2]) for slot in down_slots]
	return down_slots
def start(across_words: list[str], down_words: list[str], grid: list[str]) -> list[str]:
	across_slots = get_across_slots(grid)
	down_slots = get_down_slots(grid)
	# We need a mutable grid, so we use list[list[str]]
	mut_grid = []
	for i in range(len(grid)):
		arr = []
		for j in range(len(grid[i])):
			arr.append([grid[i][j]])
		mut_grid.append(arr)
# Start filling the across words
	i = 0
	while len(across_words):
		used = False
		if used:
			across_slots.pop(i)
		else:
			i = (i + 1) % len(down_slots)
		if len(across_words[0]) == across_slots[i][2]:
			x, y, _ = across_slots[i]
			for counter, letter in enumerate(across_words[0]):
				mut_grid[x][y + counter] = [letter]
			else:
				used = True
			across_words.pop(0)
# Start filling the down words
	i = 0
	while len(down_words):
		used = False
		if used:
			down_slots.pop(i)
		else:
			i = (i + 1) % len(down_slots)
		if len(down_words[0]) == down_slots[i][2]:
			x, y, _ = down_slots[i]
			for counter, letter in enumerate(down_words[0]):
				mut_grid[x + counter][y] = [letter]
			else:
				used = True
			down_words.pop(0)
# Convert list[list[str]] to list[str]
	grid = []
	for i in range(len(mut_grid)):
		string = ""
		for j in range(len(mut_grid[i])):
			for k in range(len(mut_grid[i][j])):
				string += mut_grid[i][j][k][0]
		grid.append(string)
	return grid

def display_grid(grid: list[str]) -> None:
	for row in grid:
		for col in row:
			print(f"{col:>2}", end='')
		print()

def main():
	ACROSS = ['HYBRID', 'EARTH']
	DOWN = ['BREAD', 'HELMET']
	grid = [
	"########",
	"#      #",
	"# # ####",
	"# #     ",
	"# # ####",
	"# # ####",
	"# ######",
	]

	print(" The Initial Crossword is ".center(40, '='))
	display_grid(grid)
	print("The Across Words Are : ", ', '.join(ACROSS))
	print("The Down Words Are : ", ', '.join(DOWN))
	result = start(ACROSS, DOWN, grid)
	print('\n\n')
	print(" The Final Crossword is ".center(40, '='))
	display_grid(result)
main()
