import random
import math

score = 0
alphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
relations = [" is equal to ", " is different from "]
loop = True
answer = 0

print("Welcome to the Relational Frame Training Game")
print("This game trains your ability to make basic relationships")
print("to improve your learning skills\n")
print("Let's begin!\n")

def split():
    return alphabet[0][int(math.floor(random.random() * 26))]

def get_rel():
    return relations[int(math.floor(random.random() * 2))]

while loop:

    stat1 = split()+split()+split()
    comp = get_rel()
    stat2 = split()+split()+split()
    print(stat1+comp+stat2)

    print("\nWhat relation do {} and {} have?".format(stat1,stat2))
    answer = input("(write 1, 2, or 3) \n1: equal \n2: different \n3: quit\n")

    if (answer == "1" and comp == relations[0])or(answer == "2" and comp == relations[1]):
        score += 1
        print("Correct")
        print("score: {}".format(score))
        print("\n-----------------------------\n")
    elif (answer == "2" and comp == relations[0])or(answer == "1" and comp == relations[1]):
        score -= 1
        print("wrong")
        print("score: {}".format(score))
        print("\n-----------------------------\n")
    elif answer == 3:
        loop = False
    else:
        print("invalid answer")

print("\nYour total score was {}".format(score))
