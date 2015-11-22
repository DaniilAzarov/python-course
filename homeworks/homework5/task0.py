import re
import sys

data = sys.stdin.read()
results = len(re.findall("you", data))
print(results)