import re
import sys

data = sys.stdin.read()
rules = '[Yu][Oo][Uu]'
results = len(re.findall(rules, data))
print(results)