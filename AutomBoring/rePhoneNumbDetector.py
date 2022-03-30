import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me 415-555-10111, or at 415-555-9999 when time.')
print(mo.group())


print(phoneNumRegex.findall('Call me 415-555-10111, or at 415-555-9999 when time.'))

