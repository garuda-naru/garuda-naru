Exercise 1: Given two lists create a third list by picking an odd-index element from the first list and even index elements from the second.
  
  
  Given:

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]


listone = [3,6,9,12,15,18,21]
listtwo = [4,8,12,16,20,24,28]
listone = listone[1::2]
listtwo = listtwo[0::2]
print("Even List ",listone)
print("Odd List ",listtwo)
print(listone+listtwo)

