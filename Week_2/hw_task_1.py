#Не уверен, что это самый оптимальный подход, но как сделать задачу не разделяя строку на слова, не придумал
def separator(stroka):
    i = 0
    words = ['']
    for letter in stroka:
        if letter == ' ':
            i += 1
            words.append('')
        else:
            words[i]=words[i]+letter
    return words

def cleaner(stroka):
    words = separator(stroka)
    filtered_words = list(filter(lambda x: x!='Python' and x!='php' and x!='go' and x!='C', words))
    return ' '.join(filtered_words)

A = 'Eto php test C stroki Python'
result = cleaner(A)
print(result)