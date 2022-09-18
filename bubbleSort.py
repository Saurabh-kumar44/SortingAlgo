size = int(input("Enter the size:"))
result = []
for i in range(size):
    arr = int(input("Enter the values:"))
    result.append(arr)
print(result)

for i in range(size-1):
    for j in range(0,size-i-1):
         if(result[j]>result[j+1]):
             result[j],result[j+1] = result[j+1],result[j]
             print("Swapping between:",result[j],result[j+1])
print("The Sorted array is:" ,result)