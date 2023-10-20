food={}

while True:
    try:
        name=input()
        if name in food:  
            food[name]+=1
        else:
            food[name]=1
    except EOFError:
        food=sorted(food.items())
        for i in range(len(food)):
            print(f"{food[i][1]} {food[i][0].upper()}")
        break