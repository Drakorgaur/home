import re
text = '</note> and <b>foo</b> and <i>so on</n> and 1 < 2'

print(re.findall(r'<(/?[a-z]{1,4})>', text))
# /? - searches for optional backslash
# [a-z]{1,4} - searches for 1 to 4 lowercase letters
