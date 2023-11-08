def positive_counter(list):
    counter = 0
    for elem in list:
        if elem>0:
            counter += 1
    return(counter)

A = (0,1,-1,4,-4)
print(positive_counter(A))