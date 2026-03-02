import re

text = "The rain in Spain stays\n mainly in the plain."
pattern = r"\b[a-z].{4,}\b"
matches = re.search(pattern, text)
print(matches) # The

price = "Mango rates are 50.99 per kg."
pattern = "[0-9][0-9].[0-9][0-9]"
match_phone = re.search(pattern, price)
print(match_phone.group()) # 50.99
