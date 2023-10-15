line = input("Expression: ")
a=line.find(" ")
part1=float(line[:a])
part2=line[a+1:a+2]
part3=float(line[a+2:])
if part2=="+":
    print("{:.1f}".format(part1+part3))
elif part2=="/":
    print("{:.1f}".format(part1/part3))
elif part2=="*":
    print("{:.1f}".format(part1*part3))
elif part2=="-":
    print("{:.1f}".format(part1-part3))