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

    def factorial(n):
    	if n == 0:
    		return 1
    	return factorial(n - 1) * n

    if adj > 7:
        adj = 7

    adj_comb = 0
    for k in range(adj):
        adj_comb += factorial(adj) / (factorial(adj-(k + 1)))
        cool = int(adj_comb) * nouns * verbs

    return(cool)

with open("./dict.txt", "r") as dict:
    print(yazkora(dict))
