import random
count=0
score=0
while count<5:
    number=random.randint(1,10)
    
    guess=int(input('Guess a number: '))
    
    if guess==number:
        score=score+1
    print(number)   
    count=count+1

print("You guessed {:d} out of {:d} correctly". format(score,count))
