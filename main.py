#2 вариант

def calculate_average(numbers): #основная функция
    if not numbers:
        return None
    return round(sum(numbers) / len(numbers))

