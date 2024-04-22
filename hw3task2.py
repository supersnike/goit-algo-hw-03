import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевіряємо коректность вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000 and 1 <= quantity <= (max_num - min_num + 1)):
        return []

    # Генеруємо унікальні числа у заданому діапазоні
    numbers = random.sample(range(min_num, max_num + 1), quantity)

    # Повертаємо відсортований список чисел
    return sorted(numbers)

# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)