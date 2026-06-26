import re

p = re.compile('[a-z]+')
m = p.finditer("333 python test")

for r in m:
    print(r)