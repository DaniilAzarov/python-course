import re
import sys

data = sys.stdin.read()
rules = "(\d*)(000+|111+|222+|333+|444+|555+|666+|777+|888+|999+)(\d*)"
results = re.findall(rules, data)
for i in results:
    i = "".join(i)
    print(i)