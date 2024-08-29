#start with greeting
#give the user an inventory to work with along with a choice command
#give the player their HP and SP points (sword uses HP: 25 while Magic Book uses SP : 10)
#define damage in terms of LARGE=75, NORMAL=50, SMALL=25, BLOCK=0, MISS=0
#define four enemy types 
#1-phy(weak), magic(strong)- TOTAL HP: 100; resources:5, hp gained:35, sp gained: 35
#2- phy(weak), magic(weak)- TOTAL HP: 75; resources:3,  hp gained: 30, sp gained: 10
#3- phy(strong),magic (strong) [insert random crit to deal LARGE]-TOTAL HP: 150, hp gained: 70, sp gained: 45
#4- phy(strong), magic(weak)- TOTAL HP: 100  hp gained: 45, sp gained: 20
#let the enemy have resources for repairing
#revive player if they lost a fight

import random

# Define constants for the game
HP = 200
SP = 100
SWORD = 25
BOOK = 10
LARGE = 75
NORMAL = 40
SMALL = 25
BLOCK = 0
MISS = 0
FLEE_HP = 10
FLEE_SP = 5

# Monster attack values
mLARGE = 60
mSMALL = 20

# Print game introduction
print(r"""
RRRR   PPPP   GGG  
R   R  P   P G     
RRRR   PPPP  G  GG 
R  R   P     G   G 
R   R  P      GGG  
""")

print("\nWELCOME CHOSEN WARRIOR!")
name = input("Please insert your name: ")

print("\nThere was once a fellow warrior named " + name + " who roamed the great fields of RPG land. They were sent on a quest by the High King to defeat the four villains that terrorized their prosperous lands.")
print("\nThey were called: THE HOT HEADED RAM!")
print("THE MANY LEGGED FLY!")
print("THE DECEITFUL SNAKE!")
print("And their leader: THE UNDEFEATABLE DRAGON!")

choice = input("\nAre we ready to start this epic adventure? (Type Y for Yes and N for No): ")

if choice == "N":
    print("Very well " + name + ", we shall see you again some day...")
    exit()
elif choice != "Y":
    print("Invalid choice. Please restart the game.")
    exit()

print("\nYour health is: " + str(HP) + " and your Spirit points are: " + str(SP))
print("Defeat the monsters by exploiting their weaknesses with your sword (that uses HP) points and your magic book (that uses SP)! Remember to keep an eye on your health and SP points!")
print("This is an easy game BTW")

# Game loop
while HP > 0:
    print("\n" + name + " has set forth on their adventure again!")
    print("\nThey encounter:")

    villain = random.randint(1, 4)
    #villain=4 #test case
    run = 0

    if villain == 1:
        print(r"""
    /\\  /\\
   {  o  o }
   |  \__/  |  Roar! I am the Ram Monster!
    \      /
     \    /
     /    \ 
    (______)  
""")
        ram = 100

        while HP > 0 and ram > 0:
            print("\nStrengths: Physical (HP) \t Weaknesses: Magic (SP)")
            print("Your choices:")
            print("1. |ATTACK| (SWORD: -25 HP) \t2. |CAST A SPELL| (MAGIC BOOK: -10 SP)")
            print("3. |BLOCK| (-5 HP) \t4. |FLEE| (-10 HP, -5 SP)")
            method = int(input("What will you do ---> "))

            if method == 1:
                if HP >= SWORD:
                    ram -= SMALL
                    HP -= SWORD
                    print("You attack with your sword!")
                else:
                    print("You are too weak to attack with your sword!")
            elif method == 2:
                if SP >= BOOK:
                    ram -= LARGE
                    SP -= BOOK
                    print("You use a spell from your book!")
                else:
                    print("The book can't read your magic level!")
            elif method == 3:
                HP -= BLOCK
            elif method == 4:
                HP -= FLEE_HP
                SP -= FLEE_SP
                run += 1
                print("You flee from the battle!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
                    
            print("\nThe monster's health is now: "+ str(ram))
            # Enemy attacks if not fleeing
            if run == 0 and ram > 0:
                fate = random.choice([mLARGE, mSMALL, mSMALL, mSMALL])
                if fate == mLARGE:
                    HP -= mLARGE
                    print("\nThe RAM releases a mighty roar before charging you at full speeds!")
                else:
                    HP -= mSMALL
                    print("\nThe RAM bashes his hooves against your body, sending you reeling!")
                print("Your health is now: " + str(HP))
            elif run != 0 and ram > 0:
                print("\nThe RAM rushes at you as you try to escape, injuring you in the process.")
                HP -= FLEE_HP
                SP -= FLEE_SP
                break

            if ram <= 0:
                print("\nYou have defeated the Hot-Headed Ram Monster! Perhaps it will learn to control its anger one day...")
                HP+= 35
                SP+=35
                break

    elif villain == 2:
        print(r"""
      _     _
     / \~~~/ \
   ,----(     . . )  Bzzzz! I am the Insect Monster!
  /      \_  (   x ) 
 /|  |     | (    /  
^  ^  ^    ^ ^--^
""")

        insect = 75

        while HP > 0 and insect > 0:
            print("\nStrengths: NONE \t Weaknesses: Magic (SP), Physical (HP)")
            print("Your choices:")
            print("1. |ATTACK| (SWORD: -25 HP) \t2. |CAST A SPELL| (MAGIC BOOK: -10 SP)")
            print("3. |BLOCK| (-5 HP) \t4. |FLEE| (-10 HP, -5 SP)")
            method = int(input("What will you do ---> "))

            if method == 1:
                if HP >= SWORD:
                    insect -= LARGE
                    HP -= SWORD
                    print("You attack with your sword!")
                else:
                    print("You are too weak to attack with your sword!")
            elif method == 2:
                if SP >= BOOK:
                    insect -= LARGE
                    SP -= BOOK
                    print("You use a spell from your book!")
                else:
                    print("The book can't read your magic level!")
            elif method == 3:
                HP -= BLOCK
            elif method == 4:
                HP -= FLEE_HP
                SP -= FLEE_SP
                run += 1
                print("You flee from the battle!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

            print("\nThe monster's health is now: "+ str(insect))        
            # Enemy attacks if not fleeing
            if run == 0 and insect > 0:
                fate = random.choice([mSMALL, mSMALL, mSMALL, mSMALL, mLARGE])
                if fate == mLARGE:
                    HP -= mLARGE
                    print("\nThe insect stings you with a powerful venom!")
                else:
                    HP -= mSMALL
                    print("\nThe insect's bite is minor but still hurts!")
                print("Your health is now: " + str(HP))

            if insect <= 0:
                print("\nYou have defeated the Many-legged Insect! What a pushover...")
                HP+=30
                SP+=10
                break

    elif villain == 3:
        print(r"""
         /^\/^\ 
       _|__|  O|
 \/     /~     \_/ \
  \____|__________/  \
        \_______      \
               `\     \                
                 |     |     Ssssss! I am the Snake Monster!
                /      /
               /     / 
              /      /
             /     / 
            /_____/  
""")

        snake = 100

        while HP > 0 and snake > 0:
            print("\nStrengths: Magic (SP) \t Weaknesses: Physical (HP)")
            print("Your choices:")
            print("1. |ATTACK| (SWORD: -25 HP) \t2. |CAST A SPELL| (MAGIC BOOK: -10 SP)")
            print("3. |BLOCK| (-5 HP) \t4. |FLEE| (-10 HP, -5 SP)")
            method = int(input("What will you do ---> "))

            if method == 1:
                if HP >= SWORD:
                    snake -= NORMAL
                    HP -= SWORD
                    print("You attack with your sword!")
                else:
                    print("You are too weak to attack with your sword!")
            elif method == 2:
                if SP >= BOOK:
                    snake -= LARGE
                    SP -= BOOK
                    print("You use a spell from your book!")
                else:
                    print("The book can't read your magic level!")
            elif method == 3:
                HP -= BLOCK
            elif method == 4:
                HP -= FLEE_HP
                SP -= FLEE_SP
                run += 1
                print("You flee from the battle!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

            print("\nThe monster's health is now: "+ str(snake))        
            # Enemy attacks if not fleeing
            if run == 0 and snake > 0:
                fate = random.choice([mLARGE, mSMALL, mSMALL])
                if fate == mLARGE:
                    HP -= mLARGE
                    print("\nThe Snake strikes with a venomous bite!")
                else:
                    HP -= SMALL
                    print("\nThe Snake's attack is swift but not too damaging!")
                print("Your health is now: " + str(HP))

            if snake <= 0:
                print("\nYou have defeated the Deceitful Snake! Perhaps it just needs a friend?")
                HP+=45
                SP+=20
                break

    elif villain == 4:
        print(r"""
        /^\/^\
      _|__|  O|
\/     /~     \_/ \
 \____|__________/  \
      \_______      \
              `\     \                 \
                |     |                  \
               /      /                    \
              /     /                       \\
             /      /                         \ \\
            /     /                            \  \\
           /_____/                              \____\
            Roar! I am the Dragon Monster!
""")

        dragon = 120

        while HP > 0 and dragon > 0:
            print("\nStrengths: Physical (HP) \t Weaknesses: Magic (SP)")
            print("Your choices:")
            print("1. |ATTACK| (SWORD: -25 HP) \t2. |CAST A SPELL| (MAGIC BOOK: -10 SP)")
            print("3. |BLOCK| (-5 HP) \t4. |FLEE| (-10 HP, -5 SP)")
            method = int(input("What will you do ---> "))

            if method == 1:
                if HP >= SWORD:
                    dragon-= random.choice([SMALL, SMALL, NORMAL])
                    HP -= SWORD
                    print("You attack with your sword!")
                else:
                    print("You are too weak to attack with your sword!")
            elif method == 2:
                if SP >= BOOK:
                    dragon-= random.choice([SMALL, SMALL, NORMAL])
                    SP -= BOOK
                    print("You use a spell from your book!")
                else:
                    print("The book can't read your magic level!")
            elif method == 3:
                HP -= BLOCK
            elif method == 4:
                HP -= FLEE_HP
                SP -= FLEE_SP
                run += 1
                print("You flee from the battle!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

            print("\nThe monster's health is now: "+ str(dragon))        
            # Enemy attacks if not fleeing
            if run == 0 and dragon > 0:
                fate = random.choice([mLARGE, mLARGE, mSMALL,mSMALL])
                if fate == mLARGE:
                    HP -= mLARGE
                    print("\nThe Dragon breathes fire at you!")
                else:
                    HP -= mSMALL
                    print("\nThe Dragon attacks you with its claws!")
                print("Your health is now: " + str(HP))

            if dragon <= 0:
                print("\nYou have defeated the Undeafeatable Dragon! You are a master at this game :)")
                break

    # Check if player is still alive
    if HP <= 0:
        print("\nYou have been defeated by the villain. Reviving...")
        HP = 200
        SP = 100
        continue

    # Prompt to continue or end the game
    choice = input("\nDo you want to continue? (Y/N): ")
    if choice.upper() != "Y":
        print("\nSee you again, " + name + "!")
        HP+=70
        SP+=45
        break
