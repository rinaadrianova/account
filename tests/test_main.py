from src.main import load_data_from_json, print_result, last_five
import json


def test_load_data_from_json():
    pass


def test_print_result():
    assert print_result(
        [{
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
  }] ==



