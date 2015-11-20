import utils

from utils import prime as prime1
print(prime1(17))


from utils import *
print(prime1(17))
#print(utils.euclid(17, 85))
#print(dir(utils))

import timeit
print(timeit.timeit("prime1(17)", "from utils import prime as prime1", number = 10000))



