masiv = [] 
a = 0
import random as rd
while a < 19:
    masiv.append(rd.randint(-100,100))
    a += 1
    for i in range(0, len(masiv), 2):
        max_masiv = max(masiv)
        masiv[i] = max_masiv
    
print(masiv)    