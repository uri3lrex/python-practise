import random

bankofall= ['following','insecurity','princely', 'jester','king','queen','court', 'soldiers']
word= random.choice(bankofall)

gameword= ['_']* len(word)

total_attempts= 7;

hangman_stages = [
    '''
       -----
       |   |
           |
           |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
           |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    '''
]

hang_count= 0

while total_attempts>0:

    print('\nCurrent word: ' + ' '.join(gameword)); #use \n to go to next line while join parses any iterable or array into a string
    guess= input('Guess a letter: ')
    if guess in word:
     for i in range(len(word)):
       if word[i] == guess:
          gameword[i] = guess
          print('Great guess!')
    else:
      total_attempts= total_attempts-1
      hang_count= hang_count+1
      print('\n' + ' '.join(hangman_stages[hang_count]))
      print('\nWrong guess! Attempts left: '+ str(total_attempts));
    if '_' not in gameword:
      print('\nYou did it! The word is: ' + word);
      break
else:
      print(hangman_stages[6])
      print('\nYou have failed! Your word  was: ' + word )

 