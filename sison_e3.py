# filename      : sison_e2.py
# author        : George William Sison
# description   : This is a python program

inputtedNumbers = input("\nEnter a comma separated list of numbers: ")

try :
        
    numbers = str(inputtedNumbers).split(",")
    
    sumOfSquares = 0

    for num in numbers :
        sumOfSquares += float(num) ** 2

    print("Sum of squares: {:.2f}".format(sumOfSquares))
except :
    print("\nInvalid Input!!")
