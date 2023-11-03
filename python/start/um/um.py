import re
import sys
import string


def main():
    print(count(input("Text: ")))
    sys.exit(1)


def count(s):
    i=0
    c=s.translate(str.maketrans('', '', string.punctuation))
    words = c.split(" ")
    for a in words:
        if a.lower() == "um":
            i+=1
    return i




if __name__ == "__main__":
    main()