import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        return contr(s)

def contr(s):
    num1,num2=0,0
    strings=s.split(" ")
    if len(strings[0])==1:
        strings[0]="0"+strings[0]+":00"
    elif int[strings[0][0]]>1 and strings[0][1].isdigit() and strings[0][1]>2:
        raise ValueError
    if len(strings[3])==1:
        strings[3]="0"+strings[3]+":00"
    elif int[strings[3]]>12:
        raise ValueError
    if strings[1]=="PM":
        num1=int(strings[0][0:2])
        num1+=12
        num1=str(num1)+strings[0][2:5]
    else:
        num1=strings[0]
    if strings[4]=="PM":
        num2=int(strings[3][0:2])
        num2+=12
        num2=str(num2)+strings[3][2:5]
    else:
        num2=strings[3]
    new_hour=f"{num1} to {num2}"
    return new_hour



...


if __name__ == "__main__":
    main()
