n=int(input("Enter the number: "))
for i in range(2,int(pow(n,0.5))):
    if n % i == 0:
        count = 0
        while n%i == 0:
            n /= i
            count += 1
        print("%s^%s" %(i,count))
if n != 1:
    print("%s^%s" %(n,1))
