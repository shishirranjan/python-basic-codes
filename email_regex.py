import re
import email.utils
n = int(input())
for i in range(n):
    mail = input()
    parsed_email = email.utils.parseaddr(mail)[1].strip()
    result = bool(re.match(r'^[a-zA-Z][\w\-\.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$',parsed_email))
    if result == True:
        print(mail)
