import sys
import csv

after=[]

if sys.argv[1][-3:]!="csv" or sys.argv[2][-3:]!="csv":
    sys.exit("Not a CSV file")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
else:
        try:
            with open(sys.argv[1]) as file:
                lines = csv.DictReader(file)
                for row in lines:
                    name=row["name"].split(",")
                    after.append({"first":name[1].lstrip(),"last":name[0],"house":row["house"]})
            with open(sys.argv[2],"w") as file:
                writer=csv.DictWriter(file,fieldnames=["first","last","house"])
                writer.writerow({"first":"first","last":"last","house":"house"})
                for row in after:
                    writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})
        except FileNotFoundError:
            sys.exit("File does not exist")