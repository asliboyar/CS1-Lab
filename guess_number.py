import random
number=random.randint(0, 21)
def main():
    x=int(input('Guess a number one through twenty: '))
    if x == number:
        print("You got it!")
    elif x > number:
        print("too high")
        main()
    else:
        print("too low")
        main()
main()
