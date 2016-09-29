heapArr = list()

def parent(i):
	return (i-1)//2

def insertElem(x):
	pos = len(heapArr)
	heapArr.insert(pos,x)
	while pos!=0 and heapArr[parent(pos)] < heapArr[pos]:
		temp = heapArr[parent(pos)]
		heapArr[parent(pos)] = heapArr[pos]
		heapArr[pos] = temp
		pos = parent(pos)

def heapify(i):
	l = 2*i+1
	r = 2*i+2
	largest = i
	if l < len(heapArr) and heapArr[i] < heapArr[l]:
		largest = l
	if r < len(heapArr) and heapArr[largest] < heapArr[r]:
		largest = r
	if largest != i:
		temp = heapArr[largest]
		heapArr[largest] = heapArr[i]
		heapArr[i] = temp
		heapify(largest)


def getMax():
	max = heapArr[0]
	heapArr[0] = heapArr[-1]
	heapArr.pop()
	heapify(0)
	return max

###main program starts here###
n=int(input())
arr=list(map(int,input().split()))

print(-1,-1,sep="\n")
mul = 1
for i in range(2,n):
    for j in range(i+1):
        insertElem(arr[j])
    mul *= getMax() * getMax() * getMax()
    print(mul)
    mul = 1
    heapArr = []
