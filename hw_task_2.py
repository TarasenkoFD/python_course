def max_len_of_lists(list1,list2):
    len1 = len(list1)
    len2 = len(list2)
    max_len = max(len1,len2)
    return (max_len)

A = [1,2,3,5]
B = ['a',1,73,35,'b']

print(max_len_of_lists(A,B))