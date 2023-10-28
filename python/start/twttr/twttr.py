sentence=input("Input: ")

def shorten(a):
    b=a
    letters=["a","e","i","o","u","A","E","I","O","U"]
    for i in letters:
        b=b.replace(i,"")
    return b
    
sentence=shorten(sentence)
print(f"Output: {sentence}")