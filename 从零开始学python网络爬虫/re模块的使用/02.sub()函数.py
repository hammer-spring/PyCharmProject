import re
phone = '123-4567-1234'
new_phone = re.sub('\D','',phone)
print(new_phone)