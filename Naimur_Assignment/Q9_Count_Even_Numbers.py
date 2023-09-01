def count_even_numbers(L):
    count = 0
    for i in L:
        if i%2 == 0:
            count+=1
        else:
            count = count
    return count

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]    
print(count_even_numbers(a))
