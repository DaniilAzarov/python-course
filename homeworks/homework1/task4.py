def letter_counter(users_str):
    data = {}
    users_lst = sorted(list(users_str))
    counter = 0
    cycle = 0
    while cycle != len(users_lst):
        if users_lst[counter] not in data:
            data[users_lst[counter]] = users_lst.count(users_lst[counter])
        counter += 1
        cycle += 1
    users_lst = list(data.keys())
    users_lst.sort()
    for letter in users_lst:
        print(letter, data[letter])
users_input = letter_counter(input())
