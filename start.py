from action import Action
from speech_to_text import s2t
from speak import speak

query = s2t()
value = Action(query)

print("Me-> " + query)
speak(value)
print("Bot->" + value)