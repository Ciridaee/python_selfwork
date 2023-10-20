name=input("camelCase: ")
for i in range(0,len(name)):
    if name[i].isupper():
        name=name[:i]+"_"+name[i].lower()+name[i+1:]
        print(name)
    else:
        print(name)

