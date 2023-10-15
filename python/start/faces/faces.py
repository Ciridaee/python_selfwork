
def main():
    sentence = input()
    sentence=convert(sentence)
    print(sentence)

def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

main()