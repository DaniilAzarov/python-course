
def lst_sort(num_lst):
    num_lst_for_sort = []
    str_lst = num_lst.split()    
    for num in str_lst:
        num_lst_for_sort.append(int(num))
    lst_of_odd = sorted(num_lst_for_sort[0::2])
    lst_of_even = sorted((num_lst_for_sort[1::2]), reverse = True)
    counter = 0
    lst_sorted = []
    while counter != (len(num_lst_for_sort)/2):
        lst_sorted.append(lst_of_odd[counter])
        lst_sorted.append(lst_of_even[counter])
        counter = counter + 1
    
    for num in lst_sorted:
        print (num, end = ' ')

user_input = lst_sort(input())
