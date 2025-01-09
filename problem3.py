#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""

x = 0
mylist = [0]

for x in range(0,10):
    y = input("Enter an integer: ")
    y = int(y)
    mylist.append(y)
    if y == -1:
        break

mylist.sort()
listlength = len(mylist)
listlength = int(listlength)
print(f"The largest number you entered was {mylist[listlength-1]}")