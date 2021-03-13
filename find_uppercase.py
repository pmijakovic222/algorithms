input_str_1 = "JaSamPetar"
input_str_2 = "jaSamPetar"
input_str_3 = "jasampetar"

#iterative
def iterative(input_str):
	for i in range(len(input_str)):
		if input_str[i].isupper():
			return input_str[i]
	return "No uppercase found"

print(iterative(input_str_1))
print(iterative(input_str_2))
print(iterative(input_str_3))

#recursive
def recursive(input_str, idx=0):
	if input_str[idx].isupper():
		return input_str[idx]
	if idx == len(input_str) - 1:
		return "No uppercase found"
	else:
		return recursive(input_str, idx + 1)

print(recursive(input_str_1))
print(recursive(input_str_2))
print(recursive(input_str_3))