import random

with open("wordlist.txt") as file:
    file_words = file.read()
    wordlist = file_words.split()


def get_random(words):
    random_word = random.choice(words)
    return random_word


def check():
    w = ""
    length = input("Length of word (min = 2, max = 22): ")
    while len(w) != int(length):
        w = get_random(wordlist)
    else:
        return w


def game():
    word = check()
    hidden_word = []
    for i in word:
        hidden_word.append("_")
    wrong = 7
    while wrong > 0:
        if "_" in hidden_word:
            print(hidden_word)
            print("Guesses left: " + str(wrong))
            guess = input("Letter: ")
            if guess in word and not guess in hidden_word and len(guess) == 1:
                if word.count(guess) == 1:
                    index = word.index(guess)
                    hidden_word[index] = guess
                else:
                    for n in range(0, len(word)):
                        letter = word[n]
                        if guess == letter:
                            hidden_word[n] = guess
            else:
                wrong -= 1
        else:
            print("You win! The word was " + word + "!")
            break
    if wrong == 0:
        print("You lose! The word was " + word + "!")


game()
