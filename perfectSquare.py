numberInput=input("Enter a number: ")
number=int(numberInput)

factor=1
sum_of_factors=0

while factor<number:
    if number%factor==0:
        sum_of_factors=sum_of_factors+factor
    factor=factor+1

if sum_of_factors==number:
    print(number, "is a perfect square")
else:
    print(number,"is not a perfect square")
    
if sum_of_factors<number:
    print(number, "is deficient")
else:
    print(number, "is abundant")
