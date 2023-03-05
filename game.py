from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()


while michelangelo.health > 0 and jack_sparrow.health > 0:
    response = ""
    while not response == "A" and not response == "B":
        response = input("Who do you want to be? A) Ninja B) Pirate \nResponse:")
        if response == "A":
            response =""
            while not response == "1" and not response == "2":
                response = input("What do you want Ninja to do? 1)Attack 2)Karatedojo Attack \nAction:")
                if response == "1":
                    michelangelo.attack(jack_sparrow)
                elif response == "2":
                    michelangelo.karatedojoattack(jack_sparrow)
                else:
                    print("Please choose 1 or 2")
            dice_roll = random.randint(1,2)
            if dice_roll == 1:
                jack_sparrow.attack(michelangelo)
            else:
                jack_sparrow.pirateattack(michelangelo)


        elif response == "B":
            response =""
            while not response == "1" and not response == "2":
                response = input("What do you want Pirate to do? 1)Attack 2)Pirate Attack \nAction:")
                if response == "1":
                    jack_sparrow.attack(michelangelo)
                elif response == "2":
                    jack_sparrow.pirateattack(michelangelo)
                else:
                    print("Please choose 1 or 2")
            dice_roll = random.randint(1,2)
            if dice_roll == 1:
                michelangelo.attack(jack_sparrow)
            else:
                michelangelo.karatedojoattack(jack_sparrow)
        else:
            print("Please choose A or B")

            