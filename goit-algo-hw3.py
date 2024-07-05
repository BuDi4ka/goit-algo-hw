from datetime import datetime
import random

def get_days_from_today(date):
    try:
         date_formatted = datetime.strptime(date, "%Y-%m-%d") 
    except ValueError:
         return 'Неправильний формат дати. Використайте формат РРРР-ММ-ДД'
    date_today = datetime.today()
    date_diff = (date_today - date_formatted).days
    return date_diff

date_to_check = "2024-05-05"
print(get_days_from_today(date_to_check))


def get_numbers_ticket(min, max, quantity):
    win_list = []
    if (1000 > max > min > 1) and quantity != 0:
        while quantity > 0:
            number = random.randint(min, max)
            if number not in win_list:
                win_list.append(number)
                quantity -= 1 
        return sorted(win_list)
    else:
        return win_list

lottery_numbers = get_numbers_ticket(4, 7, 2) 
print("Ваші лотерейні числа:", lottery_numbers)
