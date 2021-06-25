guess_word = "PIZZA"
user_guess = "Z"

word_dict = {

}

for index,letter in enumerate(guess_word):
    word_dict[index] = letter

for i in range(len(word_dict)):
    if user_guess == word_dict[i]:
        print("letter correct")
