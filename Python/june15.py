# conditional statements if, else and elif



#-----------------------------------------------------------------------------------------------------------------------------------#

a= int(input("Enter value a: "))

b= int(input('Enter value b: '))

print (a+b, type(a+b))

if a>b:
	print(a, " is greater than ", b)

elif a<b:
	print(b," is greatr than, ", a)

else:
	print("Both are equal")



#-----------------------------------------------------------------------------------------------------------------------------------#

# A calculator

a= int(input("Enter value a: "))

b= int(input('Enter value b: '))

o= input("What do you want to do with these numbers?: ")


if o=='+':
    print("The sum of the two numbers is: ",a+b)

elif o=='-':
    message= input("Are you ready for a negative answer?  yes/no:  ")
    if message=="yes":
        print("The difference of the two numbers is: ",a-b)
        
    elif message=='no':
        
        if a>b:
            print("The difference of the two numbers is: ",a-b)
        
        else:
            print("The difference of the two numbers is: ",b-a)
        
    
elif o=='*':
    print("The product of the two numbers is: ",a*b)

elif o=='/':
    print("The division of the two numbers is: ",a/b)

elif o=='//':
    print("The floor division of the two numbers is: ",a//b)    
    
else:
    print("Nope! Don't know how to do that mate! ")                                                                                                                                             
#---------------------------------------------------------------------------------------------------------------------------------#

