def cost():
	w = int(input("Enter the width of floor\n"))
	h = int(input("Enter the height of floor\n"))
	cost = int(input("Enter the cost of one tile\n"))
	print("One tile is 2 X 2 metre square")
	area = w*h
	no_of_tiles = area/2
	total_cost = no_of_tiles * cost
	print('Total cost incured $',total_cost)

def main():
	cost()

if __name__ == '__main__':
	main()