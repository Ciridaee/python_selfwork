def main():
    while True:
        fract = input("Fraction: ")
        try:
            perc = convert(fract)
            break
        except (ValueError, ZeroDivisionError):
             continue
        
    print(gauge(perc))


def convert(fract):
    while True:
        try:
            a, b = fract.split("/")
            a = int(a)
            b = int(b)
            f= a/b
            if f<=1:
                a=int(f*100)
                return a
            else:
                fract = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
            raise

def gauge(percent):
    if percent <=1:
        return 'E'
    elif percent >=99:
        return 'F'
    else:
        return str(percent) + '%'

if __name__ == "__main__":
    main()