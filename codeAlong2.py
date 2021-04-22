
"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

import random
import numpy
import matplotlib.pyplot as plot

myList = []
unique_list = []

def mainProgram():
    print("Hello, there! Let's work with lists!")
    while True:
        try:
            print('''
Choose one of the following options. Please type a number ony!''')
            choice1 = input("""
1. Edit the list
2. Search the list
3. View the list
4. End Program
""")
            while True:

                if choice1 == "1":
                    print('''
Choose an option by typing a number.''')
                    choice2 = input('''
1. Add one number to the list
2. Add a bunch of numbers to the list
3. Sort list
4. Clear List''')
                    if choice2 == "1":
                        addToList()
                        break
                    elif choice2 == "2":
                        addABunch()
                        break
                    elif choice2 == "3":
                        sortList(myList)
                        break
                    else:
                        clearList()
                        break


                if choice1 == "2":
                    print('''
Choose an option by typing a number.''')
                    choice3 = input('''
1. Linear Search
2. Recursive Binary Search
3. Iterative Binary search
4. Random Choice''')
                    if choice3 == "1":
                        linearSearch()
                        break
                    elif choice3 == "2":
                        binSearch = input("What number are you looking for? ")
                        recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
                        break
                    elif choice3 == "3":
                        binSearch = input("What number are you looking for?  ")
                        result = iterativeBinarySearch(unique_list, int(binSearch))
                        break
                        if result != -1:
                            print("Your number is at index position {}".format(result))
                        else:
                            print("Your number is not found in the list, bud!")
                        break
                    else:
                        randomSearch()
                        break

           
                if choice1 == "3":
                    print('''
Choose an option by typing a number.''')
                    choice4 = input('''
1. Return the value at an index position
2. Print list
3. Plot list''')
                    if choice4 == "1":
                        indexValues()
                        break
                    elif choice4 == "2":
                        printLists()
                        break
                    else:
                        plotList()
                        break
           
            else:
                break
        except:
            print("An error occured! :( ")

"""
Function explanation:
The variable "newItem" stores the result of a user input function inside of it.
The int() function forces that string into an integer. The append function then adds the value stored in newItem to the end of myList.
The print() functin prints the list with the new value.
"""             
def addToList():
    newItem = input("What would you like to add? Please enter an integer ")
    myList.append(int(newItem))
    print(myList)
"""
Function explanation:
The variable "numToAdd" stores the result of a user input function.
This variable holds the amount of numbers that the user wants to add in the form of a string.
The variable "numRange" does the same thing, but instead stores the user's desired number range.
The values in numToAdd and numRange are both forced into an integer using the int() function.
The for loop uses "numToAdd" to tell the function how many times to run (how many times to add a number to myList).
The append runction uses random.randint to choose a random number to add to the list.
The range (0, int(numRange) ensures that the random number chosen is between 0 and the value in numRange.
""" 
def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input("How many numbers do you want me to add?  ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")
"""
Function explanation:
The for loop tells the function to go through every value in myList individually.
The if statement says that if a value is not already in unique_list, it should append that value into unique_list.
If the value is already in unique_list, the function doesn't append it. Now that there are no duplicates in unique_list,
the function uses sort() to put the list in numerical order.
The variable "showMe" stores the result of a user input function (y or n). If the user types a y, the program prints unique_list.
"""
def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list? Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)
"""
Function explanation:
The variable "indexPos" stores the result of a user input function inside of it.
We then force the value stored in indexPos into an integer using the int() function.
We used indexPos to call a value at the given index position.
""" 
def indexValues():
    indexPos = input("Choose a position in the list to see the value for!  ")
    print(myList[int(indexPos)-1])
"""
Function explanation:
The function uses a print statement displaying a string to the user.
It then uses another print statement to print a random value from myList. random.randint is a library that allows the prorgam to use any integer within a range.
In this case, the range is between 0 and the amount of items in myList.
Since python starts counting at 0, we need to subtract 1 to avoid the possibility of the function choosing an index value that isn't in myList.
"""
def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])
"""
Function explanation:
The variable "searchItem" stores the result of a user input function inside of it. "indexCount" is a variable that will eventually store the number of times
that an item was found in myList. The for loop uses the len() function to tell the program to run the loop for as many times as there are items in myList.
In other words, the loop will run for each individual list item. The if statement tells the function that,
if a value in the list matches the user's input stored in searchItem, it needs to add 1 to index count.
Once a match is found, the function also uses a format function to tell the user what position their value was found at. It then uses another format function to
display the number of times that the value was found (indexCount).
"""
def linearSearch():
    print("We're going to search through the list in THE WORST WAY POSSIBLE MWAHAHAHAH!")
    searchItem = input("What are you looking for? Number-wise?  ")
    indexCount = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            indexCount = indexCount + 1
            print("Your item is at index {}".format(x))
    print("Your item appeared {} times in the list".format(indexCount))
"""
Function explanation:
This function finds the user's desired value by continuously removing the half of the list that does not contain the value.
To do this, it defines 3 variables: low, high, and mid. mid is the average of low and high.
The if statement says that if the value happens to be directly in the middle of the list, it can display that value's index position and stop running.
The elif statement says that if the value has a lower index position than the middle of the list, it re-runs
the entire function, this time without the top half of the list.
It repeats this until the number falls directly in the middle of the list or until it is the only number remaining.
The else statement says that if the value's index position is higher than the middle of the list, it re-runs the function without the bottom half of the list.
If the number is not found in the list, the program uses a print statement to tell the user that the number isn't there.
"""
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Oh, what luck. Your number is at position {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)

        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")
"""
Function explanation:
This function defines 3 variables- low, mid, and high. "high" is the highest position in the list, "low" is the lowest position in the list, and mid is
the average of high and low (the middle position of the list).
The while loop says that if the value in low is less than the value in high (if there are items in the list), it should find the
midpoint of the list by averaging high and low. The if statement says that if the desired value's position is in the top half of the list,
the program should remove the entire lower half of the list by reassigning low (which was previously 0) to mid + 1.
This removes the old mid point and everything before it. The elif statement is essentially the same, but removes the top half of the
list when the desired value is in the lower half. This loop will continue over and over until the value is directly in the middle of the list.
"""
def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
"""
Function explanation:
The first if statement says that if there are no items in myList, the function should tell the user that the list is empty.
If myList is empty, that means unique_ist is also empty, so there is no need to print either.
The elif statment says that if unique_list is empty, it can
print myList instead, without having to ask the user to choose which list to view.
The else statement says that if neither of the previous conditions are true and both lists have items, it should ask the user which one to print.
The variable "whichOne" stores the data from the user input. If the user types s, the function prints the sorted list (unique_list).
Otherwise, it prints the original myList.
"""
def printLists():
    if len(myList) == 0:
        print("Your list is empty!")
    elif len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or un-sorted? s/u ")
        if whichOne.lower() == "s":
            print(unique_list)
        else:
            print(myList)
"""
Function explanation:
This function uses two libraries- numpy and matplotlib.
The first line tells the function to print all the points in myList.
The x coordinate of those points are the values in myList.
The y coordinates of those points are ceated by the function numpy.zeros_like. This function creates an array of zeros with the same dimensions as myList.
For example, if myList is [1,2,3] numpy.zeros_like creates a list that is [0,0,0], making the coordinates onthe graph (1,0) (2,0) and (3,0).
The second line of the function creates a title for the graph.
The third line of the function tells the graph what tick marks to put on the y axis.
There are no numbers in the brackets, so the graph doesn't show any tickmarks on the y axis.
The last line of the program shows the graph.
"""
def plotList():
    plot.scatter(myList, numpy.zeros_like(myList))
    plot.title('Your List :)')
    plot.yticks([])
    plot.show()
"""
Function explanation:
This function uses .clear() to clear myList and unique_list. 
"""
def clearList():
    myList.clear()
    unique_list.clear()
    print("Your list has been cleared!")


if __name__ == "__main__":
    mainProgram()
