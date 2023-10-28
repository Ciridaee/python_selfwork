def main():
    num3=int(round(control(),0))

    if num3>98:
        print("F")
    elif num3<2:
        print("E")
    else:
        print(f"{num3}%")
    


def control():
    while True:
        try:
            sentence=input("Fraction: ")
            a=sentence.find("/")
            num1=int(sentence[:a])
            num2=int(sentence[a+1:])
            if num1/num2<=1:
                return (num1/num2)*100
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


if __name__ == "__main__":
    main()