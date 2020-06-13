num = int(input('Enter a number: '))
counter=0

for item in range(1,num+1):
    if num%item==0:
        counter = counter+1

if counter==2:
    print("{} is a prime number". format(num))
else:
    print("{} is not a prime number". format(num))
