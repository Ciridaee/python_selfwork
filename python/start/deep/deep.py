answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer=answer.lower()
if  answer=="forty-two" or answer=="forty two":
    print("Yes")
elif answer.find("42") is not -1:
    print("Yes")
else:
    print("No")