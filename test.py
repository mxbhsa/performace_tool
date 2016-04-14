import re
print(re.search('super', 'superstition').span())
print re.search(r"\(%abc\)", "(%abc)(%abc)def").span()