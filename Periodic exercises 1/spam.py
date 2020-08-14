import re
def has_spam(s):
    return len(re.findall('spam', s.lower())) != 0
def is_valid(c):
    return re.match('[\w ]', c) is not None
username = input()
content = input()
if username.isdigit():
    username = False
else:
    username = True
if has_spam(content):
    res = 0
    for c in content:
        if not is_valid(c):
            res += 1
    if res > len(content) / 2:
        content = False
    else:
        content = True
else:
    content = True
if content and username:
    print("Not Spam")
elif (not content ) and username:
    print("Invalid Content")
elif content and (not username):
    print("Invalid Sender")
else:
    print("Fully Invalid")

