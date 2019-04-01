import re
a = 'one1two2three3'
infos = re.search('\d+',a)
print(infos)
print(infos.group())