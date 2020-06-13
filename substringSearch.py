word='mississippi'
target_str=input('Enter the character you want to check for: ')

for index in range(len(word)):
    if target_str == word[index]:
        print('The letter {} is in the word {}'. format(target_str,word))
        break
    
#print('Yesss {}'. format(target_str))

#while index < len(word):
#        if letter == target_str:
 #           
#        index = index + 1
