import sys
from PIL import Image,ImageOps


if sys.argv[1][-4:].lower()!=".jpg" and sys.argv[1][-4:].lower()!="jpeg" and sys.argv[1][-3:].lower()!=".png" and sys.argv[2][-4:]!=".jpg"and sys.argv[2][-4:]!="jpeg"and sys.argv[2][-3:]!=".png":
    sys.exit("Invalid input")
elif sys.argv[1][-3:]!=sys.argv[2][-3:]:
    sys.exit("Input and Output have different extensions")
elif len(sys.argv)==3:
        try:
             img=Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist")
        shirt=Image.open("shirt.png")
        size=shirt.size
        muppet=ImageOps.fit(img,size)
        muppet.paste(shirt,shirt)
        muppet.save(sys.argv[2])
        sys.exit(0)
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments")