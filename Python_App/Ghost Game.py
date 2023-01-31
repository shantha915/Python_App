# Ghost Game
from random import randint
print('Ghost Game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print('The doors ahead...')
    print('A ghost is behnd one.')
    print('which door do you open?')
    door =  input ('1,2 or 3?')
    door_num = int(door)    
    print('GHOST!')
    feeling_brave = False
else:
    print('No ghost!')
score = score+1
print('Run away!')
print('Game over! you scored', score)
    
