import requests
import re

utl_bio = "http://bioinformaticsinstitute.ru"

response = requests.get(utl_bio)
html_code = response.text

regex = "<a href=\"http://twitter.com/[^\"]+\" "
results = re.findall(regex, html_code)

print(response.status_code)
print(results)