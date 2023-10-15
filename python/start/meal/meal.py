
def main():
    time=input("time? ")
    p1=convert(time)
    if p1>=7.0 and p1<=8.0:
        print("breakfast time")
    elif p1>=12.0 and p1<=13.0:
        print("lunch time")
    elif p1>=18.0 and p1<=19.0:
        print("dinner time")

def convert(time):
    partx, party = time.split(":")
    party=float(party)/60
    partx=float(partx)
    return partx+party


if __name__ == "__main__":
    main()