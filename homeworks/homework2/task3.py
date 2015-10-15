def euclid(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        if a % b == 0:
            return b
        else:
            return euclid(b, a % b)
    elif a < b:
        if b % a == 0:
            return a
        else:
            return euclid(a, b % a)

users_input = list(input().split(' '))
a, b = int(users_input[0]), int(users_input[1])

print(euclid(a, b))

