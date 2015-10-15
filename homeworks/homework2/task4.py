def euclid(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        if a % b == 0:
            return b
        else:
            return euclid(b, a % b)
    elif a < b:
        if b % a == 0:
            return a
        else:
            return euclid(a, b % a)


def rpfilter(a, args):
    simple_list = []
    for n in args:
        n = int(n)
        if euclid(a, n) == True:
            simple_list.append(n)
    if len(simple_list) > 0:
        simple_str = ''
        for n in simple_list:
            n = str(n)
            simple_str = (simple_str + n + " ")
        return simple_str
    else:
        return None

users_input = input().split(' ')
print(rpfilter(int(users_input[0]), users_input[1:]))
