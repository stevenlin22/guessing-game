import random

play_again = 'z'
round_number = 0
number_of_guesses = 11
score_total = 0
score_multiplier = 1
threshold = 0
name = input("Enter your name. If you want to quit, enter 'q': ")

while True:
    score = number_of_guesses - 1
    randomnum = random.randint(1,100)
    if play_again == 'n':
        print("--------")
        print("womp womp you suck ahahahaha\nYour final score was only: ", score_total)
        break
    elif play_again == 'y':
        print("--------")
        print("Reloading time .......")
    round_number += 1
    low_guess = 0
    high_guess = 0
    if name == 'q':
        break
    else:
        print("--------")
        print("Beginning the game......")
        print("Welcome to round ", round_number)
        if round_number%10 == 0:
            threshold += 150
            if score_total >= threshold:
                number_of_guesses += 1
        elif round_number%5 == 0:
            number_of_guesses -= 1
        if round_number%2 == 0:
            score_multiplier += 0.5
        if number_of_guesses == 0:
            print("--------")
            print("Out of Guesses. Boing Boing Boing Bonk!\nYour final score was: ", score_total)
        for i in range(1,number_of_guesses):
            print("You have ",number_of_guesses-i," tries.")
            guess = int(input("Make a guess from 1-100: "))
            if guess == randomnum:
                if i == 1:
                    print("--------")
                    print("Concrajulashions,",name, "! You did it!!!!\nIt took you only",i, "try")
                    print(low_guess, "of your guesses were low, while", high_guess, "of your guesses were high")
                    score *= score_multiplier
                    score_total += score
                    print("Your scored: ", score,"\nYour multiplier is: ", score_multiplier, "\nYour total score is now: ", score_total)
                else:
                    print("--------")
                    print("Concrajulashions,",name, "! You did it!!!!\nIt took you only",i, "tries")
                    print(low_guess, "of your guesses were low, while", high_guess, "of your guesses were high")
                    score *= score_multiplier
                    score_total += score
                    print("Your scored: ", score,"\nYour multiplier is: ", score_multiplier, "\nYour total score is now: ", score_total)
                play_again = input("Would you like to continue? 'y' for Yes!! 'n' for nah: ")
                break
            elif guess < randomnum:
                print("--------")
                msgrdm = random.randint(1,8)
                if msgrdm == 1:
                    print("Too Low! Maybe guess higher or something idk hehehe")
                elif msgrdm == 2:
                    print("Wayyyyy too Low!!!! Try going higher idiot")
                elif msgrdm == 3:
                    print("Too low, try going higher pookie, you got this")
                elif msgrdm == 4:
                    print("A bit low, how are you even still alive? Go higher")
                elif msgrdm == 5:
                    print("Too low broski, you should like go higher or something")
                elif msgrdm == 6:
                    print("Low Blow!!! Blow me higher")
                elif msgrdm == 7 and guess != 6:
                    print("Maybe a tad bit low. You can go a bit higher, you got at least 1 more try")
                else:
                    print("You so low that the flames of hell are licking at your grippers. Climb that stair faster. Go Higher!")
                low_guess += 1
                score -= 1
            else:
                print("--------")
                msgrdm = random.randint(1,8)
                if msgrdm == 1:
                    print("Too High! Maybe guess lower or something idc, do whatever")
                elif msgrdm == 2:
                    print("Wayyyyy too high!!!! Holy fuck you are an idiot")
                elif msgrdm == 3:
                    print("Too high, try going lower a little bit pookie, you got this")
                elif msgrdm == 4:
                    print("A bit high, how did you even get through elemenatry math? Go lower")
                elif msgrdm == 5:
                    print("Too high brospecies, you should like go lower or something, that chillax you real good")
                elif msgrdm == 6:
                    print("Bro shot too high at the skies and fell into the ground. Try going lower, then you wouldn't miss")
                elif msgrdm == 7 and guess != 7:
                    print("Maybe a tad bit high. You can go a bit lower maybe, you got at least 1 more try so you got this")
                else:
                    print("You went so high a cop pulled you over for driving while being that high. Try not doing that. Go lower")
                high_guess += 1
                score -= 1
        if guess != randomnum:
            print("--------")
            print("OOOOOOOOF! Tough luck", name, ". You just suck m8. Do better. Be better. Rethink your life choices cause the number was ",randomnum)
            print(low_guess, "of your guesses were low, while", high_guess, "of your guesses were high")
            score_total += score
            print("Your scored: ", score,"\nYour multiplier is: ", score_multiplier, "\nYour total score is now: ", score_total)
            play_again = input("Would you like to continue? 'y' for not being a loser and keep rising up 'n' for being a sucker and giving up: ")