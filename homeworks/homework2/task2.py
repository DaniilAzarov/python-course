users_num_list = []


def how_much():
    n = int(input())
    for i in range(0, n):
        users_num = int(input())
        users_num_list.append(users_num)

    def prime():
        for l in users_num_list:
            if l == 1:
                print(False)
            else:
                d = 2
                while l % d != 0:
                    d += 1
                if l == d:
                    print(True)
                else:
                    print(False)
    prime()
how_much()

