def getProfit(arr,rate,years):
    if len(arr)==0 or years<1 or rate<=0:
        print("The input is invalid")
        
    else:
        change=90
        for i in arr:
            new_price= i*((1+(rate/100))**years)
            change+=(new_price-i)
            
        print(change)
        
    
getProfit([10000,2130320,123020],10,4)
