from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="bundesbank-to-sqlite",
    description="Convert Bundesbank banking export to a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Andreas Madsack",
    url="https://github.com/mfa/bundesbank-to-sqlite",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["bundesbank_to_sqlite"],
    entry_points="""
        [console_scripts]
        bundesbank-to-sqlite=bundesbank_to_sqlite.cli:cli
    """,
    install_requires=[
        "sqlite-utils~=3.2.1",
        "click",
        "openpyxl"
    ],
    extras_require={"test": ["pytest"]},
    tests_require=["bundesbank-to-sqlite[test]"],
)
