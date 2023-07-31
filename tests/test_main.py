from src.main import load_data_from_json, print_result
import pytest
import json

def test_load_data_from_json():
    test_file_path = 'test_operations.json'
    test_data = [
        {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
    ]

    with open(test_file_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f)

    loaded_data = load_data_from_json(test_file_path)
    assert len(loaded_data) == len(test_data)
    assert loaded_data == test_data


def test_load_data_from_json_nonexistent_file():
    file_path = 'nonexistent_file.json'
    with pytest.raises(FileNotFoundError):
        load_data_from_json(file_path)


def test_print_result():
    assert print_result(
        {
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
      "amount": "70946.18",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 10848359769870775355",
    "to": "Счет 21969751544412966366"
  }) == f'20.12.2018 Перевод организации\n' \
        f'Счет **5355 -> Счет **6366\n' \
        f'70946.18 USD\n'
    assert print_result(
        {
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
      "amount": "70946.18",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "to": "Счет 21969751544412966366"
  }) == f'20.12.2018 Перевод организации\n' \
        f'Не указано -> Счет **6366\n' \
        f'70946.18 USD\n'



