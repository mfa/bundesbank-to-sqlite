import click
import sqlite_utils

from bundesbank_to_sqlite.utils import save_banking_data


@click.group()
@click.version_option()
def cli():
    "Convert Bundesbank blz data to a SQLite database"


@cli.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument(
    "xlsx_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    default="blz-aktuell-xls-data.xlsx",
)
def convert(db_path, xlsx_path):
    db = sqlite_utils.Database(db_path)
    save_banking_data(db, xlsx_path)
