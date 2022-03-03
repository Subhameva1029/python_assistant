from bot import speak
speak("welcome to the calculator section")
speak("   ")
print("_________________!! CALCULATOR !!___________________")
speak("We have few functions available and ")
speak("  ")
speak("we are trying hard to bring new facilities")
speak("  ")
speak(" for addition press one")
speak(" ")
print("ADDITION------------------------- 1")
speak("for substraction press two ")
speak(" ")
print("SUBSTRACTION--------------------- 2")
speak("for multiplication press three ")
speak("  ")
print("MULTIPLICATION------------------- 3")
speak(" for division press four")
speak("  ")
print("DIVISION------------------------- 4")
speak(" to exit press five ")
speak("  ")
print("EXIT----------------------------- 5")

data = []

def addition():
    result = 0
    speak("Enter the number of numbers you wanna add")
    num = int(input("Enter the no. of numbers you wanna add :"))
    for i in range(0, num):
        speak("Enter the number to add : ")
        temp_1 = int(input("Enter the number to add : "))
        data.append(temp_1)
        result += data[i]


    speak(f"Sum of the numbers are {result}")
    print("Sum of the numbers are ", result)

def substraction():
    result = 0
    speak("Enter the number of numbers you wanna substract")
    num = int(input("Enter the no. of numbers you wanna substract :"))
    for i in range(0, num):
        speak("Enter the number to substract : ")
        temp_1 = int(input("Enter the number to substract : "))
        data.append(temp_1)
        result -= data[i]


    speak(f"result after substraction is {result}")
    print("final result is  ", result)

def multiplication():
    result = 1
    speak("Enter the number of numbers you wanna multiply")
    num = int(input("Enter the no. of numbers you wanna multiply : "))
    for i in range(0, num):
        speak("Enter the number to multiply : ")
        temp_1 = int(input("Enter the number to multiply : "))
        data.append(temp_1)
        result *= data[i]


    speak(f"Multiplication of the numbers is {result}")
    print("multiplication of the numbers is ", result)

def division():
    speak("Enter the numerator")
    num_1 = int(input("Enter the Numerator : "))
    speak("Enter the Denominator")
    num_2 = int(input("Enter the Denominator : "))
    quotient = int(num_1 / num_2)
    reminder = num_1 % num_2

    speak(f"quotient of the division is {quotient}")
    speak(f"   and reminder is {reminder}")
    print("Quotient of the Division is  ", quotient)
    print("And Reminder is ", reminder)






cal_inp = int(input("Enter the choice : "))
if cal_inp == 1 :
    addition()

elif cal_inp == 2 :
    substraction()

elif cal_inp == 3 :
    multiplication()

elif cal_inp == 4 :
    division()

elif cal_inp == 5 :
    exit()