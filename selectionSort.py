L = [2,43,4,1,5,6,7,8,50]
print("The array is:")
for i in range(0,len(L)):
    print(L[i],end =" ")#like same
# print(L)#like same
for i in range(len(L)-1):
    min = i
    for j in range(i+1,len(L)):
        if(L[j]<L[min]):
            min = j
    temp = L[i]
    L[i] = L[min]
    L[min] = temp
    print("Swapping between: ", temp,L[i])
print()
print("Sorted array:")
# for i in range(0, len(L)):
#     print(L[i], end = " ")
print("Sorted Array is:", L)