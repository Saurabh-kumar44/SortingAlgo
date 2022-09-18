size = int(input("Enter the size of list:"))
a = []
for i in range(size):
    val = int(input("Enter the value:"))
    a.append(val)
print(a)
for i in range(1,size):
    t = a[i]
    j = i-1
    while(j>=0 and t<a[j]):
        a[j+1] = a[j]
        print("Swapping between: ",t,a[j])
        j -=1
    a[j+1] = t
    # print(a[i])
    # print("The sorted list is:",a)#same
print("The sorted list is:",a)#same