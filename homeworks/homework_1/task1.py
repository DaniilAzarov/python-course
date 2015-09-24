def spoon_and_iron(gadget, quantity):
    
    if gadget == "ложка":
        vars = ["ложка", "ложки", "ложек"]
        if quantity % 10 == 1 and quantity % 100 != 11:
            gadget = vars[0]
        elif quantity % 100 == 12 or quantity % 100 == 13 or quantity % 100 == 14:
            gadget = vars[2]
        elif quantity % 10 >= 2 and quantity % 10 <= 4:
            gadget = vars[1]
        else:
            gadget = vars[2]
            
    elif gadget == "утюг":
        vars = ["утюг", "утюга", "утюгов"]
        if quantity % 10 == 1 and quantity % 100 != 11:
            gadget = vars[0]
        elif quantity % 100 == 12 or quantity % 100 == 13 or quantity % 100 == 14: 
            gadget = vars[2]
        elif quantity % 10 >= 2 and quantity % 10 <= 4:
            gadget = vars[1]
        else:
            gadget = vars[2]
    
    print(quantity, gadget)

user_input = spoon_and_iron(input(),int(input()))

