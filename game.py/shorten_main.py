'''
1 for snake
-1 for gun
0 for water
'''
import random
cpu = random.choice([0, 1, -1]) # random choices from computer using random module 
game={'s':1,'w':0,'g':-1} # to make computer understand meaning of choices
reversegame={1:'snake',0:'water',-1:'gun'} # display the meaning of choosen option 
print(game)
choice=input("Enter any input of your choice : ")# user input 
you=game[choice]
print(f'you choosed {reversegame[you]} \nCopmuter choosed {reversegame[cpu]}') # print choices of both
if(cpu==you): # draw condition for game 
    print( 'Game tie') 

#game logic 
# if(cpu==1 and you==-1):  # computer-user = 2
#     print('win')
# elif(cpu==-1 and you==1): # computer-user = -2
#     print('lose')
# elif(cpu==0 and you==1): # computer-user = -1
#     print('win')
# elif(cpu==1 and you==0): # computer-user = 1
#     print('lose')
# elif(cpu==0 and you==-1): # computer-user = 1
#     print('lose')
# elif(cpu==-1 and you==0): # computer-user = -1
#     print('win')
# else:
#     print('something went wrong ,\n Try again !')

# complex logic for game analsying arithmetic chances of win 
if((cpu-you)==1 or (cpu-you)==-2): 
    print('You lose!')
else:
    print("You Win! ")