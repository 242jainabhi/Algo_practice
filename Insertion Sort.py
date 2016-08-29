a=map(int,raw_input("Enter the Array: ").split())
print "Before sorting: " , a
for i in range(1,len(a)):
    print i,
    j=i-1
    curr=a[i]
    while j >= 0 and curr < a[j]:
        temp = a[j]
        a[j] = a[j+1]
        a[j+1] = temp
        j=j-1
print "After sorting: " , a
