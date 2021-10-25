import random
lst = [random.randint(0, 30) for i in range(20)]
print(lst)
result=0
count=0
for a in range(len(lst)-2):
    if lst[a+2] > lst[a+1] > lst[a]:
        count+=1
    elif count>=1 and lst[a+1] > lst[a+2]:
        result+=1
        count=0 
if lst[-1] > lst[-2] > lst[-3]:
    result+=1
print(result)