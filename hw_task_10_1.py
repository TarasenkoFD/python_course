lst = [2,4,5,8,9,13]
i = 0
while i<len(lst):
    lst[i]*=i
    i+=1
print(lst)