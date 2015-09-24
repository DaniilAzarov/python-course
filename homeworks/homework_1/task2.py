
def mean_fun(str_lst):
    str_lst = str_lst.split()
    num_lst = []
    for n in str_lst:
        num_lst.append(float(n))
    num_mean = (sum(num_lst) / len(num_lst))
    print(num_mean)

open_fun = mean_fun(input())


  


        



