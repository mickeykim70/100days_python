print("The love calculator is calculating scores...")
name1 = input("What is your name? ")
name2 = input("What is your friend's name? ")

combined_name = name1 + name2
lowered_name = combined_name.lower()

t = lowered_name.count("t")
r = lowered_name.count("r")
u = lowered_name.count("u")
e = lowered_name.count("e")
l = lowered_name.count("l")
o = lowered_name.count("o")
v = lowered_name.count("v")
e = lowered_name.count("e")

first_digit = t + r + u + e
second_digit = l + o + v + e

score = int(str(first_digit)+ str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, AAA ~~~")
elif (score >= 40) or (score <= 50):
    print(f"Your score is {score}, BBB ~~~")
else:
    print(f"Your score is {score}. CCC ~~~")

 