def exeptor(fn):
    def checker(*args,**kwargs):
        result = fn(*args,**kwargs)
        if not type(result) is int:
            raise Exception('Wrong output format')
        return result
    return checker

@exeptor
def test(A):
    return A

@exeptor
def testt(A,B):
    return A+B

A1 = 1
A2 = '1'
A3 = True
A4 = [1,2,3]
A5 = 1.0

print(test(A1))
print(test(A2))
print(test(A3))
print(test(A4))
print(test(A5))
