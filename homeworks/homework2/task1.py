def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)


def combinations(n, k):
    if k > n:
        return 0
    else:
        comb_calc = factorial(n) / (factorial(k) * factorial(n - k))
        return comb_calc
users_input = list(input().split(' '))
n, k = int(users_input[0]), int(users_input[1])
a = combinations(n, k)
print(int(a))

