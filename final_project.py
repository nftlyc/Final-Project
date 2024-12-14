# My python function


def activity1():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            print ("\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\b***\n\t\t\t\t\t\t\t\b\b*****\n\t\t\t\t\t\t\t\b\b\b*******\n\t\t\t\t\t\t\t\b\b*****\n\t\t\t\t\t\t\t\b***\n\t\t\t\t\t\t\t*")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")
        
def activity2():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            name = input ("Please type your name ==> ")

            print("Hi" +  name) 
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity3():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            fullname = input (" What is your name? ")
            age = input (" How old are you? ")
            mobilenumber = input (" What is your mobile number? ")
            email = input (" Email: ")
            gender = input (" Sex: ")
            dateofbirth = input (" Date of birth: ")
            placeofbirth = input (" Where were you born? ")
            maritalstatus = input (" Is married? true or false ")
            religion = input (" Religion: ")
            languagesknown = input (" Languages known: ")
            address = input (" Address: ")

            print ("Hi, my name is " + fullname + " and I'm " , age , " years old " , gender , " \nI live in " + address + " \nmy phone number is " , mobilenumber , " and this is my email " + email + " \nI was born on " , dateofbirth , " in " + placeofbirth + " \nIt is " , maritalstatus ," that i'm married \nMy religion is " + religion + " and " + languagesknown + " is tha language that i can speak")

    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity4():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            number1 = eval(input("Enter a number ---> "))
            number2 = eval(input("Enter another number ---> "))
            answer = (number1 + number2)

            print(f"The sum of {number1} and {number2} is {answer}")
        else:
            print("Invalid answer, pls only answer 'yes' or 'no'")

def activity5():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            print("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM")

            print("=======================================")

            fahrenheit = eval(input("Enter temperature in Fahrenheit ----> "))

            celsius = ((fahrenheit - 32)*5) / 9

            print(f"{fahrenheit} degrees Fahrenheit converted to celsuis is {celsius} degrees")
        else:
            print("Invalid answer, pls only answer 'yes' or 'no'")

def activity6():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            x = 5

            print(x)

            x = x + 10

            print(x)

            x = x + 15

            print(x)

            x += 10

            print(x)

            x += 20

            print(x)
        else:
            print("Invalid answer, pls only answer 'yes' or 'no'")

def activity7():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            gold = 0

            name = input("Hi, Enter your name: ")
            hasMine = input("Did you mine gold today? ")

            if hasMine.lower() == "yes":
                gold += hasMine
                print(f"Hi! {name}, Today you have a total of {gold} gold")
            else:
                print(f"Hi! {name}, Today you have a total of {gold} gold")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity8():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            password = input("Enter your password: ")

            if password.lower() == "neftalycareg420":
                print("Acces Granted")
                print("Enjoy using the system")
            elif password.lower() == "neftalycareg123":
                print("Acces Granted")
                print("Enjoy using the system")
            else:
                print("Acces Denied")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity9():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            age = eval(input("Enter your age here ---> "))

            if age <= 7 and age >= 1:
                print("You are a Toddler")

            elif age <= 13 and age >= 8:
                print("You are a Pre-Teen")

            elif age <= 18 and age >= 14:
                print("You are a Teenager")

            elif age <= 31 and age >= 19:
                print("You are in a Early Adulthood")

            elif age <= 45 and age >= 32:
                print("You are in a Mid Adulthood")

            elif age <= 59 and age >= 46:
                print("You are in a Mid Adulthood")

            elif age <= 100 and age >= 60:
                print("You are in a Mid Adulthood")

            else:
                print("Please enter a number") 
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity10():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            name = input("Enter your name: ")
            isStudent = input("Are you a current student of DLL (YES) or (NO): ")

            if isStudent.lower() == "yes":
                yearlevel = input("What year are you currently enrolled? \nF - Freshmen \nS - Sophomore \nJ - Junior \nSR - Senior \nPlease input your answer here: ")

                if yearlevel.lower() == "f":
                    print(f"Hi {name}, Freshmen, Welcome to DLL!")
                if yearlevel.lower() == "s":
                    print(f"Hi {name}, Sophomore, Welcome to DLL!")
                if yearlevel.lower() == "j":
                    print(f"Hi {name}, Junior, Welcome to DLL!")
                if yearlevel.lower() == "sr":
                    print(f"Hi {name}, Senior, Welcome to DLL!")
                else:
                    print("Invalid Input")
        
            else:
                print(f"Thankyou for using the system")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity11():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
                for IKOT in range (1,10):
                    print("Hello World")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity12():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for bilang in range (10, 1, -1):
                print(f"wow ganto sya kadami {bilang}")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity13():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            sum = 1
            isa = int(input("Enter a number: "))
    
            for x in range (isa,0,-1):
                sum *= x
            print(f"The factorial of {isa} is {sum}")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity14():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for x in range (0, 11):
                print(x, end= " ")
                for y in range (0, 11):
                    print("*", end= " ")
            print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity15():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for x in range (0, 11):
                print(x, end= " ")
                for y in range (0, x):
                    print("*", end= " ")
            print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity16():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
                for x in range (1,11):
                    for y in range(1,x+1):
                        print(" ",end=" ")
                    for z in range(11,x,-1):
                        print("*",end=" ")
                    print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity17():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            column = eval(input("Enter number of column >>> "))
            for x in range(1,11):
                for y in range(1,column + 1):
                    print(x*y,end="\t")
                print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity18():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            nt = eval(input("Enter number of triangle(s) ==> "))
            for x in range(1,5):
                for y in range(1,nt+1):
                    for z in range(1,x+1):
                        print("*",end=" ")
                    for a in range(5,x,-1):
                        print(" ",end=" ")
                    print(end=" ")
                print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity19():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            tuloy = True

            while tuloy:
                name = input("Enter your name: ")
                if name.lower() == "stop":
                    print("PROGRAM TERMINATED")
                    break
                    tuloy = False
                else:
                    continue
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity20():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            tuloy = True
            total = 0
            ilan = 0
            while tuloy:
                namba = int(input("Pls enter a number --> "))
                if namba == 0:
                    print("Loop has now terminated")
                    print(f"You have entered {ilan} numbers")
                    print(f"The sum of all the numbers given is {total}")
                    break
                ilan += 1
                total += namba
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity21():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            tuloy = True
            num = 0

            while tuloy:
                ask = input("Do you wish to create a new triangle (yes or no) -> ")

                if ask.lower() == "no":
                    print("Program / Loop Terminated")
                    break
                elif ask.lower() == "yes":
                    num += 1
                    for x in range(1,6):
                        for a in range(1,num + 4):
                            for y in range(1,x+1):
                                print(y,end=" ")
                            for z in range(6,x,-1):
                                print(" ",end=" ")
                        print()
                    continue
            else:
                print("Invalid answer, pls only answer 'yes' or 'no'")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge1():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            print ("\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\b***\n\t\t\t\t\t\t\t\b\b*****\n\t\t\t\t\t\t\t\b\b\b*******\n\t\t\t\t\t\t\t\b\b*****\n\t\t\t\t\t\t\t\b***\n\t\t\t\t\t\t\t*")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge2():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            name = input ("What is youre name? ")
            print ("\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\b\b* * *\n\t\t\t\t\t\t\t\b\b\b\b* * * * *\n\t\t\t\t\t\t\t\b\b\b\b\b\b\b*   "+ name +"   *\n\t\t\t\t\t\t\t\b\b\b\b* * * * *\n\t\t\t\t\t\t\t\b\b* * *\n\t\t\t\t\t\t\t*")      
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge3():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            fullname = input (" What is your name? ")
            age = input (" How old are you? ")
            mobilenumber = input (" What is your mobile number? ")
            email = input (" Email: ")
            gender = input (" Sex: ")
            dateofbirth = input (" Date of birth: ")
            placeofbirth = input (" Where were you born? ")
            maritalstatus = input (" Is married? true or false ")
            religion = input (" Religion: ")
            languagesknown = input (" Languages known: ")
            address = input (" Address: ")

            print ("Hi, my name is " + fullname + " and I'm " , age , " years old " , gender , " \nI live in " + address + " \nmy phone number is " , mobilenumber , " and this is my email " + email + " \nI was born on " , dateofbirth , " in " + placeofbirth + " \nIt is " , maritalstatus ," that i'm married \nMy religion is " + religion + " and " + languagesknown + " is tha language that i can speak") 
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge4():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            number1 = eval(input("Enter a number --> "))

            number2 = eval(input("Enter a number --> "))

            answer1 = number1 + number2
            answer2 = number1 - number2
            answer3 = number1 * number2
            answer4 = number1 / number2
            answer5 = number1 % number2
            answer6 = number1 ** number2
            answer7 = number1 // number2

            print("The sum of  " , number1,  " and " , number2, " is " , answer1)
            print("The difference of  " , number1,  " and " , number2, " is " , answer2)
            print("The product of  " , number1,  " and " , number2, " is " , answer3)
            print("The quotient of  " , number1,  " and " , number2, " is " , answer4)
            print("The remainder of  " , number1,  " and " , number2, " is " , answer5)
            print(" " , number1,  " exponent by " , number2, " is " , answer6)
            print("The floor division of  " , number1,  " and " , number2, " is " , answer7) 
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge5():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            fahrenheit = eval(input("Enter a temperature in fahrenheit: "))
            celsius = ((fahrenheit - 32) * 5)/9

            rounded= (round(celsius, 2))

            print(fahrenheit, "degrees Farenheit converted to celsius is" , rounded, "degree") 
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge6():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            x = 5
            print(x)

            x = x + 10
            print(x)

            x = x + 15
            print(x)

            x = x + 20
            print(x) 
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge7():
    tuloy = True
    
    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask == "no":
            print("Program Terminated")
            break
        elif ask == "yes":
            name = input("Enter your name: ")
            grocery = input("Did you buy grocery? (yes / no): ")

            if grocery == "yes":
                name_item = input("Enter the name of the item you bought: ")
                price_item = float(input("Enter the price of the item: "))
                age = int(input("Enter your age: "))
                given_amount = float(input("Amount given: "))

                disc = round((price_item * 0.052), 2)
                discprice = round((price_item - disc), 2)
                tax = round((price_item * 0.123), 2)
                taxprice = round((price_item + tax), 2)

                if age >= 60:
                    print(f"Hi {name}, you purchased a {name_item}, with a price of {price_item} pesos plus a 5.2% discount ({disc} pesos) to your total purchase.")
                    print(f"Total of: {discprice}")
                    print(f"Change: {round(given_amount - discprice, 2)}")
                    print("Thank you for your purchase. \nCome back again.")

                elif age < 60:
                    print(f"Hi {name}, you purchased a {name_item}, with a price of {price_item} pesos plus a 12.3% tax ({tax} pesos) to your total purchase.")
                    print(f"Total of: {taxprice}")
                    print(f"Change: {round(given_amount - taxprice, 2)}")
                    print("Thank you for your purchase. \nCome back again.")
        
            else:
                print("Thank you for trusting us. \nSee you again next time.")
    
    else:
        print("Invalid answer, please only answer 'yes' or 'no'.")

def codechallenge8():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            sum = 0
            for u in range (1, 11):
                num = int(input(f"Enter number {u}: "))
                sum += num

            print(f"The summationof all provided number is {sum}")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge9():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for x in range(0,11):
                print(" ", end= " ")
                for y in range(0,x):
                    print(" ", end= " ")
                for z in range (x,10):
                    print("*", end= " ")
                print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")
        
def codechallenge10():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for x in range(0, 5):
                for y in range (5, x, -1):
                    print(" ", end=" " )
                for z in range (0, x*2):
                    print("*", end=" " )
                print()
            for a in range(5, 0, -1):
                for b in range (5, a, -1):
                    print(" ", end=" " )
                for c in range (0, a*2):
                    print("*", end=" " )
                print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge11():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for x in range(1,4): 
                for y in range(6,x,-1): 
                    print(" ",end=" ")

                for z in range(x,1,-1):     
                    print("*",end=" ")

                for a in range(1,x+1): 
                    print("*",end=" ")
                print()

            for x in range(4,0,-1): 
                for y in range(6,x,-1): 
                    print(" ",end=" ")

                for z in range(x,1,-1):     
                    print("*",end=" ")

                for a in range(1,x+1): 
                    print("*",end=" ")
                print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge12():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for x in range(1,6):
                for y in range(6,x,-1): 
                    print(" ",end=" ") 

                for z in range(1,x+1): 
                    print("*", end=" ")
    
                for a in range(1,x+1): 
                    print("*", end=" ")
                print()

            for x in range(4,0,-1):
                for y in range(5,0,-1): 
                    print(" ",end=" ") 

                for z in range(6,x,-5): 
                    print("*",end=" ")
    
                for a in range(6,x,-5): 
                    print("*",end=" ")
                print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge13():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for x in range(1,4): 
                for y in range(6,x,-1): 
                    print(" ",end=" ")

                for z in range(x,1,-1):     
                    print(z,end=" ")

                for a in range(1,x+1): 
                    print(a,end=" ")
                print()

            for x in range(4,0,-1): 
                for y in range(6,x,-1): 
                    print(" ",end=" ")

                for z in range(x,1,-1):     
                    print(z,end=" ")

                for a in range(1,x+1): 
                    print(a,end=" ")
                print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge14():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            tuloy = True
            total = 0
            ilan = 0
            while tuloy:
                namba = int(input("Pls enter a number --> "))
                if namba == 0:
                    print("Loop has now terminated")
                    print(f"You have entered {ilan} numbers")
                    print(f"The sum of all the numbers given is {total}")
                    break
                ilan += 1
                total += namba
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge15():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            tuloy = True
            num = 0

            while tuloy:
                ask = input("Do you wish to create a new triangle (yes or no) -> ")

                if ask.lower() == "no":
                    print("Program / Loop Terminated")
                    break
                elif ask.lower() == "yes":
                    num += 1
                    for x in range(1,6):
                        for a in range(1,num + 4):
                            for y in range(1,x+1):
                                print(y,end=" ")
                            for z in range(6,x,-1):
                                print(" ",end=" ")
                        print()
                        continue
            else:
                print("Invalid answer, pls only answer 'yes' or 'no'")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def codechallenge16():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            balance = 0 

            def create_account(name, initial_deposit = 0):
                Account_name = name
                b = 0
                b = initial_deposit
                balance = b
                print(f"BANK ACCOUNT CREATE FOR {Account_name} WITH INITIAL DEPOSIT OF {balance}")

            def check_balance():
                global balance
                print(f"CURRENT BALANCE IS {balance}")



            def get_denomination(amount):
                d1 = amount // 1000
                depo1 = amount % 1000
    
                d2 = amount // 500
                depo2 = depo1 % 500
    
                d3 = amount // 200
                depo3 = depo2 % 200
    
                d4 = amount // 100
                depo4 = depo3 % 100
    
                d5 = amount // 50
                depo5 = depo4 % 50
    
                d6 = amount // 20
                depo6 = depo5 % 20
    
                d7 = amount // 10
                depo7 = depo6 % 10
    
                d8 = amount // 5
                depo8 = depo7 % 5
    
                d9 = amount // 1
                depo9 = depo8 % 1

                print(f"{d1} - 1000")
                print(f"{d2} - 500")
                print(f"{d3} - 200")
                print(f"{d4} - 100")
                print(f"{d5} - 50")
                print(f"{d6} - 20")
                print(f"{d7} - 10")
                print(f"{d8} - 5")
                print(f"{d9} - 1")


            def deposit():
                global balance
                balance += amount
                print(f"Deposited {amount}. New balance is {balance}")

            def withdraw():
                global balance
                if amount <= balance:
                    balance -= amount
                    print(f"Withdrew {amount}. New balance is {balance}")
                else:
                    print("Insufficient funds")



            isCont = True

            get_denomination(1378)
            while isCont == True:
                print("WELCOME TO MY BANK SIMULATION PROGRAM")
                print("=====================================")
                print("ENTER FROM THE OPTIONS BELOW")
                print("1 -- CREATE ACCOUNT")
                print("2 -- DEPOSIT")
                print("3 -- CHECK BALANCE")
                print("4 -- WITHDRAW")
                print("5 -- EXIT")

                choice = input("Enter your choice -- > ")

                if choice == "1":
                    print("BANK APPLICATION FORM")
                    name = input("Please Enter Your FULL NAME --> ")
                    print("INITIAL DEPOSIT IS A REQUIREMENT PHP100 MAINTAINING BALANCE")
                    amount = int(input("Enter Amount to Deposit --> "))
                    create_account(name, amount)
                    print("ACCOUNT CREATED")
                elif choice == "2":
                    amount = float(input("Enter amount to deposit: "))
                    deposit(amount)

                elif choice == "3":
                    check_balance()

                elif choice == "4":
                    amount = float(input("Enter amount to withdraw: "))
                    withdraw(amount)

                elif choice == "5":
                    print("Exiting the bank simulation. Goodbye!")
                    break
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")


isContinue = True

while isContinue:
    
    print("HI WELCOME TO MY PROGRAM")
    print("========================")
    print("1.Activities 2.CodeChallange")
    ask = input("What do want to open? ")
    
    if ask.lower() == "1":
        print("SELECT FROM THE FOLLOWING CODE \n1 = activity1 \n2 = activity2 \n3 = activity3 \n4 = activity4 \n5 = activity5 \n6 = activity6 \n7 = activity7 \n8 = activity8 \n9 = activity9 \n10 = activity10 \n11 = activity11 \n12 = activity12 \n13 = activity13 \n14 = activity14 \n15 = activity15 \n16 = activity16 \n17 = activity17 \n18 = activity18 \n19 = activity19 \n20 = activity20 \n21 = activity21")
        ask = input("Which program would you like to run?, Please select from the option above, Enter Here ==> ")

        if ask == "1":
            activity1()
            continue

        elif ask == "2":
            activity2()
            continue

        elif ask == "3":
            activity3()
            continue

        elif ask == "4":
            activity4()
            continue

        elif ask == "5":
            activity5()
            continue

        elif ask == "6":
            activity6()
            continue

        elif ask == "7":
            activity7()
            continue

        elif ask == "8":
            activity8()
            continue

        elif ask == "9":
            activity9()
            continue

        elif ask == "10":
            activity10()
            continue

        elif ask == "11":
            activity11()
            continue

        elif ask == "12":
            activity12()
            continue

        elif ask == "13":
            activity13()
            continue

        elif ask == "14":
            activity14()
            continue

        elif ask == "15":
            activity15()
            continue

        elif ask == "16":
            activity16()
            continue

        elif ask == "17":
            activity17()
            continue

        elif ask == "18":
            activity18()
            continue

        elif ask == "19":
            activity19()
            continue

        elif ask == "20":
            activity20()
            continue

        elif ask == "21":
            activity21()
            continue

        elif ask == "stop":
            print("The Program Terminated")
            print("Thankyou for using the system!")
            break

    elif ask.lower() == "2":
        print("SELECT FROM THE FOLLOWING CODE \n1 = codechallenge1 \n2 = codechallenge2 \n3 = codechallenge3 \n4 = codechallenge4 \n5 = codechallenge5 \n6 = codechallenge6 \n7 = codechallenge7 \n8 = codechallenge8 \n9 = codechallenge9 \n10 = codechallenge10 \n11 = codechallenge11 \n12 = codechallenge12 \n13 = codechallenge13 \n14 = codechallenge14 \n15 = codechallenge15 \n16 = codechallenge16 ")
        ask = input("Which program would you like to run?, Please select from the option above, Enter Here ==> ")
        
        
        if ask == "1":
            codechallenge1()
            continue

        elif ask == "2":
            codechallenge2()
            continue

        elif ask == "3":
            codechallenge3()
            continue

        elif ask == "4":
            codechallenge4()
            continue

        elif ask == "5":
            codechallenge5()
            continue

        elif ask == "6":
            codechallenge6()
            continue

        elif ask == "7":
            codechallenge7()
            continue

        elif ask == "8":
            codechallenge8()
            continue

        elif ask == "9":
            codechallenge9()
            continue

        elif ask == "10":
            codechallenge10()
            continue

        elif ask == "11":
            codechallenge11()
            continue

        elif ask == "12":
            codechallenge12()
            continue

        elif ask == "13":
            codechallenge13()
            continue

        elif ask == "14":
            codechallenge14()
            continue

        elif ask == "15":
            codechallenge15()
            continue

        elif ask == "16":
            codechallenge16()
            continue


    elif ask.lower() == "stop":
        print("The Program Terminated")
        print("Thankyou for using the system!")
        break
