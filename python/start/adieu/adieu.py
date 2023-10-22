sentence="Adieu, adieu, to "
count=0
while True:
    try:
        name=input()
        count=count+1  
        if count==1:
            sentence=sentence+name
        elif count==2:
            sentence=sentence+" and "+name
        elif count==3:
            sentence=sentence.replace(" and",",")+", and "+name
        elif count>3:
            sentence=sentence.replace(", and",",")+", and "+name
         
    except EOFError:
        break

print(sentence)