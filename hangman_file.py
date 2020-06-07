# generate a random word
from random_word import RandomWords


def word_generator():
    r = RandomWords()
    r.word_of_the_day()
    # Return a single random word
    random_word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1,
                                    maxCorpusCount=6, minDictionaryCount=1, maxDictionaryCount=6, minLength=4,
                                    maxLength=7)
    return random_word

#print(word_generator())


# turn word into list and remove middle letters:
def word_into_list(word):
    guess_word = [char for char in word]
    first_letter = guess_word[0]
    last_letter = guess_word[-1]
    new_list = []
    for char in word:
        if char == first_letter or char == last_letter:
            new_list.append(char)
        else:
            new_list.append("_")
    return (new_list)


random_word = word_generator()
#print(word_into_list(random_word), random_word)

hidden_word = word_into_list(random_word)


# input

def get_letter_index(guess):
    for letter in random_word:
        if letter == guess:
            index = random_word.index(guess)
            break
    return index


def hangman_game():
        print("This is a game of hangman. You have 10 chances to make a wrong guess \n Here is the word: " + str(hidden_word) + ".")
        counter = 0
        correct_counter = 0
        condition = "_" in hidden_word
        while counter < 10:
             if "_" not in hidden_word: #stops the game if the word is found
               print('You found the word with '+ str(counter+correct_counter)+ " tries remaining.")
               break
             letter = input("Try guessing a letter:")
             print('You guessed ' + letter)
             new = hidden_word
             if letter in random_word and letter != random_word[0] and letter !=random_word[-1]: #divide this into if and elif
                    print("correct")
                    correct_counter += 1
                    index = get_letter_index(letter)
                    #replacement
                    try:
                      new.remove('_')
                      new.insert(index, letter)
                    except ValueError:
                      pass
                    print(new)
             else:
                    counter += 1  # add strikes counter
                    print("incorrect. You have "+ str(10-counter)+ " more tries")
                    print(new)
        return "End of game. The word was: "+ random_word+ "."

#execute game
print(hangman_game())

#things i gotta fix: double letters in the middle of the word, first and last letter duplicates
