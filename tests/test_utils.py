import pytest
import sqlite_utils
from bundesbank_to_sqlite.utils import save_banking_data
from openpyxl import Workbook


@pytest.fixture
def xlsx_file():
    data = [('Bank-leitzahl', 'Merkmal', 'Bezeichnung', 'PLZ', 'Ort', 'Kurzbezeichnung', 'PAN', 'BIC', 'Prüfziffer-berechnungs-methode', 'Datensatz-nummer', 'Änderungs-kennzeichen', 'Bankleitzahl-löschung', 'Nachfolge-Bankleitzahl'), ('10000000', 1, 'Bundesbank', '10591', 'Berlin', 'BBk Berlin', '20100', 'MARKDEF1100', '09', '011380', 'U', 0, '00000000')]

    wb = Workbook()
    ws = wb.active
    ws.title = "Daten"
    for row in data:
        ws.append(row)

    # TODO: use TemporaryFile
    filename = '/tmp/test.xlsx'
    wb.save(filename = filename)
    return filename


def test_save_banking_data(xlsx_file):
    db = sqlite_utils.Database(memory=True)
    save_banking_data(db, xlsx_file)
    assert len(list(db["bundesbank_blz"].rows)) == 1
    assert len(list(db["bundesbank_blz"].rows)[0]) == 13
    assert list(db["bundesbank_blz"].rows)[0]["blz"] == "10000000"
    assert list(db["bundesbank_blz"].rows)[0]["city"] == "Berlin"
