import re
p = re.compile('[a-z]+')
String = " {{2}, {1,2}, {1,2,3}, {1,2,3,4}}"
temp = p.findall(String)

print(temp)
