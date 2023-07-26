from src.utils import transfer_date, transaction_cards


def test_transfer_date():
    assert transfer_date("2019-07-03T18:35:29.512364") == "03.07.2019"
    assert transfer_date("2018-06-30T02:08:58.425572") == "30.06.2018"
    assert transfer_date("2018-03-23T10:45:06.972075") == "23.03.2018"


def test_transaction_cards():
    assert transaction_cards() == 'Не указано'
    assert transaction_cards("Счет 75106830613657916952") == 'Счет **6952'
    assert transaction_cards("Visa Classic 6831982476737658") == 'Visa Classic 6831 98** **** 7658'



