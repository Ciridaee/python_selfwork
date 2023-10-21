from pyfiglet import Figlet
import sys

if len(sys.argv)==1:
    random=True
elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
    random=False
else:
    print("Invalid usage")
    sys.exit(1)

figlet=Figlet()
figlet.getFonts()


if random==False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
elif random==True:
    figlet.setFont(font=random.choice(figlet.getFonts()))


sentence=input("Input: ")
print(figlet.renderText(sentence))