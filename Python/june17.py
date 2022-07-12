n= int(input("Enter amount: "))

if n>1500 and n<=3000:
    discount= n*0.05
    
elif n>3000 and n<=5000:
    discount= n*0.1
    
elif n<=1500:
    discount=n*0
    
else:
    discount= n*0.15
    
print("The amount previously was", n)
print("the discount applicable is", discount)
print("The final amount is", n-discount)
