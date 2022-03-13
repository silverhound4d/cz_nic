import csv
import sys


def read_args():
    if len(sys.argv) != 2:
        print(f"Requires 1 argument, {len(sys.argv) - 1} were given.")
        exit()
    return {"file_path": sys.argv[1]}

def get_data(path) -> list[dict]:
    with open(path, 'r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f, delimiter=";")
        my_dict = [dic for dic in csv_reader]
        return my_dict