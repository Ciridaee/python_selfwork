import random
import sys

def main():
        levell=level()
        guess=random.randint(1, levell)
        while True:
            if control(guess):
                break
            else:
                pass
        print("Just right!")
        sys.exit(1)
        
def level():
    while True:
        try:
            level=int(input("Level: "))
            if level<1:
                pass
            else:
                return level
        except:
            pass
        
def ans():
    while True:
        try:
            ans=int(input("Guess: "))
            if ans<1:
                pass
            else:
                return ans
        except:
            pass

def control(guess):
    while True:
        anss=ans()
        if anss<guess:
            print("Too small!")
            pass
        elif anss>guess:
            print("Too large!")
            pass
        else:
            return True


main()