from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у об'єкт datetime
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        # Отримання поточної дати
        today = datetime.today()
        # Розрахунок різниці у днях
        difference = date_obj - today
        # Повернення різниці у днях як цілого числа
        return difference.days
    except ValueError:
        # Обробка винятків для неправильного формату вхідних даних
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'")
        return None

# Приклад використання
print(get_days_from_today("2021-10-09"))  
