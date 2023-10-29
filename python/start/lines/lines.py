import sys
if len(sys.argv)<=1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith('.py')==False:
    sys.exit("Not a Python file")
else:
    try:
        file = open(sys.argv[1],'r')
        lines = file.readlines()
        lenn=len(lines)-1
        i=0
        for line in lines:
            if line.isspace()==True:
                continue
            if line.lstrip().startswith("#"):
                continue
            else:
                i=i+1
                
        file.close()
        print(i)
    except:
        sys.exit("File does not exist")