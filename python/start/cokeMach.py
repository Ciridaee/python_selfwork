print("Hello, Coke's price is 50 cents. This machine accepts only 1,5,10,15,25,50 cent")
cokePrice=50
cokeChange=0
while True:
    money2=input("Please insert a coin: ")
    money=(int)(money2)
    if money !=1 and  money !=5 and  money !=10 and  money !=15 and  money !=25 and  money !=50:
        break

    cokePrice=cokePrice-money
    change=cokePrice
    if change <=0:
        cokeChange=change*(-1)
        break

acceptMoney=[[25,0],[15,0],[10,0],[5,0],[1,0]]
a=0
for i in range(5):
        if cokeChange>=acceptMoney[i][0]:
            cokeChange-=acceptMoney[i][0]
            acceptMoney[i][1]+=1
        
print(f"Change: {acceptMoney[0][1]}x{acceptMoney[0][0]}, {acceptMoney[1][1]}x{acceptMoney[1][0]}, {acceptMoney[2][1]}x{acceptMoney[2][0]}, {acceptMoney[3][1]}x{acceptMoney[3][0]}, {acceptMoney[4][1]}x{acceptMoney[4][0]}")