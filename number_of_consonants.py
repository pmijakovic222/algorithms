input_str_1 = "Abc de"
input_str_2 = "python"

#iterative
vowel = "aeiou"
def iterative(input_str):
	count = 0
	for i in input_str:
		if i.lower() not in vowel and i.isalpha():
			count += 1
	return count

print(iterative(input_str_1))
print(iterative(input_str_2))

#recursive
def recursive(input_str):
	if input_str == "":
		return 0
	elif input_str[0].lower() not in vowel and input_str[0].isalpha():
		return 1 + recursive(input_str[1:])
	else:
		return recursive(input_str[1:])

print(recursive(input_str_1))
print(recursive(input_str_2))