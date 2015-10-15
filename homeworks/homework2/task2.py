def how_much():
    users_num_list = []
    n = int(input())
    for i in range(0, n):
        users_num = int(input())
        users_num_list.append(users_num)
    return users_num_list
users_list = how_much()


def prime(l):
    if l == 1:
        result = False
    else:
        d = 2
    while l % d != 0:
        d += 1
    if l == d:
        result = True
    else:
        result = False
    return result

for i in users_list:
    print(prime(i))
