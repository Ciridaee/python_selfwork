def main():
    sentence=input("Input: ")
    sentence=shorten(sentence)
    print("Output: "+sentence)

def shorten(a):
    word_wo_v=""
    for letter in a:
        if not letter.lower() in ['a','e','i','o','u']:
            word_wo_v+=letter
    return word_wo_v
    
if __name__== "__main__":
    main()