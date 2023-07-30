from src.main import load_data_from_json, data_last_five, print_result
import pytest


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



