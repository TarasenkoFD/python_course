#Не очень понял смысл вызывать второй раз функцию. Вернее, не очень понял, как отследить корректность работы. Только через доп. сообщение, видимо

def second_try(fn):
    def newfn(*args,**kwargs):
        try:
            result = fn(*args,**kwargs)
        except:
            print('Second try')
            result = fn(*args,**kwargs)
        return result
    return newfn
@second_try
def zero_div(n):
    return n/(n-n)
@second_try
def imp_cond():
    return int(1.5)

A = 1

print(zero_div(A))