def mergesort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        leftlist = list1[:mid]
        rightlist = list1[mid:]
        mergesort(leftlist)
        mergesort(rightlist) 
        i=j=k=0 
        while(i<len(leftlist) and j<len(rightlist)):
            if leftlist[i] < rightlist[j]:
                list1[k] = leftlist[i]
                i +=1
                k +=1
                # print("Swapping list",leftlist[i],rightlist[j])
            else:
                list1[k] = rightlist[j]
                j +=1
                k +=1
                # print("Swapping list",leftlist[i],rightlist[j])
        while i<len(leftlist):
            list1[k] = leftlist[i]
            i +=1
            k +=1
            # print("Swapping list",leftlist[i],rightlist[j])
        while j<len(rightlist):
            list1[k] = rightlist[j]
            j +=1
            k +=1
            # print("Swapping list",leftlist[i],rightlist[j])

# num = int(input("Enter how many elements you want in list:"))
# list1 = [int(input())for x in range(num)]
list1 = [23,4,22,45,3,2,56]
print("Your list is:",list1)
mergesort(list1)
print("Sorted list is:",list1)