menu={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
newMenu={}
for key in menu.items():
    i=0
    name=key[i].lower()
    newMenu[name]=menu[key[i]]
    i==i+1

total=0
def sum():
    while True:
        try:
            item=input("Item: ").lower()
            if item in newMenu:
                global total
                total += newMenu[item]
                total2=format(total,".2f")
                print(f"${total2}")
        except EOFError:
            print()
            break
sum()