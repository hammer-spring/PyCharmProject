import re
a = 'one1two2three3'
infos = re.findall('\d+',a)
print(infos)