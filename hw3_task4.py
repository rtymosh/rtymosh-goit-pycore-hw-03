# Завдання 4

# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.


# Вимоги до завдання:

# Параметр функції users — це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
# Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
# Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').


# Рекомендації для виконання:

# 1. Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт — datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
# 2. Визначте поточну дату системи за допомогою datetime.today().date().
# 3. Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
# 4. Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
# 5. Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
# 6. Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
# 7. Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
# 8. Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.


# Критерії оцінювання:

# Актуальність та коректність визначення днів народження на 7 днів вперед.
# Правильність обробки випадків, коли дні народження припадають на вихідні.
# Читабельність та структурованість коду.


# Приклад:

# Припустимо, у вас є список users:

# users = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# Використання функції get_upcoming_birthdays:

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)

# Якщо сьогодні 2024.01.22 результатом може бути:

# [
#     {'name': 'John Doe', 'congratulation_date': '2024.01.23'},
#     {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
# ]

# Цей список містить інформацію про те, кого і коли потрібно привітати з днем народження.
from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    # Get current date
    today = datetime.today().date() - timedelta(days=6)
    print("Today is:", today)
    # Initialize list for upcoming birthdays
    upcoming_birthdays = []
    # Convert birthday strings to datetime objects and check for upcoming birthdays
    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=today.year)
        # If birthday has already occurred this year, consider next year(end of December cases)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        # Calculate days until birthday
        days_until_birthday = (birthday_this_year - today).days
        # Check if birthday is within the next 7 days
        if 0 <= days_until_birthday < 7:
            celebration_date = birthday_this_year
            if celebration_date.weekday() in (5, 6):  # Saturday or Sunday
                days_to_monday = 7 - celebration_date.weekday()
                celebration_date = (
                    timedelta(days=days_to_monday) + celebration_date
                )  # Move to next Monday
            # Add to upcoming birthdays list of dicts
            upcoming_birthdays += [
                {
                    "name": user["name"],
                    "congratulation_date": celebration_date.strftime("%Y.%m.%d"),
                }
            ]

    return upcoming_birthdays


# Testing data:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Fn1 LN1", "birthday": "2025.11.09"},
    {"name": "Fn2 LN2", "birthday": "2025.11.02"},
    {"name": "Fn3 LN3", "birthday": "2025.11.05"},
    {"name": "Roman Tymoshenko", "birthday": "2025.11.03"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
