def plural(quantity, vars):
    if quantity % 10 == 1 and quantity % 100 != 11:
        gadget = vars[0]
    elif quantity % 100 == 12 or quantity % 100 == 13 or quantity % 100 == 14:
        gadget = vars[2]
    elif quantity % 10 >= 2 and quantity % 10 <= 4:
        gadget = vars[1]
    else:
        gadget = vars[2]
    return str(str(quantity) + " " + gadget)

vars_1 = ['утюг', 'утюга', 'утюгов']
vars_2 = ['ложка', 'ложки', 'ложек']
vars_3 = ['гармошка', 'гармошки', 'гармошек']
vars_4 = ['чайник', 'чайника', 'чайников']

users_input_gadget = input()
users_input_quantity = int(input())

if users_input_gadget == vars_1[0]:
    print(plural(users_input_quantity, vars_1))
elif users_input_gadget == vars_2[0]:
    print(plural(users_input_quantity, vars_2))
elif users_input_gadget == vars_3[0]:
    print(plural(users_input_quantity, vars_3))
elif users_input_gadget == vars_4[0]:
    print(plural(users_input_quantity, vars_4))
