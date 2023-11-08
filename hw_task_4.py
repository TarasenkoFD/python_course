def value_comparison(value):
    if abs(value)>100:
        print('-')
    elif abs(value)<=100:
        print('+')
    else:
        print('Something went wrong')

B = 7
C = 105

value_comparison(B)
value_comparison(C)