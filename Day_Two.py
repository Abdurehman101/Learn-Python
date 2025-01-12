#WAP to input user's first name & print uts length...
F_Name = input("Enter Your Firts Name: ")
print(len(F_Name))

#WAP to find the occurrence of '$' in a string..
check = "Nowdyas $ price increase day by day right now $ is 256$."
print(check.find("$"))
print(check.count("$"))

#Conditional Statements
marks = int(input("Enter the student marks:"))
if(marks>=90):
    print("Congrulation your grade is A")
elif(marks>=80 and marks<90):
    print("Congrulation your grade is B")
elif(marks>=70 and marks<80):
    print("Please Study Hard")
elif(marks<70):
    print("Grade D")
else:
    print("Please enter the Invalied number")           


#WAP to check if a number entered by the user is odd or even
check_Num = int(input("Enter The Number: "))
if(check_Num % 2 == 0):
    print("Number Is Even",check_Num)
else:
    print("Number Is Odd")    


#WAP to find the greatest of 3 numbers entered by the user
a = int(input("Enter The Number: "))
b = int(input("Enter The Number: "))
c = int(input("Enter The Number: "))

if(a>b and a>c):
    print("First number is largest",a)
elif(b>c):
    print("Second number is largest",b)
else:
    print("Largest Number is :",c)        


#WAP to check if a number is a multiple of 7 or not.
Num_1 = int(input("Enter A Number:"))
if(Num_1 % 7 == 0):
    print("Multiple Of 7")
else:
    print("Not Multiple of 7")    