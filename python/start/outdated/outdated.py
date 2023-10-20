months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def calc(date2):
    x="0"
    if str(date2).find(" ")!=-1:
        date2=date2.strip(" ")
    if int(date2)<10:
        date2=str(date2)
        return x+date2
    else:
        date2=str(date2)
        return date2

def contr():
    while True:
        try:
            date=input("Date: ")
            if date.find("/")==-1:
                blank=date.find(" ")
                blank2=date.rfind(" ")

                month=date[:blank]
                day=date[blank+1:blank2-1]
                year=date[blank2:]

                month=months.index(month)+1

                month=calc(month)
                day=calc(day)
                year=calc(year)

                if int(month)>12 or int(day)>31 or date.find(",")==-1:
                    contr()

                print(year+"-"+month+"-"+day)
                break
            else:
                slash=date.find("/")
                slash2=date.rfind("/")

                month=date[:slash]
                day=date[slash+1:slash2]
                year=date[slash2+1:]
                
                month=calc(month)
                day=calc(day)
                year=calc(year)
                    
                if int(month)>12 or int(day)>31:
                    contr()

                print(year+"-"+month+"-"+day)
                break
                
        except :
            pass

contr()