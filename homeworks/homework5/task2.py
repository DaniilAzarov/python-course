import re
import sys

data = sys.stdin.read()
rules = "\d*[1234567890]{3}\d*"
results = str(re.findall(rules, data))
print(results)
