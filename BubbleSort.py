#Ente Length of List of Bubble Sort 
num = int(input("Enter Length of Value : "))
L = [int(input("Enter Value : "))for x in range(num)]
print("Original List : ",L)
#Bubble sort in ascending Algoritham
for j in range(num-1):
    for i in range(num-1):
        if L[i]>L[i+1]:
            L[i],L[i+1] = L[i+1],L[i]
print("Sorted List in Ascending Order: ",L)
#Bubble Sort in Descending Algoritham
for j in range(num-1):
    for i in range(num-1):
        if L[i]<L[i+1]:
            L[i],L[i+1] = L[i+1],L[i]
print("Sorted List in Descending Order: ",L)