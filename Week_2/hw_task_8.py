#Нашел метод в интернете. Логика работы понятна
def custom_key(elem):
    return elem[1]

list = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

list.sort(key=custom_key)

print(list)