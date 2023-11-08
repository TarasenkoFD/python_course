def factorial(number):
    if not type(number) is int:
        raise Exception('Wrong format')
    fact = number
    if number == 0:
        fact = 1
    else:
        for i in range(1,number):
            fact *= (number-i)
    return(fact)

A = 5
print(factorial(A))
