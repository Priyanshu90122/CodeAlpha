import random 
 
def hangman(): 
    words = ["python", "java", "swift", "javascript", "hangman", "programming","hello"] 
    word = random.choice(words) 
    guessed_word = ["_"] * len(word) 
    attempts = 6 
    guessed_letters = [] 
 
    print("Welcome to Hangman!") 
    print("Guess the word, one letter at a time.") 
 
    while attempts > 0: 
        print(f"\nWord: {' '.join(guessed_word)}") 
        print(f"Attempts left: {attempts}") 
        guess = input("Enter a letter: ").lower() 
 
        if guess in guessed_letters: 
            print("You already guessed that letter.") 
            continue 
 
        guessed_letters.append(guess) 
 
        if guess in word: 
            for i in range(len(word)): 
                if word[i] == guess: 
                    guessed_word[i] = guess 
            print(f"Good guess!") 
        else: 
            attempts -= 1 
            print(f"Wrong guess. You have {attempts} attempts left.") 
 
        if "_" not in guessed_word: 
            print(f"\nCongratulations! You guessed the word: {''.join(guessed_word)}") 
            break 
    else: 
        print(f"\nGame Over! The word was: {word}") 
 
hangman() 
 