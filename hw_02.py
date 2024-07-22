from typing import Callable
import re

def generator_numbers(text: str):
    text_split = text.split(" ")
    for element in text_split:
        match = re.search(r'[0-9]+', element)
        if match:
            yield float(element)


def sum_profit(text: str, func: Callable):
    sum = 0
    gen = func(text)
    while True:
        try:
            sum += next(gen)
        except StopIteration:
            break
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

