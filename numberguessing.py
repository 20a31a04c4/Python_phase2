import random as r
r=r.randint(1,10)
for i in range(5):
    k=int(input())
    if r<k:
        print('it is too high')
    elif r>k:
        print('it is low')
    else:
        print('you guessed right')
        break