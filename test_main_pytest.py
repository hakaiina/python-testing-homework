from main import calculate_average

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