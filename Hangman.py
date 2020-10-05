import random as rd
import datetime
import string
import datetime

# Please go to line 482 to skip the word dictionary list, the script begin on line 482

# Init the game with our word bank


word_bank = """Adult

Aeroplane

Air

Aircraft Carrier

Airforce

Airport

Album

Alphabet

Apple

Arm

Army

Baby

Baby

Backpack

Balloon

Banana

Bank

Barbecue

Bathroom

Bathtub

Bed

Bed

Bee

Bible

Bible

Bird

Bomb

Book

Boss

Bottle

Bowl

Box

Boy

Brain

Bridge

Butterfly

Button

Cappuccino

Car

Car-race

Carpet

Carrot

Cave

Chair

Chess Board

Chief

Child

Chisel

Chocolates

Church

Church

Circle

Circus

Circus

Clock

Clown

Coffee

Coffee-shop

Comet

Compact Disc

Compass

Computer

Crystal

Cup

Cycle

Data Base

Desk

Diamond

Dress

Drill

Drink

Drum

Dung

Ears

Earth

Egg

Electricity

Elephant

Eraser

Explosive

Eyes

Family

Fan

Feather

Festival

Film

Finger

Fire

Floodlight

Flower

Foot

Fork

Freeway

Fruit

Fungus

Game

Garden

Gas

Gate

Gemstone

Girl

Gloves

God

Grapes

Guitar

Hammer

Hat

Hieroglyph

Highway

Horoscope

Horse

Hose

Ice

Ice-cream

Insect

Jet fighter

Junk

Kaleidoscope

Kitchen

Knife

Leather jacket

Leg

Library

Liquid

Magnet

Man

Map

Maze

Meat

Meteor

Microscope

Milk

Milkshake

Mist

Money

Monster

Mosquito

Mouth

Nail

Navy

Necklace

Needle

Onion

PaintBrush

Pants

Parachute

Passport

Pebble

Pendulum

Pepper

Perfume

Pillow

Plane

Planet

Pocket

Post-office

Potato

Printer

Prison

Pyramid

Radar

Rainbow

Record

Restaurant

Rifle

Ring

Robot

Rock

Rocket

Roof

Room

Rope

Saddle

Salt

Sandpaper

Sandwich

Satellite

School

Sex

Ship

Shoes

Shop

Shower

Signature

Skeleton

Slave

Snail

Software

Solid

Space Shuttle

Spectrum

Sphere

Spice

Spiral

Spoon

Sports-car

Spot Light

Square

Staircase

Star

Stomach

Sun

Sunglasses

Surveyor

Swimming Pool

Sword

Table

Tapestry

Teeth

Telescope

Television

Tennis racquet

Thermometer

Tiger

Toilet

Tongue

Torch

Torpedo

Train

Treadmill

Triangle

Tunnel

Typewriter

Umbrella

Vacuum

Vampire

Videotape

Vulture

Water

Weapon

Web

Wheelchair

Window

Woman

Worm

X-ray"""
# Convert our word bank into a list
word_bank = list(word_bank.split("\n\n"))
# Shuffle our words.
rd.shuffle(word_bank)


# Essential function to find the average guess for all round
def getAverage(l):
    return sum(l) / len(l)


# Caesar shift function for intense mode
def caesar_encrypt(inp, shift):
    inp = inp.lower()
    letters = string.ascii_lowercase
    letters_shifted = letters[shift:] + letters[:shift]
    table = str.maketrans(letters, letters_shifted)
    return inp.translate(table)


# Welcome message
print("Welcome to Hangman! You have to guess a word letter by letter.")
print("You also have the option for an intense mode, trust me, you won't win.")
print("\n" + "First, let me know your name so I know how to address you.")

# Get user's name
name = str(input("My name is >> "))

# Get game round count
while True:
    try:
        game_count = int(input(f"Okay {name}, how many round(s) of game would you like to play? >> "))
        round_or_rounds = ["round", "rounds"]
        print(f"I see, you want to play {game_count} {round_or_rounds[0] if game_count == 1 else round_or_rounds[1]}.")
        break
    except ValueError:
        print(f"Not valid input, please try again {name}.")

# A list to store guess count for every game
all_guess_count = []
the_current_round = 0

# Create a copy of this variable so it won't be decremented after a round finishes
original_game_count = game_count

while game_count > 0:
    the_current_round += 1
    if the_current_round != original_game_count:
        print(f"\nRound {the_current_round} \n")
    else:
        print(f"\nRound {the_current_round} (Last Round) \n")
    # Let user decide on a word length
    while True:
        userDecideWordLength = str(input(f"Okay {name}, would you like to decide on a word length? (Y/N) >> ")).upper()
        if userDecideWordLength != "Y":
            if userDecideWordLength == "N":
                # Convert to a boolean of false if input is N
                userDecideWordLength = False
                break
            else:
                # Neither Y or N
                print(f"Hello {name}, I don't know what you want, can you input again?")
        else:
            # Y means True
            userDecideWordLength = True
            break

    # Let the user decide a word length, if they asked for it.
    if userDecideWordLength:
        while True:
            # Avoid invalid input
            try:
                length = int(input(f"Okay {name}, Please enter your desired word length >> "))
                break
            except ValueError:
                print("Not a valid input, please try again!")
    else:
        # Generate a random word length
        print(f"That's fine {name}. It's hard for me to decide too, but I think I've got it.")
        length = rd.randint(3, 13)
    # Filter all words in word bank that matches our length
    word = [w for w in word_bank if len(w) == length]

    # If word length is too big or too small, no word matched from the word bank, user have to input length again.
    while not word:
        # Keep trying if the user enters invalid input or no match again.
        while True:
            # Avoid invalid input
            try:
                print("No word found in the word bank. Please enter another desired length")
                length = int(input(f"Okay {name}, Please enter your desired word length (again) >> "))
                word = [w for w in word_bank if len(w) == length]
                break
            except ValueError:
                print("Nope, try again!")

    # Select a random word from our filtered list.
    word = rd.choice(word).lower().strip().replace("-", " ")

    # Extreme game mode selection
    while True:
        extreme_mode = str(input("Would like to try the intense mode? The word will be caesar shifted by today's day. (Y/N) >> ")).upper()
        if extreme_mode != "Y":
            if extreme_mode == "N":
                # Convert to a boolean of false if input is N
                extreme_mode = False
                break
            else:
                # Neither Y or N
                print(f"Hello {name}, I don't know what you want, can you input again?")
        else:
            # Y means True
            extreme_mode = True
            break

    # We will use today's day as the key for Caesar cipher.
    today_day = datetime.datetime.today().day

    if extreme_mode:
        key = today_day
        word = caesar_encrypt(word, key)

    print(f"\nI know the word now, it is your turn to guess. Good luck {name}!")

    # store all guessed chars
    all_guesses = ''
    # amount of guess
    guess_count = 0

    # Turns we give the user, you may adjust this
    turns = 12

    while turns > 0:
        print("\n")

        fail_count = 0

        # Separate the word by letter
        for char in word:
            if char in all_guesses:
                # If match, replace with the letter
                print(char, end="")
            else:
                print("\r".join("_"), end="")
                fail_count += 1

        if fail_count == 0:
            # Show the original word even if the word decrypted.
            # Decrypt the word by setting the key as negative.
            wordtype = [word.capitalize(), caesar_encrypt(word, -today_day).capitalize()]

            # Using the ternary operator if the word has been encrypted, show decrypted, else show the original word
            print(f"\nCongratulations, you win! The word is \"{wordtype[1] if extreme_mode else wordtype[0]}\", it took you {guess_count} tries.")

            # Finished the round, go to next round
            game_count -= 1

            # Append the guess count from this round to the total guess count, so we can calculate the average in the end.
            all_guess_count.append(guess_count)
            break

        guess_char = str(input(f"\nGuess {guess_count + 1} >> "))

        if guess_char in all_guesses:
            # If the user guessed the same char before
            print("You've already guessed this letter, try something else.\n")
        else:
            guess_count += 1

            # Avoid multiple entries
            if len(guess_char) > 1:
                guess_char = rd.choice(guess_char)
                print(
                    f"I see multiple entries, nice try, the game doesn't work this way, I am taking a random letter from "
                    f"that, and it is ... \"{guess_char}\"")

            # Append our letter to every letters we've guessed so so far
            # We convert to lower case because "a" and "A" are the same letter.
            all_guesses += guess_char.lower()

            # Print a message based-on if used guessed a correct letter or not
            if guess_char not in word:
                turns -= 1
                print("Wrong haha")

                # Plural or singular check
                turn_turns = ["turn", "turns"]
                print(f"{name}, you have {turns} {turn_turns[0] if turns == 1 else turn_turns[1]} left.")

                if turns == 0:
                    # User ran out of turns and has not guessed every character

                    # Show the original word even if the word decrypted.
                    # Decrypt the word by setting the key as negative.
                    wordtype = [word.capitalize(), caesar_encrypt(word, -today_day).capitalize()]

                    # Using the ternary operator if the word has been encrypted, show decrypted, else show the original word
                    print(f"You lost, the word was \"{wordtype[1] if extreme_mode else wordtype[0]}\"")
                    game_count -= 1
                    all_guess_count.append(guess_count)
                    break
            else:
                print(f"Nice one {name}, you've found a correct letter!")

    # The user finished all of their rounds.
    if game_count == 0:
        print(f"\nYou finished all of your rounds. Your average was guess per round was {int(getAverage(all_guess_count))}.\n")

# Goodbye message
print("\nPlay again to improve your score!")
print(f"Goodbye {name}, it was nice to meet you, hopefully we will meet again!")

# Prevent Python console from suddenly exiting without displaying the essential messages
input("\nPress any key to exit...")
