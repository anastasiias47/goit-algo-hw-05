import sys
from pathlib import Path
from collections import Counter


path_from_terminal = sys.argv

path_string = path_from_terminal[1]
def file_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("There is no such file in directory")
    return inner

def parse_log_line(line: str) -> dict:
    log_items = line.split(' ')
    parsed_log_line = {'date': log_items[0], 'time': log_items[1], 'level':log_items[2], 'message': " ".join(log_items[3:])}
    return parsed_log_line

@file_error
def load_logs(file_path: str) -> list:
    absolute_file_path = Path(file_path)
    with open(file_path, 'r', encoding='utf-8') as source_file:
        log_lines = [parse_log_line(line) for line in source_file.read().splitlines(False)]
    return log_lines


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    matching_logs = [" ".join([line['date'], line['time'], "-", line['message']]) for line in logs if line['level'] == level]
    return matching_logs

def count_logs_by_level(logs: list) -> dict:
    level_count = Counter([line['level'] for line in logs])
    return level_count


def display_log_counts(counts: dict):
    print("{:<30} {:<30}".format('Рівень логування', 'Кількість' ))
    for key, value in counts.items():
        print("{:<30} {:<30} ".format(key, value))

if __name__ == '__main__':
    logs = load_logs(path_string)
    logs_counted = count_logs_by_level(logs)
    display_log_counts(logs_counted)
    if len(path_from_terminal) == 3:
        requested_level = path_from_terminal[2]
        logs_details = '\n'.join(filter_logs_by_level(logs,requested_level))
        print(f'Деталі для логів рівня {requested_level}:\n{logs_details}')


