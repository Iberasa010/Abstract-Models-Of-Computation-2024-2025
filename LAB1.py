import math
# THIS IS THE FIRST PYTHON LAB ON THIS SUBJECT. IT'S JUST A COUPLE INTRODUCTORY EXERCISES.
# NOTE: AI has been used to document some of the functions, as well as to translate certain parts of the code.

#EXERCISE 1:
print("EXERCISE 1")
# This function takes a number as input and returns its absolute value.
# It uses the built-in abs() function to compute the absolute value of said number.
def absoluteValue(num):
    return abs(num)

print(absoluteValue(-5))
print(absoluteValue(0))
print(absoluteValue(-11))

print("-----------------------------------------------------------------------------")

#EXERCISE 2:
print("EXERCISE 2")
#This function takes two numbers as input (num1 and num2) and returns their sum
def sum(num1, num2):
    return num1 + num2

print(sum(-5, 2))
print(sum(5, 2))
print(sum(0, -12))

print("-----------------------------------------------------------------------------")

#EXERCISE 3:
print("EXERCISE 3")
# This function converts a temperature from Celsius to Fahrenheit.
# It takes a temperature in Celsius as input and returns the equivalent in Fahrenheit.
def celsiusToFahrenheit(temperature):
    return (9/5)*temperature + 32

print(celsiusToFahrenheit(5))
print(celsiusToFahrenheit(-12))
print(celsiusToFahrenheit(43))

print("-----------------------------------------------------------------------------")

#EXERCISE 4:
print("EXERCISE 4")
# This function calculates the area of a sphere given its radius.
# It takes the radius as input and returns the result using the formula: 4 * pi * radius.
# Note: The math module must be imported to access the value of pi.
def calculateSphereArea(radius):
    pi = math.pi
    return 4 * pi * (radius ** 2)

print(calculateSphereArea(4))
print(calculateSphereArea(0))
print(calculateSphereArea(21.1))

print("-----------------------------------------------------------------------------")

#EXERCISE 5:
print("EXERCISE 5")
# NOTE: THIS EXERCISE IS COMMENTED OUT BECAUSE ASSERT EXCEPTIONS BLOCK THE REST OF THE SCRIPT.
# UNCOMMENT TO RUN THIS PART AND VERIFY IT WORKS, THEN COMMENT IT OUT AGAIN TO CHECK THE REST OF THE EXERCISES.

'''
# This function checks three conditions using assertions:
# 1. It checks if 'a' is equal to 'b'. If not, it raises an AssertionError with an error message.
# 2. It checks if 'b' is less than 'c'. If not, it raises an AssertionError with an error message.
# 3. It checks if 'c' is greater than 'a'. If not, it raises an AssertionError with an error message.
# If all conditions are met, the function completes without raising any errors.
def verifyValues(a, b, c):
    assert a == b, "Error: a and b do not have the same values"
    assert b < c, "Error: b is not less than c"
    assert c > a, "Error: c is not greater than a"
    return "Conditions are correct!"


print(verifyValues(4, 4, 6))
print(verifyValues(2, 5, 6))
print(verifyValues(4, 4, 2))
print(verifyValues(0, 0, 0))
'''

print("-----------------------------------------------------------------------------")

#EXERCISE 6
print("EXERCISE 6")
# This function calculates the Euclidean distance between two points (x1, y1) and (x2, y2).
# It uses the formula: sqrt((x2 - x1)^2 + (y2 - y1)^2).
# First, it calculates the squared differences for both x and y coordinates,
# then returns the square root of the sum of these squared differences.
# Note: The math module must be imported to use math.sqrt().
def calculateEuclideanDistance(x1, y1, x2, y2):
    num1 = (x2 - x1) ** 2
    num2 = (y2 - y1) ** 2
    return math.sqrt(num1 + num2)

print(calculateEuclideanDistance(2, 4, 2, 3))
print(calculateEuclideanDistance(0, 4, 12, 4.2))
print(calculateEuclideanDistance(1.2, 1.2, 1.2, 1.2))

print("-----------------------------------------------------------------------------")

#EXERCISE 7
print("EXERCISE 7")
# This function performs a mathematical calculation using three steps:
# 1. It calculates 5 times the cube of 'x' and stores it in num1.
# 2. It calculates the square root of the sum of the squares of 'x' and 'y', storing the result in num2.
# 3. It calculates the exponential of the natural logarithm of 'x' (which simplifies to 'x') and stores it in num3.
# The function then returns the sum of num1, num2, and num3.
# Note: The math module must be imported for math.sqrt(), math.exp(), and math.log().
def exerciseCalculation(x, y):
    num1 = (5 * (x ** 3))
    num2 = math.sqrt((x**2) + (y**2))
    num3 = math.exp(math.log(x))
    return num1 + num2 + num3

print(exerciseCalculation(2, 3))
print(exerciseCalculation(5, 5))
print(exerciseCalculation(10, 5))
print(exerciseCalculation(12.2, 1))


print("-----------------------------------------------------------------------------")

#EXERCISE 8
print("EXERCISE 8")
# This function creates and returns a simple list.
# The list contains five integer elements: [1, 2, 3, 4, 5].
# The function does not take any inputs and simply returns the predefined list.
def createList():
    list = [1, 2, 3, 4, 5]
    return list

# This collection is known as a 'list'. We can consider it a numerical vector, but Python lists
# usually come with a series of built-in functions that allow us to modify the list in more ways
# than numerical arrays in other programming languages.

print(createList())

print("-----------------------------------------------------------------------------")

#EXERCISE 9
print("EXERCISE 9")
# This function iterates through a given list and replaces any occurrence of the number 4 with the number 10.
# The function then returns the modified list.
def replaceFours(list):
    for i in range(len(list)):
        if list[i] == 4:
            list[i] = 10
    return list

listOfFours1 = [4, 4, 4]
listOfFours2 = [4, 1, 2, 2, 2, 2, 3, 4, 99, 0, 1, 4]

print(replaceFours(listOfFours1))
print(replaceFours(listOfFours2))


print("-----------------------------------------------------------------------------")

#EXERCISE 10
print("EXERCISE 10")
# This function calculates the number of iterations required for each number in the input list
# to reach 1 using the Collatz conjecture.
# For each number in the list:
# - If the number is even, it is divided by 2.
# - If the number is odd, it is multiplied by 3 and then 1 is added.
# The process continues until the number becomes 1, and the iteration count is stored.
# The function returns a new list with the iteration count for each number.
def collatzIterationsForEachNumber(list):
    resultList = []

    for i in range(len(list)):
        count = 0
        num = list[i]
        finished = False
        while not finished:
            if num == 1:
                finished = True
            else:
                if num % 2 == 0:
                    num = num / 2
                    count += 1
                else:
                    num = (num * 3) + 1
                    count += 1

        resultList.append(count)

    return resultList

list1 = [1, 3, 17, 22, 7]
list2 = [21, 31, 11, 10]
list3 = [6, 11, 27, 32, 33]

print(collatzIterationsForEachNumber(list1))
print(collatzIterationsForEachNumber(list2))
print(collatzIterationsForEachNumber(list3))


print("-----------------------------------------------------------------------------")

#EXERCISE 11
print("EXERCISE 11")
# This function initializes and returns a predefined matrix (2D list).
# The matrix contains six rows and three columns with various integer values.
# The function does not take any input and simply returns the predefined matrix.
def initializeMatrix():
    matrix = [[1, 2, 3], [4, 5, 1], [1, 2, -1], [2, 2, 2], [0, -3, -4], [0, 1, -1]]
    return matrix

print(initializeMatrix())


print("-----------------------------------------------------------------------------")

#EXERCISE 12
print("EXERCISE 12")
# This function counts how many times a specific number appears in a given matrix (2D list).
# It takes two arguments:
# - 'matrix': the matrix in which to search for the number.
# - 'num': the number to count occurrences of.
# The function iterates through each element of the matrix, and if the element is equal to 'num',
# it increments a counter. It then returns the total count of occurrences.
def countOccurrencesInMatrix(matrix, num):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == num:
                count += 1
    return count

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
matrix3 = [[-1, 2, 3], [-4, 5, -1], [7, -1, 9]]

print(countOccurrencesInMatrix(matrix1, 5))
print(countOccurrencesInMatrix(matrix2, 1))
print(countOccurrencesInMatrix(matrix3, -1))

print("-----------------------------------------------------------------------------")

#EXERCISE 13
print("EXERCISE 13")
# This function checks if there is any number between 4 and 7 (exclusive) in a given matrix (2D list).
# It iterates through each element of the matrix:
# - If it finds a number that is greater than 4 and less than 7, it prints a message and returns True.
# - If no such number is found after checking all elements, it prints a different message and returns False.
def isNumberBetweenFourAndSeven(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] > 4 and matrix[i][j] < 7):
                print("A number between 4 and 7 has been found")
                return True

    print("No number between 4 and 7 has been found")
    return False

matrixA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrixB = [[10, 2, 3], [-1, 0, 1], [8, 9, 7]]
matrixC = [[5, 4, 2], [3, 7, 6], [1, 10, 8]]

print(isNumberBetweenFourAndSeven(matrixA))
print(isNumberBetweenFourAndSeven(matrixB))
print(isNumberBetweenFourAndSeven(matrixC))


print("-----------------------------------------------------------------------------")

#EXERCISE 14:
print("EXERCISE 14")
# This function compares a list of numbers with a corresponding list of booleans.
# It counts how many times the following conditions are met:
# 1. A number is greater than 0 and its corresponding boolean value is True.
# 2. A number is less than or equal to 0 and its corresponding boolean value is False.
# The function returns a list where:
# - The first element is the count of matches for positive numbers with True.
# - The second element is the count of matches for non-positive numbers with False.
def compareBooleansToNumbers(numberList, booleanList):

    matchList = [0, 0]
    for i in range(len(numberList)):
        if numberList[i] > 0 and booleanList[i] == True:
            matchList[0] += 1

        elif numberList[i] <= 0 and booleanList[i] == False:
            matchList[1] += 1

    return matchList

numberList1 = [-2, 3, 4, -7, 10, -234]
booleanList1 = [True, True, True, True, False, False]
numberList2 = [1, -2, 3, 0, -5]
booleanList2 = [True, False, True, False, False]

print(compareBooleansToNumbers(numberList1, booleanList1))
print(compareBooleansToNumbers(numberList2, booleanList2))

print(compararBooleanosANumeros(listaNums2, listaBools2))


