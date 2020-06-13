my_list = [1.6,2.7,3.8,4.9]
a_list = []
new_list = 0

for val in my_list:
    temp = str(val)
    a_list.append(temp.split('.'))

for val in a_list:
    new_list =(int(val[0]))
    print(new_list)

my_str= ':'.join(val)

print(my_str)
