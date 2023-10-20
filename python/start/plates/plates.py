
def main():
    plate = input("Plate: ")
    length=len(plate)
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(plate)>1 and len(plate)<=6:
        if plate[0:2].isalpha():
            for i in range(len(plate)):
                if plate[i].isalpha()==False:
                        if plate[i]!=0:
                            return True
                        else:
                            return False
        else:
            return False
    else:
        return False
    


main()