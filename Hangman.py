import random as rd

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

Money $$$$

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

# Welcome message
print("Welcome to Hangman! You have to guess a word letter by letter")
print("First, let me know your name so I know how to address you.")

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


def getAverage(l):
    return sum(l) / len(l)


# A list to store guess count for every game

all_guess_count = []
the_current_round = 0

while game_count > 0:
    the_current_round += 1
    print(f"\nRound {the_current_round}: \n")
    # Let user decide on a word length
    while True:
        userDecideWordLength = str(input(
            f"Okay {name}, would you like to decide on a word length? (Y/N) >> ")).upper()
        if userDecideWordLength != "Y":
            if userDecideWordLength.upper() == "N":
                userDecideWordLength = False
                break
            else:
                print(
                    f"Hello {name}, I don't know what you want, can you input again?")
        else:
            userDecideWordLength = True
            break
    # Let the user decide a word length.
    if userDecideWordLength:
        while True:
            try:
                length = int(
                    input(f"Okay {name}, Please enter your desired word length >> "))
                break
            except ValueError:
                print("Not a valid input, please try again!")
    else:
        # Generate a random word length
        print(
            f"That's fine {name}. It's hard for me to decide too, but I think I've got it.")
        length = rd.randint(1, 10)
    # Filter all words in word bank that matches our length
    word = [w for w in word_bank if len(w) == length]

    # If word length is too big or too small, no word was found match, user input length again.
    while not word:
        print("No word found in the word bank. Please enter another desired length")
        length = int(
            input(f"Okay {name}, Please enter your desired word length (again) >> "))
        word = [w for w in word_bank if len(w) == length]

    # Select a random word from our filtered list.
    word = rd.choice(word).lower().strip().replace("-", " ")

    print(
        f"\nI know the word now, it is your turn to guess. Good luck {name}!")

    all_guesses = ''
    guess_count = 0

    # Turns we give the user
    # You may adjust this
    turns = 12

    while turns > 0:
        fail_count = 0
        for char in word:
            if char in all_guesses:
                print(char, end="")
            else:
                print("_", end="")
                fail_count += 1

        if fail_count == 0:
            print(
                f"\nCongratulations, you win! The word is \"{word.capitalize()}\", it took you {guess_count} tries.")
            game_count -= 1
            all_guess_count.append(guess_count)
            break

        guess_char = str(input(f"\nGuess {guess_count + 1} >> "))
        if guess_char in all_guesses:
            print("You've already guessed this letter, try something else.")
        else:
            guess_count += 1

            # Avoid multiple entries
            if len(guess_char) > 1:
                guess_char = rd.choice(guess_char)
                print(
                    f"I see multiple entries, nice try, the game doesn't work this way, I am taking a random letter from "
                    f"that, and it is ... {guess_char}")

            # Append our letter to every letters we've guessed so so far
            all_guesses += guess_char

            # Print a message based-on if used guessed a correct letter or not
            if guess_char not in word:
                turns -= 1
                print("Wrong haha")
                print(f"{name}, you have {turns} turns left.")
                if turns == 0:
                    print(f"You lost, the word was \"{word.capitalize()}\"")
                    game_count -= 1
                    all_guess_count.append(guess_count)
                    break

    # The user finished all of their rounds.
    if game_count == 0:
        print(
            f"\nYou finished all of your rounds. Your average was guess per round was {int(getAverage(all_guess_count))}.\n")

# Goodbye message
print("\nPlay again to improve your score!")
print(f"Goodbye {name}, it was nice to meet you, hopefully we will meet again!")
