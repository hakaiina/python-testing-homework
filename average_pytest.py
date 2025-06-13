# 2 вариант


def calculate_average(numbers):  # основная функция
    if not numbers:
        return None
    return round(sum(numbers) / len(numbers))


def main():
    user_input = input("Введите числа через пробел: ").strip()
    if not user_input:
        print(None)
        return

    try:
        numbers = list(map(float, user_input.split()))
        print(calculate_average(numbers))
    except ValueError:
        print("Ошибка. Введите только числа.")


if __name__ == "__main__":
    main()

#tests


def test_average_normal_list():
    print("\nTested by Polina Starostina.")
    assert calculate_average([1, 2, 3, 4, 5]) == 3

def test_average_single_number():
    print("\nTested by Polina Starostina.")
    assert calculate_average([10]) == 10

def test_average_empty_list():
    print("\nTested by Polina Starostina.")
    assert calculate_average([]) is None

def test_average_with_floats():
    print("\nTested by Polina Starostina.")
    assert calculate_average([1.5, 2.5, 3.5]) == 2

def test_average_with_negatives():
    print("\nTested by Polina Starostina.")
    assert calculate_average([-1, -2, -3]) == -2

def test_average_rounding_up():
    print("\nTested by Polina Starostina.")
    assert calculate_average([1, 2]) == 2

def test_average_rounding_down():
    print("\nTested by Polina Starostina.")
    assert calculate_average([1, 1, 2]) == 1

if __name__ == "__main__":
    # Вывод информации о тестировщике
    tester_name = "Polina Starostina"
    print(f"\nTested by {tester_name}")