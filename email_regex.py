import re
import email.utils
n = int(input())
for t in range(n):
    mail = input()
    parsed_email = email.utils.parseaddr(mail)[1].strip()
    result = bool(re.match(r'^([A-Za-z0-9\._-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})$',parsed_email))
    if result == True:
        print(mail)
