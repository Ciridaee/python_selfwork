def main():
    greeting=input("Greeting: ")
    a=value(greeting)
    print(a)

def value(greeting):
    if greeting.lower().find("hello")>-1:
        return "$0"
    elif greeting.lower()[0]=="h":
        return "$20"
    else:
        return "$100"
    
if __name__ == "__main__":
    main()