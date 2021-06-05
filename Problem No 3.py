Exercise 2: Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
  
  Given:

list1 = [54, 44, 27, 79, 91, 41]


list_one = [54,44,27,79,91,41]
print("Original list : ",list_one)
list_one.remove(list_one[4])
print("List after Adding element at index 2",list_one)
list_one.insert(2,11)
print("List after Adding element at index 2  ",list_one)
list_one.append(11)
print("List after Adding element at last  ",list_one)
