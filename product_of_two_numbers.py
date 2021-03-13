x = 5
y = 3

#iterative
def iterative(x, y):
	return x * y

print(iterative(x,y))

#recursive
def recursive(x, y):
	if x < y:
		x,y = y,x
	if y <= 0:
		return 0
	return x + recursive(x, y-1)

print(recursive(x,y))