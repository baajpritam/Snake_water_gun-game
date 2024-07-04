'''
1 for snake
-1 for gun
0 for water
'''
import random
cpu = random.choice([0, 1, -1]) # random choices from computer using random module 
print('Option are :-')
game={'s':1,'w':0,'g':-1} # to make computer understand meaning of choices
reversegame={1:'snake',0:'water',-1:'gun'} # display the meaning of choosen option 
print(game)
choice=input("Enter any input of your choice : ")# user input 
you=game[choice]
print(f'User choosed :- {reversegame[you]} \nCopmuter choosed :- {reversegame[cpu]}') # print choices of both choices
#game logic
if(cpu==you): # draw condition for game 
    print( 'Game tie')
elif(cpu==1 and you==-1):  # computer = snake and user = gun
    print('Game result : User win')
elif(cpu==-1 and you==1): # computer = gun and user = snake
    print('Game result : Computer win')
elif(cpu==0 and you==1): # computer = water and user = snake
    print('Game result : User win')
elif(cpu==1 and you==0): # computer = snake and user = water
    print('Game result : Computer win')
elif(cpu==0 and you==-1): # computer = water and user = gun
    print('Game result : Computer win')
elif(cpu==-1 and you==0): # computer = gun and user = water
    print('Game result : User win')
else:
    print('something went wrong ,\n Try again !') 