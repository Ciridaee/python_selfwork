import random
import sys

def main():
    level=get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level<1 or level>3:
                pass
            else:
                return level
        except:
            pass

def generate_integer(level):
    if level==1:
        questions(1,1)
    elif level==2:
        questions(2,1)
    else:
        questions(3,1)

def questions(level,count):
    for a in range(1,10):
    
        i=1
        if level==1:
            num1=random.randint(0,9)
            num2=random.randint(0,9)
        elif level==2:
            num1=random.randint(10,99)
            num2=random.randint(10,99)
        else:
            num1=random.randint(100,999)
            num2=random.randint(100,999)
        num3=num1+num2
        usr=input(f"{num1} + {num2} = ")

        while True:
        
            cond=control(usr,num1,num2,num3,i)
            if cond==False:
                break
            else:
                count=count+1
                break
            
            cond=control(usr,num1,num2,num3,i)
            if cond==False:
                break
            else:
                count=count+1
                break
    print(f"Score: {count}")
    sys.exit(0)

def control(usrc,num1c,num2c,num3c,i):
        while True:
            try:
                if int(usrc)!=num1c+num2c:
                    print("EEE")
                    usrc=input(f"{num1c} + {num2c} =")
                    i=i+1
                    if i==3:
                        print("EEE")
                        print(f"{num1c} + {num2c} = {num3c}")
                        return False
                if int(usrc)==num1c+num2c:
                    return True
            except:
                print("EEE")
                usrc=input(f"{num1c} + {num2c} = ")
                i=i+1
                if i==3:
                    print("EEE")
                    print(f"{num1c} + {num2c} = {num3c}")
                    return False
                pass

if __name__ == "__main__":
    main()