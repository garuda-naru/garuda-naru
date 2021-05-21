#Create a Function For Mergesort Algoritham
def MergeSort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[ :mid]
        right_list = list1[mid: ]
#We need to run same Function Until Complete Sort So We use Recursion
        MergeSort(left_list)
        MergeSort(right_list)
#To Stop Recursion Initialise the indexes
        i = 0
        j = 0
        k = 0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k] = left_list[i]
                i+=1
                k+=1
            else:
                list1[k] = right_list[j]
                j+=1
                k+=1
#this statement for to check if there any remaining values 
        while i<len(left_list):
            list1[k] = left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            list1[k] = right_list[j]
            j+=1
            k+=1
num = int(input("Enter Length of List : "))
list1 = [int(input("Enter Values : "))for x in range(num)]
MergeSort(list1)
print(list1)