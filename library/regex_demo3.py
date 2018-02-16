import re

lst = re.split("[0-9]+", "abc12bbc34zyz")
print(lst)

lst2 = re.findall("[\d]+","abc 12 bbc34 zyz,bbc-pqr 8223")
print(lst2)

lst3 = re.findall(" [\d]+","abc 12 bbc34 zyz,bbc-pqr 8223")
print(lst3)