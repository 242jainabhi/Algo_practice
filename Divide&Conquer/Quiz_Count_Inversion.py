from Counting_Inversions_Example import mergeSort

f=open("IntegerArray.txt",'r')
arr=f.readlines()
arr=[int(i.strip()) for i in arr]

print("Counting...")
count = mergeSort(arr)
print("No. of Inversions: ",count)

f.close()
