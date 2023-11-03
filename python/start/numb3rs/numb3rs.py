import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit(0)


def validate(ip):
    if re.search(".", ip) and ip.count(".") == 3:
        num1,num2,num3,num4 = ip.split(".")
        if num1.isdigit() and num2.isdigit() and num3.isdigit() and num4.isdigit():
            if int(num1) >= 0 and int(num1) <= 255 and int(num2) >= 0 and int(num2) <= 255 and int(num3) >= 0 and int(num3) <= 255 and int(num4) >= 0 and int(num4) <= 255:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

main()

if __name__ == "__main__":
    main()