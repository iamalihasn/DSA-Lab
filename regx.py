import re

paragraph = "The rain in Spain stays mainly in the plain."
pattern = r'\b\w+ain\b'  # Matches words that end with 'ain'
matches = re.findall(pattern, paragraph)
print(matches)  # Output: ['rain', 'Spain', 'plain']

sentance = "The quick brown fox jumps over the lazy dog."

pat = r'\b\w{3}\b'  # Matches words with exactly 3 letters
matches = re.findall(pat, sentance)
print(matches)  # Output: ['The', 'fox', 'the', 'dog']

sentance2 = "The RAIN in SPAIN STAYS MAINLY in the PLAIN."
pat = r'\b[A-Z]{4,5}\b'  # Matches words with exactly 4 uppercase letters
matches2 = re.findall(pat, sentance2)
print(matches2)  # Output: ['RAIN', 'SPAIN', 'STAYS', 'PLAIN']

phone = "My phone number is 123-456-7890."
patt = r'\d{3}-\d{3}-\d{4}'
match_phone = re.search(patt, phone)

if match_phone:
    print("Phone number found:", match_phone.group())
else:
    print("Phone number not found.")

email = "Please contact us at support@example.com for more information."
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
match_email = re.search(email_pattern, email)
if match_email:
    print("Email found:", match_email.group())
else:    
    print("Email not found.")