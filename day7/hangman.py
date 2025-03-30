import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
for number in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()

display = ""
for letter in chosen_word:
    if letter == guess:
        print("Right")
        display += letter
    else:
        print("Wrong")
        display += "_"
print(display)