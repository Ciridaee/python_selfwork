def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 6>=len(s)>=2:
            
            if s.isalpha():
                return True
            
            elif s[0:2].isalpha() and s.isalnum():
                #isalnum alfabetik karakter olup olmadigini denetler

                for char in s:

                    if char.isdigit():

                        ind=s.index(char)

                        if s[ind:].isdigit() and int(char)!=0:
                            return True
                        else:
                            return False
    else:
        return False
    


if __name__ == "__main__":
    main()