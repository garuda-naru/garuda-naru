num = int(input("Enter Length of List : "))
L = [int(input("Enter Value : ")) for x in range(num)]
#Ascending Order Sorting
print("Original list ",L)
for i in range(num):
    m_v = L[i]
    for j in range(i+1,num):
        if L[j] < m_v:
            m_v = L[j]
    m_i = L.index(m_v)
    L[i],L[m_i] = L[m_i],L[i]
print("Sorted List in Ascending ",L)

#Descending Order
for i in range(num):
    m_v = L[i]
    for j in range(i+1,num):
        if L[j] > m_v:
            m_v = L[j]
    m_i = L.index(m_v)
    L[i],L[m_i] = L[m_i],L[i]
print("Sorted List in Descending",L)
