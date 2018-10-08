
inputtedNumbers = input("\nEnter a comma separated list of numbers: ")

try :
        
    numbers = str(inputtedNumbers).split(",")
    
    sumOfSquares = 0

    for num in numbers :
        sumOfSquares += float(num) ** 2

    print("Sum of squares: " + str(sumOfSquares))
except :
    print("\nInvalid Input!!")