import uuid
import pyperclip

uid = uuid.uuid4()
print(uid)
pyperclip.copy(str(uid))


