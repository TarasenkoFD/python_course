#Сам не придумал
#Нашел в интернете и разобрался. Немного подкорректировал, чтобы соответствовало задаче

def lesenki(n,k=0):
    result = 0
    if n == 0:
        return result+1
    elif k<n:
        for i in range(k+1, n+1):
            result += lesenki(n-i, i)
        return result
    else:
        return result

print(lesenki(5))


    # 1 - 1
    # 2 - 1
    # 3 - 2
    # 4 - 2
    # 5 - 3
    # 6 - 4
    # 7 - 5