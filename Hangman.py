import random

words = [
    'ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam',
    'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle',
    'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama',
    'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda',
    'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino',
    'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider',
    'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel',
    'whale', 'wolf', 'wombat', 'zebra'
]

figure = [
    r'''
  +---+
  |   |
      |
      |
      |
      |
  ========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
  ========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
  ========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
  ========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
  ========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
  ========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
  ========'''
]


word = random.choice(words)
length = len(word)
print(word)
quest = list(word)
print(quest)

guess =[]
for i in range(0, length):
    print("_", end="")
    guess.append("_")

letter_count = 0
count = 0

while guess != quest and count < 7:
    letter = input("\nEnter your guess for the letter: \n")

    # Check if the letter is in the word
    if letter in word:
        # Update the guessed letters
        for i, let in enumerate(word):
            if let == letter:
                guess[i] = letter
    else:

        print(figure[count])
        count += 1


    print("Current guess: " + "".join(guess))

if count == 7:
    print("GAME OVER! YOU LOST!")

else:
    print("CONGRATULATIONS! YOU WON THE GAME!")




