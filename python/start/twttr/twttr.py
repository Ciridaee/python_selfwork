sentence=input("Input: ")
letters=["a","e","i","o","u","A","E","I","O","U"]
for a in letters:
    sentence=sentence.replace(a,"")
print(f"Output: {sentence}")