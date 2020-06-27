n=int(input())
arr = list(input())

second_list = []
count = 0

for num in arr:
    newNum = int(num)
    second_list.append(newNum)

firstMax = max(second_list)
second_list = [value for value in second_list if value != firstMax]

secondMax = max(second_list)
print(secondMax)


# highest = 0
# secondHighest = 0
# second_list = []

# for num in arr:
#     newNum = int(num)
#     if newNum>highest:
#         second_list.append(highest)
#         highest = newNum
    
#     else:
#         second_list.append(newNum)

# for value in second_list:
#     if value>secondHighest and value!=highest:
#         secondHighest=value

# print (secondHighest)


    
# listEl = [1,2,5,6,7,8];

# second=0;

# # find the highest number in the list;

# first=max(listEl);

# # form a new list without the highest number included

# indexOfHighestValue=listEl.index(first)
# del listEl[indexOfHighestValue]
# print(listEl)
# # find the maximum of this new list
# second =  max(listEl)

# print(second)
# # return the value;

