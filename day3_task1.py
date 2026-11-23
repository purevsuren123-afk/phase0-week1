n = 100
def sum_to_n(n):
    total = 0
    for i in range(1, n+1):
        total = total+ i
    return total

def sum_to_n_2(n):
    return n * (n + 1) // 2

print(sum_to_n(n))
print(sum_to_n_2(n))   
print(sum_to_n(n)==sum_to_n_2(n))



