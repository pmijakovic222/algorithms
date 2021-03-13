input_str = "pythoniscool"

print(len(input_str))

#iterative
def iterative(input_str):
	count = 0
	for i in input_str:
		count += 1
	return count

print(iterative(input_str))

#recursive
def recursive(input_str):
	if input_str == "":
		return 0
	return 1 + recursive(input_str[1:])

print(recursive(input_str))
