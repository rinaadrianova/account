import json
from src.utils import transaction_cards, transfer_date, get_last_five


def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


file_path = 'D:/skypro/account_transactions/operations.json'
data = load_data_from_json(file_path)


def print_result(data_last_five):
    return f'{transfer_date(data_last_five["date"])} {data_last_five["description"]}\n' \
           f'{transaction_cards(data_last_five.get("from"))} -> {transaction_cards(data_last_five["to"])}\n'\
           f'{data_last_five["operationAmount"]["amount"]} {data_last_five["operationAmount"]["currency"]["name"]}\n'


data_last_five = get_last_five(data)


for data in data_last_five:
    print(print_result(data))
