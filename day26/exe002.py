sentence = input("Enter a sentence: ")

result = sentence.split()
print(result)

char_count = {word: len(word) for word in result}

print(char_count)
