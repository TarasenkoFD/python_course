import time

def timing(fn):
    def newfun(*args,**kwargs):
        start = time.time()
        result = fn(*args,**kwargs)
        finish = time.time()
        duration = finish - start
        print(f'Vremya - {duration}')
        return result
    return newfun
@timing
def fast(A,B):
    return A+B
@timing
def long(A,B):
    for i in range (0, 10**8):
        result = A + B
    return result

A = 1
B = 2
print(fast(A,B))
print(long(A,B))