
INSTRUCTIONS:

1. The program will begin by prompting you with four numbered options. Choose an option and type the corresponding number. 
Press enter.

	a. It's a good idea to choose the first option of editing the list to begin. Most of the functions will
	only work if the list has numbers in it.

	b. the binary search functions require the list to be sorted. Before using a search method, sort the list.
	
	c. If you type anything but a number option, the program will return an error message. If that happens, 
	re-enter your choice. 

2. Once you have chosen a number option, the program will ask you to choose from a set of more specific options. 
Once again, type the number that corresponds with the action that you want to do.

3. After running your chosen action, the program will return to the first four options. From there, you may run through the
actions as many times as you want

4. To end the program, choose option 4 (end program) from the main action list.

-----------------------------------------------------------------------

BINARY SEARCH

A binary search is an efficient search algorithm that searches for a given value by dividing a list if half repeatedly. With each iteration, 
it eliminates half of the possible values. It compares the middle position of the sorted list to the value it's searching for in order to decide 
which half to continue the search in.

The recursive binary search function is able to quickly identify the user’s desired value by determining where the number is in relation to the 
midpoint of the sorted list. To do this, the function uses 3 arguments: ‘low’, ‘high’, and ‘mid’. ‘low’ represents the first index value in the list, 
which is zero when the function begins. High represents the highest index value in the list, which is the number of items in the list when the program begins. 
‘mid’ is the average of low and high. 

If the index position of the number is greater than the midpoint of the list, the program removes the bottom half of the list. 
It does so by re-running the program and changing the index value in ‘low’ from 0 to one position greater than the midpoint.
If the index position of the desired value is below the midpoint of the list, it removes the top half of the list by changing the index value
in ‘high’ to the position right before the midpoint. The function repeats this process until it ends up with a list that contains only one element. 
It checks whether that element matches the user’s input. If it does, the value’s index position is printed, if it doesn't, that means the list doesn’t 
contain the value. 

The iterative binary search works similarly. It also finds the desired value’s index by comparing its position to the midpoint and adjusting 
the ‘low’ and ‘high’ values accordingly. However, rather than using recursion to call itself repeatedly, the iterative binary search function uses a while loop. 
Instead of changing the arguments every time it runs, it redefines the low, mid, and high variables. The while loop runs over and over until the user’s input
 matches the value in ‘mid’.

-----------------------------------------------------------------------

MY IMPROVEMENTS

The most significant change that I implemented into the program was changing how the editing options were displayed. My goal was to reduce the amount 
of text that a user had to read at once. I separated the list editing options into four categories: edit the list, search the list, view the list, and end program. 
When a user chooses one of those four options, the program displays a more specific set of actions within the chosen category. By organizing 
the actions into groups, it helps the user understand what each function does and doesn’t overload the screen with long lists of text. Another improvement 
that I made to the program was building a function that allows the user to view their list on a number line. Visually displaying the list helps the user
to notice trends that are difficult to see when looking at a long list of numbers.

Before:

1. Add to list
2. Add a bunch o' numbers to the list
3. Return the value at an index position
4. Sort list
5. Random Choice
6. Linear Search
7. Recursive Binary Search
8. Iterative Binary Search
9. Print list
10. Plot list
11. Clear list
12. End program

After: 

1. Edit the list
2. Search the list
3. View the list
4. End Program

If I could make additional improvements to the program, I would rephrase some of the action options. Most users won’t understand the difference between
 binary and iterative search. It probably isn’t necessary to include both options because it will make little to no difference for the user.
