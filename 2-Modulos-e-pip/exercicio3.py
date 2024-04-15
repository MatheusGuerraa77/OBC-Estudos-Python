import re

def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_character("ADFDSFSFfdsffbf213321^"))
print(check_character("#@^'{};.<>"))