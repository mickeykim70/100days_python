sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split(" ")

letter_dict = {word:len(word) for word in sentence}

print(letter_dict)




