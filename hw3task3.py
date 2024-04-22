import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    digits = re.sub(r'\D', '', phone_number)
    
    # Перевіряємо, чи є міжнародний код, якщо немає - додаємо '+38'
    if not digits.startswith('+'):
        digits = '+38' + digits
    
    return digits

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
