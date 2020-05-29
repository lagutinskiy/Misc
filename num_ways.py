def num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)

def num_ways2(n):
    n_array = []
    for i in range(n+1):
        if i == 0 or i == 1:
            n_array.insert(i,1)
        else:
            n_array.insert(i, n_array[i-1] + n_array[i-2])
    return n_array[n]        

print(num_ways(35))
print(num_ways2(35))  