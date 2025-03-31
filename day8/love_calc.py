def calculate_love_score(name1, name2):
    both_names = name1 + name2
    both_names = both_names.lower().replace(" ", "")
    first_number = 0
    second_number = 0
    for letter in both_names:
        if letter in "true":
            first_number += 1
        if letter in "love":
            second_number += 1
    total = str(first_number) + str(second_number)
    print(total)
    

calculate_love_score("Kanye West", "Kim Kardashian")