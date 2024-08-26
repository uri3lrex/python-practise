import random

#first create the array which supports all the types of arcana
arcana_bank= ['fool','lovers', 'heirophant', 'emperor', 'justice']
arcana= random.choice(arcana_bank) #using the random library, a single answer can be chosen

chosen_guess= ['_']* len(arcana) #doing this will help us iniialize the lenth of whatever we are guessing as an answer

total_attempts= 10;

while total_attempts>0:

    print('\nCurrent arcana: ' + ' '.join(chosen_guess)); #use \n to go to next line while join parses any iterable or array into a string
    guess= input('Guess a letter: ')
    if guess in arcana:
     for i in range(len(arcana)):
       if arcana[i] == guess:
          chosen_guess[i] = guess
          print('Great guess!')
    else:
      total_attempts= total_attempts-1;
      print('Wrong guess! Attempts left: '+ str(total_attempts));
    if '_' not in chosen_guess:
      print('\nThe arcana is the means by which all is revealed! Your arcana is: ' + arcana);
      break
else:
      print('\nYou have failed! Your arcana was: ' + arcana + '! Soon the world will come into ruin...')

 