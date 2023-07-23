from utils import transfer_date
from utils import transaction_cards
import json

with open('operations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
last_five = []
while count < 5:
    if data[count].get('state') == "EXECUTED":
        last_five.append(data[count])
        count += 1


for i in range(len(last_five)):
    print(f'{transfer_date(last_five[i]["date"])} {last_five[i]["description"]}\n'
          f'{transaction_cards(last_five[i].get("from"))} -> {transaction_cards(last_five[i]["to"])}\n'
          f'{last_five[i]["operationAmount"]["amount"]} {last_five[i]["operationAmount"]["currency"]["name"]}\n')


