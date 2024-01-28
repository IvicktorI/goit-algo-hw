import re

phone_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    '+1246 12345678'
    ]

def normalize_phone(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)
    if len(phone_number)==12:
        phone_number= '+'+phone_number
    else:
        phone_number=phone_number[len(phone_number)-9::]
        phone_number='+380'+phone_number
    return phone_number

for i in range(len(phone_numbers)):
    phone_numbers[i]=normalize_phone(phone_numbers[i])

print(phone_numbers)