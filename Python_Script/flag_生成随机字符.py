import uuid
import pyperclip

uid = "flag{%s}" % uuid.uuid4().hex
print(uid)
pyperclip.copy(str(uid))


