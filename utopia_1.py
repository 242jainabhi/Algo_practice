f = open('Console_Input.txt','r')
q = f.read().strip().split('\n')
print('No. of lines: ',len(q))
# print(q)
count = 0
for i in q:
    count += len(i.strip().split())
print("No. of words: ",count)
