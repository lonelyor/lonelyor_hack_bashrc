import uuid
import pyperclip

uid = uuid.uuid4().hex
print(uid)
pyperclip.copy(str(uid))


