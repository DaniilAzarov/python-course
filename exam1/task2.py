def yazkora(dict):
    line = dict.read().split('\n')
    nouns = 0
    verbs = 0
    adj = 0
    for word in line:
        if word.endswith('yo'):
            adj += 1
        elif word.endswith('ka'):
            nouns += 1
        else:
            verbs += 1

    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    cool = factorial(adj) * nouns * verbs
    return(cool)

with open("./dict.txt", "r") as dict:
    print(yazkora(dict))