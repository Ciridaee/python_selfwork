greeting=input("Greeting: ")

if greeting.lower().find("hello")>-1:
    print("$0")
elif greeting.lower()[0]=="h":
    print("$20")
else:
    print("$100")