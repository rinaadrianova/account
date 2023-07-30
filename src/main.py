import json
from src.utils import transaction_cards, transfer_date, get_last_five


def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


file_path = 'D:/skypro/account_transactions/operations.json'
data = load_data_from_json(file_path)


def print_result(last_five):
    return f'{transfer_date(last_five[i]["date"])} {last_five[i]["description"]}\n' \
           f'{transaction_cards(last_five[i].get("from"))} -> {transaction_cards(last_five[i]["to"])}\n'\
           f'{last_five[i]["operationAmount"]["amount"]} {last_five[i]["operationAmount"]["currency"]["name"]}\n'


last_five = get_last_five(data)
for l in last_five:
    print(print_result(last_five))


